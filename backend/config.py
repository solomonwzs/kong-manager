#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = 'JPOaB5dREH0vONQSJzb6'

    PG_HOST = 'localhost'
    PG_PORT = 5432
    PG_DB = 'kong_tests'
    PG_USER = ''
    PG_PASS = ''

    KONG_ADM_HOST = 'http://192.168.197.130:9001'

    def pg_uri(self):
        if self.PG_USER != '' and self.PG_PASS != '':
            return f'postgresql://{self.PG_USER}:{self.PG_PASS}@\
{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}'
        else:
            return f'postgresql://{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB}'


class DevConfig(Config):
    NODE_ENV = 'development'


class TestConfig(Config):
    NODE_ENV = 'testing'


class ProdConfig(Config):
    DEBUG = False
    NODE_ENV = 'production'


env = os.environ.get('ENV')
cfg = DevConfig()
if env == 'testing':
    cfg = TestConfig()
elif env == 'production':
    cfg = ProdConfig()
