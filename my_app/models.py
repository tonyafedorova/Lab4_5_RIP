from django.db import models

import MySQLdb


#  Реализация ручками классов
# class Connection:
#     def __init__(self, user, password, db, host='localhost'):
#         self.user = user
#         self.host = host
#         self.password = password
#         self.db = db
#         self._connection = None
#
#     @property
#     def connection(self):
#         return self._connection
#
#     def __enter__(self):
#         self.connect()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.disconnect()
#
#     def connect(self):
#         if not self._connection:
#             self._connection = MySQLdb.connect(
#                 host=self.host,
#                 user=self.user,
#                 passwd=self.password,
#                 db=self.db
#             )
#
#     def disconnect(self):
#         if self._connection:
#             self._connection.close()
#
#
# class Customer:
#     def __init__(self, db_connection, name, surname):
#         self.db_connection = db_connection.connection
#         self.name = name
#         self.surname = surname
#
#     def save(self):
#         c = self.db_connection.cursor()
#         c.execute("INSERT INTO customer(name, surname) VALUES(%s, %s);",
#             (self.name, self.surname))
#         self.db_connection.commit()
#         c.close()
#
#
# con = Connection("tonya", "171064", "lab5")
#
# with con:
#     customer = Customer(con, "Сергей", "Алексеев")
#     customer.save()


class CustomerModel(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)



class PictureModel(models.Model):
    picname = models.CharField(max_length=30)
    description = models.CharField(max_length=255)


class PurchaseModel(models.Model):
    idcustomer = models.IntegerField()
    idpicture = models.IntegerField()


