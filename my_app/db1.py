import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="tonya",
    passwd="171064",
    db="lab5"
)

c = db.cursor()

# c.execute("INSERT INTO customer(name, surname) VALUES(%s, %s);", ('Владимир', 'Федоров'))
db.commit()

c.execute("select customer.name, customer.surname, pic.picname, pic.description from customer join purchase as pur on(pur.idcustomer=customer.customerid) join pictures as pic on(pic.id=pur.idpicture);")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()
