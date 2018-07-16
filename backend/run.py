#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from app import app
from api.index import index_api
from api.kong import kong_api
from api.user import user_api
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s [%(levelname)s] [%(filename)s:%(lineno)d]' +
    '%(message)s'
)

app.register_blueprint(index_api)
app.register_blueprint(kong_api)
app.register_blueprint(user_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
