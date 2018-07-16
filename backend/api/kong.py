#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from flask import (
    Blueprint,
    jsonify,
    request,
    make_response,
)
from api.user import (
    User,
    api_auth,
    cookie_info,
)
from config import cfg
import logging
import requests

kong_api = Blueprint('kong_api', __name__)


def permission_ok(method, path):
    user = User(cookie_info.uid.decode('utf8'))
    logging.debug(user)
    return True


@kong_api.route(r'/api/kong',
                methods=['POST', 'GET', 'PATCH', 'DELETE', 'PUT'])
@api_auth
def kong_proxy():
    path = request.headers.get('X-Rf-Kong-Ep')
    method = request.method
    body = request.data

    if not permission_ok(method, path):
        return jsonify({'message': 'unauthorized'}), 401

    headers = {}
    if len(body) != 0:
        headers['Content-Type'] = 'application/json'

    logging.debug(body)
    res = requests.request(method, f'{cfg.KONG_ADM_HOST}{path}', data=body,
                           headers=headers)
    resp = make_response(res.text)
    resp.headers['Content-Type'] = res.headers.get('Content-Type')

    return resp, res.status_code
