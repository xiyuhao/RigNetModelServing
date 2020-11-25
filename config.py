import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PersonalWebsite'
    MODEL_FOLDER = 'model\code'
    UPLOAD_FOLDER = os.path.join(basedir, 'quick_start')# 'quick_start'
