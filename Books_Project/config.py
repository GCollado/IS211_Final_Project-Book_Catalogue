import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Gets location of the application's database from the configuration variable.
class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET-KEY') or 'The_answer_is_42'
