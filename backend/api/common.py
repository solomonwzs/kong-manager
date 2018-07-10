#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from flask import jsonify
from app import app


class InvalidUsage(Exception):
    status_code = 400


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
