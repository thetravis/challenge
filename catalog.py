# coding=utf8

from database import Database
import json

class Catalog():
  def __init__(self, name="Katalogi"):
    self.name = name
    self.database = Database()
  
  # Search from catalog
  
  def search(self, searchCriteria):
    return json.dumps(self.database.search(searchCriteria))
  
  # Add product into catalog
  
  def add(self, name,amount,price):
    return json.dumps(self.database.add(name,amount,price))
    
    
    
    