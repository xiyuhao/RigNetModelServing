# -*- coding: utf-8 -*-
"""
Created on Fri April  3 2020
"""

from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
# app.static_folder = 'static'



from app import routes
