SECRET_KEY = 'qwerty123'

# Create Session config
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY_TABLE = 'sessions'

# Create in-memory database
DATABASE_FILE = 'sample_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Create Security Config
SECURITY_PASSWORD_SALT ='123456789'
SECURITY_EMAIL_SENDER='admin@app'

# Create EMail Configuration
MAIL_SERVER='smtp.mailtrap.io'
MAIL_PORT=2525
MAIL_USE_SSL=False
MAIL_USERNAME='6541661608ea11'
MAIL_PASSWORD='2cbe8473438708'
MAIL_USE_TLS=True


