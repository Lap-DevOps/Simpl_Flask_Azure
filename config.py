class Config:
    SECRET_KEY = 'your_secret_key'
    SECURITY_PASSWORD_SALT = 'kjsdhkjsdkjhkjds'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    PROPAGATE_EXCEPTIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_CONFIG = 'DevelopmentConfig'


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    FLASK_CONFIG = 'TestingConfig'


class ProductionConfig(Config):
    SECRET_KEY = 'your_secret_key'
    FLASK_CONFIG = 'ProductionConfig'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
