import sqlalchemy as db

engine = db.create_engine('sqlite:///pertemuan_3\\1_ORM\\ORMExampleDatabase.db', echo = True)
meta = db.MetaData()

# CREATE TABLE
User = db.Table(
    'User', meta,
    db.Column('NAME', db.String(255)),
    db.Column('EMAIL', db.String(255)),
    db.Column('PASSWORD', db.String(255)),
    db.Column('IS_ACTIVE', db.Boolean)
    )
meta.create_all(engine)

# INSERT DATA
conn = engine.connect()
user = User.insert().values(NAME = 'John Doe',
                    EMAIL = 'john@gmail.com',
                    PASSWORD = 'john123',
                    IS_ACTIVE = True)
conn.execute(user)



# SELECT DATA
conn = engine.connect()
users = User.select()
results = conn.execute(users)
for row in results:
   print (row)

   