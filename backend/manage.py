#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from app import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
