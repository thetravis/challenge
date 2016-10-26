# coding=utf8

import mysql.connector
from mysql.connector import errorcode

class Database():
  def __init__(self, name="Database"):
    config = {
      'user': 'server',
      'password': 'radiobutton2',
      'host': 'localhost',
      'database': 'catalog',
      'raise_on_warnings': True,
    }
    self.conn = mysql.connector.connect(**config)
    self.cursor = self.conn.cursor()
    self.name = name
  
  # Search from database
  
  def search(self, searchCriteria):
    if searchCriteria == "":
       searchCriteria = "%"
    search_stmt = "SELECT * FROM product WHERE name LIKE (%s)"
    data = [str(searchCriteria)+"%"]
    self.cursor.execute(search_stmt, data)
    products = self.cursor.fetchall()
    return products
    
  # Add product to database
  
  def add(self, name, amount, price):
    insert_stmt = ("INSERT INTO product (name, amount, price) VALUES (%s, %s, %s)" )
    data = (str(name), str(amount), str(price))
    self.cursor.execute(insert_stmt, data)
    self.conn.commit()
    return "Addded " + name + " " + amount + " " + price
  
  def remove(id):
    insert_stmt = ("DELETE FROM product WHERE id=%s" )
    data = (id)
    self.cursor.execute(remove_stmt, data)
    self.conn.commit()
    return "Removed " + id
  
  