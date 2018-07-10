#!/usr/bin/python3
# encoding: utf-8

__author__ = "Solomon Ng"

from app import db
from dao.base import BaseModel
from sqlalchemy.dialects.postgresql import (
    BIGINT,
    TEXT,
    TIMESTAMP,
    UUID,
)


class Service(BaseModel):
    __tablename__ = 'services'
    id = db.Column(UUID, primary_key=True)
    created_at = db.Column(TIMESTAMP)
    updated_at = db.Column(TIMESTAMP)
    name = db.Column(TEXT)
    retries = db.Column(BIGINT)
    protocol = db.Column(TEXT)
    host = db.Column(TEXT)
    port = db.Column(BIGINT)
    path = db.Column(TEXT)
    connect_timeout = db.Column(BIGINT)
    write_timeout = db.Column(BIGINT)
    read_timeout = db.Column(BIGINT)
