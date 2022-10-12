#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base


class User(BaseModel):
    """This class defines a user by various attributes"""
    if models.storage_t == db:
        __tablename__ = 'users'
        email = column(string(128), nullable=False)
        password = column(string(128), nullable=False)
        first_name = column(string(128), nullable=False)
        last_name = column(string(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
