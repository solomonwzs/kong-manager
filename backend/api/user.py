#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from flask import (
    Blueprint,
    json,
    jsonify,
    request,
)
from config import cfg
# from dao.service import Service
from werkzeug.local import LocalProxy
import base64
import collections
import hashlib
import hmac
# import logging
import os
import struct
import time


user_api = Blueprint('user_api', __name__)
secret_key = cfg.SECRET_KEY.encode('utf8')

CookieInfo = collections.namedtuple(
    'cookie_info',
    'salt, timestamp, uid, sign'
)
cookie_info = LocalProxy(lambda: _get_cookie_info())


class User(object):
    def __init__(self, uid):
        self.uid = uid
        self.name = 'Solomon'


def login_user(name, pawd):
    uid = hashlib.md5((f'{name}{pawd}').encode('utf8')).hexdigest()
    return User(uid)


def api_auth(fn):
    def wrapper():
        if cookie_info._get_current_object() is not None:
            return fn()
        else:
            return jsonify({'message': 'unauthorized'}), 401
    return wrapper


def gen_cookie(uid):
    ts = int(time.time())
    salt = os.urandom(4)
    p = struct.pack('4sI16s', salt, ts, uid)
    sign = hmac.new(secret_key, p, hashlib.md5).digest()
    buf = struct.pack('4sI16s16s', salt, ts, uid, sign)
    return base64.urlsafe_b64encode(buf)


def parse_cookie(cookie):
    try:
        buf = base64.urlsafe_b64decode(cookie)
        info = CookieInfo._make(struct.unpack('4sI16s16s', buf))
        p = struct.pack('4sI16s', info.salt, info.timestamp, info.uid)
        sign = hmac.new(secret_key, p, hashlib.md5).digest()
        if sign == info.sign:
            return info
        else:
            return None
    except Exception:
        return None


def _get_cookie_info():
    cookie = request.headers.get('X-Kong-Api-Cookie')
    if cookie is not None:
        return parse_cookie(cookie.encode('utf8'))
    return None


@user_api.route('/api/login', methods=['POST'])
def login():
    data = json.loads(request.data)

    user = login_user(data.get('name'), data.get('pawd'))
    if user is None:
        return jsonify({'message': 'login failed'}), 403

    cookie = gen_cookie(user.uid.encode('utf8'))
    return jsonify({
        'cookie': cookie.decode('utf8'),
        'user': {
            'name': 'Solomon'
        }
    })


@user_api.route('/api/user', methods=['GET'])
@api_auth
def user():
    uid = cookie_info.uid.decode('utf8')
    user = User(uid)
    return jsonify({
        'name': user.name,
        'uid': uid,
    })
