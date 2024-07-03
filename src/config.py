import os

class Config(object):
    def __init__( self, app ):
        self.app = app
        self.DEBUG = True
        self.DEVELOPMENT = True
        self.SECRET_KEY = os.urandom(32)
        self.WTF_CSRF_SECRET_KEY = os.urandom(32)

class DevConfig(Config):
    def __init__(self, app):
        super().__init__(app)
        basedir = os.path.join(self.app.root_path)
        self.SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, '../', 'database' , 'app.db')
        print('Coneting to DB : ', self.SQLALCHEMY_DATABASE_URI)

class ProductionConfig(Config):
    def __init__(self, app):
        super().__init__(app)
        self.DEVELOPMENT = False
        self.DEBUG = False