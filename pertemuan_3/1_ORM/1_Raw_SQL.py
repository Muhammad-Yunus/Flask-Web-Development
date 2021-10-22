import sqlite3

conn = sqlite3.connect("pertemuan_3\\1_ORM\\ExampleDatabase.db")
c = conn.cursor()


# CREATE TABLE
c.execute("CREATE TABLE USER(NAME varchar(255), \
                        EMAIL varchar(255), \
                        PASSWORD varchar(255), \
                        IS_ACTIVE bool)")


# INSERT DATA
c.execute("INSERT INTO USER (NAME, EMAIL, PASSWORD, IS_ACTIVE) \
                        VALUES ('John Doe', 'john@mail.com', 'john123', True)")
conn.commit()


# SELECT DATA
c.execute("SELECT * FROM USER")
rows = c.fetchall()
for row in rows:
    print(row)