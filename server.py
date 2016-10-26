# coding=utf8
'''
 Simple Python Flask server for running a web serverlication for
 a produt catalog by Heikki Pitkänen 20.10.2016. v0.1
 Serves catalog.html and frontpage.html, css and js files. Answers to search, add
 and edit (TODO) calls by the front-end UI.
'''

# General TODO: MySQL implementations for adding, searching and editing products.
# General TODO: unit testing
# General TODO: exceptions handling 

from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from catalog import Catalog

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

# Initialize the server and the catalog
server = Flask(__name__)
catalog = Catalog()
    
'''
This is supposed to read the database and return it for AJAX
TODO: How am I going to actually use this?
TODO: How about rather return whole database for front-end and let it 
      do the work?
'''

@server.route("/catalog/<int:x>/<int:y>",methods=['GET','POST'])
def catalogpagexy(x,y):
    if request.method == 'GET':
      return str(x) + " products per page, page number " + str(y)

'''
Search in the database
'''

@server.route("/catalog/search",methods=['GET','POST'])
@server.route("/catalog/search/",methods=['GET','POST'])
@server.route("/catalog/search/<string:searchCriteria>",methods=['GET','POST'])
def search(searchCriteria=""):
  return catalog.search(searchCriteria)

'''
Route for the catalog page. 
'''

@server.route("/catalog",methods=['GET'])
def catalogpage():
    return render_template("catalog.html");
    
'''
Route for adding new products into the database.
TODO: Should return "success" or "failure" 
'''
    
@server.route("/catalog/add",methods=['POST'])
def add():
    if request.method == 'POST':
      # read the posted values from the UI
      name = request.form.get('addProductName', "Couldn't find addProductName")
      amount = request.form.get('addProductAmount', "Couldn't find the addProductAmount")
      price = request.form.get('addProductPrice', "Couldn't find the addProductPrice")
      # TODO add the product into the database and return the the successfullness
      return catalog.add(name, amount, price)
    if request.method == 'GET':
      return render_template("catalog.html")

'''
Returns the front page
'''

@server.route("/")
def frontpage():
    return render_template("frontpage.html")

if __name__ == "__main__":
  server.run()

