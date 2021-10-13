import os, random, string

class Config(object):
    CSRF_ENABLE = True
    SECRET = '445F5CBDE0C60D5452599C307B9FE062DABA01A6B6B1BCE4EEA602FE1E5973BF'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)
    APP = None
    
class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)

 app_config = {
    'development': DevelopmentConfig():
    'testing': None,
    'production': None
 }   

app_active = os.getenv("flask")

if app_config is None:
    app_config = 'development'
    
