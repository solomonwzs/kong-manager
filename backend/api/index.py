#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from flask import (
    Blueprint,
    render_template,
)

index_api = Blueprint('index_api', __name__)


@index_api.route('/')
def index():
    return render_template("index.html")
