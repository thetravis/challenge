# coding=utf8

import mysql.connector
from mysql.connector import errorcode

# TODO consider the possibilities of abusing the database with SQL injection

class Database():
  
  # Initialize databe with connection to MySQL 
  
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
  
  def search(self, searchCriteria, sorting="name"):
    if searchCriteria == "":
       searchCriteria = "%"
    if sorting == "name":
      search_stmt = "SELECT * FROM product WHERE name LIKE (%s) ORDER BY name"
    if sorting == "price":
      search_stmt = "SELECT * FROM product WHERE name LIKE (%s) ORDER BY price"
    data = [str(searchCriteria)+"%"]
    self.cursor.execute(search_stmt, data)
    searchResult = self.cursor.fetchall()
    return searchResult
    
  # Add product to database
  
  def add(self, name, amount, price):
    insert_stmt = ("INSERT INTO product (name, amount, price) VALUES (%s, %s, %s)" )
    data = (str(name), str(amount), str(price))
    self.cursor.execute(insert_stmt, data)
    self.conn.commit()
    return "Addded " + name + " " + amount + " " + price
  
  # Remove product from the database
    
  def remove(self,prod_id):
    remove_stmt = "DELETE FROM product WHERE id=%s"
    data = [prod_id]
    self.cursor.execute(remove_stmt, data)
    self.conn.commit()
    return "Removed " + prod_id
    

  
  
  