#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """This class defines a user by various attributes"""
    if models.storage_t == 'db':
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
