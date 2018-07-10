#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from app import app
from api.index import index_page
from api.user import user_page
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s [%(levelname)s] [%(filename)s:%(lineno)d]' +
    '%(message)s'
)

app.register_blueprint(index_page)
app.register_blueprint(user_page)

if __name__ == "__main__":
    app.run()
