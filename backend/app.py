#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from config import cfg
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path

current_file = path.basename(__file__)
dist_path = path.join(path.dirname(path.abspath(current_file)), "dist")

app = Flask(__name__,
            static_folder=path.join(dist_path, "static"),
            template_folder=dist_path)
app.config.update(
    DEBUG=cfg.DEBUG,
    SECRET_KEY=cfg.SECRET_KEY,
    SQLALCHEMY_DATABASE_URI=cfg.pg_uri(),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy()
db.init_app(app)
