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
from dao.service import Service
from werkzeug.local import LocalProxy
import base64
import collections
import hashlib
import hmac
import logging
import os
import struct
import time


user_page = Blueprint('user_page', __name__)
secret_key = cfg.SECRET_KEY.encode('utf8')

CookieInfo = collections.namedtuple(
    'cookie_info',
    'salt, timestamp, uid, sign'
)
cookie_info = LocalProxy(lambda: _get_cookie_info())


def api_auth(fn):
    def wrapper():
        if cookie_info._get_current_object() is not None:
            return fn()
        else:
            return jsonify({"message": "unauthorized"}), 401
    return wrapper


def gen_cookie(uid):
    ts = int(time.time())
    salt = os.urandom(4)
    p = struct.pack('4sI8s', salt, ts, uid)
    sign = hmac.new(secret_key, p, hashlib.md5).digest()
    buf = struct.pack('4sI8s16s', salt, ts, uid, sign)
    return base64.urlsafe_b64encode(buf)


def parse_cookie(cookie):
    try:
        buf = base64.urlsafe_b64decode(cookie)
        info = CookieInfo._make(struct.unpack('4sI8s16s', buf))
        p = struct.pack('4sI8s', info.salt, info.timestamp, info.uid)
        sign = hmac.new(secret_key, p, hashlib.md5).digest()
        if sign == info.sign:
            return info
        else:
            return None
    except Exception:
        return None


def _get_cookie_info():
    cookie = request.headers.get('X-Rf-Api-Cookie')
    if cookie is not None:
        return parse_cookie(cookie.encode('utf8'))
    return None


@user_page.route('/api/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    logging.debug(data)

    uid = f'{data["name"]}-{data["pawd"]}'
    cookie = gen_cookie(uid.encode('utf8'))

    return jsonify({
        'cookie': cookie.decode('utf8'),
        'user': {
            'name': 'Solomon'
        }
    })


@user_page.route('/api/user', methods=['GET'])
@api_auth
def user():
    s = Service.query.filter_by(name='0x01-my-service-api-0').first()
    logging.debug(s)
    return jsonify({'name': 'Solomon'})
