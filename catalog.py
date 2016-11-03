# coding=utf8

from database import Database
import json

class Catalog():
  def __init__(self, name="Catalog"):
    self.name = name
    self.database = Database()
  
  # Search from catalog
  
  def search(self, searchCriteria, sorting):
    return json.dumps(self.database.search(searchCriteria, sorting))
  
  # Add product into catalog
  
  def add(self, name,amount,price):
    return json.dumps(self.database.add(name,amount,price))
  
  # Remove product from catalog based on id
  
  def removeProduct(self, prod_id):
    return json.dumps(self.database.remove(prod_id))
  
  # Edit product. This actually adds new product with 
  # edited data and removes the old one 
  # TODO Which is better? Editing existing product in database or removing
  # the old and adding new? 
  
  def edit(id, newname, newamount, newprice):
    addition = self.add(newname, newamount, newprice)
    removal = self.database.remove(id)
    return json.dumps(addition + "\n" + removal)
    