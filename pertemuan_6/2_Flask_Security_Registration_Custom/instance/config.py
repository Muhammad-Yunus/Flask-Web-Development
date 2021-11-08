SECRET_KEY = 'qwerty123'

# Create Session config
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY_TABLE = 'sessions'

# Create in-memory database
DATABASE_FILE = 'sample_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create Security Config
SECURITY_PASSWORD_SALT = '123456789'
SECURITY_EMAIL_SENDER='admin@app'

# Create EMail Configuration
MAIL_SERVER='smtp.mailtrap.io'
MAIL_PORT=2525
MAIL_USE_SSL=False
MAIL_USERNAME=''
MAIL_PASSWORD=''
MAIL_USE_TLS=True
