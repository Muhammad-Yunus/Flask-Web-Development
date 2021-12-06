SECRET_KEY = 'qwerty123'

# Create Session config
SESSION_TYPE = 'sqlalchemy'
SESSION_SQLALCHEMY_TABLE = 'sessions'

# Create in-memory database
DATABASE_FILE = 'IOTPLATFORM'
SQLALCHEMY_DATABASE_URI = 'mysql://user:user@localhost/' + DATABASE_FILE
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

# Create MQTT Configuration
MQTT_BROKER_URL='broker.hivemq.com'  # use the free broker from HIVEMQ
MQTT_BROKER_PORT=1883  # default port for non-tls connection
MQTT_USERNAME=''  # set the username here if you need authentication for the broker
MQTT_PASSWORD=''  # set the password here if the broker demands authentication
MQTT_KEEPALIVE=5  # set the time interval for sending a ping to the broker to 5 seconds
MQTT_TLS_ENABLED=False  # set TLS to disabled for testing purposes
