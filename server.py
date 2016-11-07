# coding=utf8
'''
 Simple Python Flask server for running a web serverlication for
 a produt catalog by Heikki Pitkänen 20.10.2016. v0.1
 Serves catalog.html and frontpage.html, css and js files. Answers to search, add
 and edit (TODO) calls by the front-end UI.
'''

# General TODO: unit testing
# General TODO: exceptions handling 

from flask import Flask, render_template, request, json, send_from_directory
from catalog import Catalog
import urllib

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

@server.route("/catalog/search",methods=['GET'])
@server.route("/catalog/search/",methods=['GET'])
@server.route("/catalog/search/<string:searchCriteria>",methods=['GET'])
@server.route("/catalog/search//<string:sorting>",methods=['GET'])
@server.route("/catalog/search/<string:searchCriteria>/<string:sorting>",methods=['GET'])
def search(searchCriteria="", sorting=""):
  return catalog.search(urllib.unquote(searchCriteria), urllib.unquote(sorting))

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
  # read the posted values from the UI
  name = request.form.get('addProductName', "Couldn't find addProductName")
  amount = request.form.get('addProductAmount', "Couldn't find the addProductAmount")
  price = request.form.get('addProductPrice', "Couldn't find the addProductPrice")
  # TODO return something is unsuccessful
  return catalog.add(name, amount, price)

'''
Remove a product matching to an id
TODO: Should return "succes" or "failure"
'''

@server.route("/catalog/remove/",methods=['POST'])
def remove():
  # TODO return something if unsuccessful
  prod_id = request.get_data()
  return catalog.removeProduct(prod_id);

'''
Returns the front page
'''

@server.route("/")
def frontpage():
   return render_template("frontpage.html")

if __name__ == "__main__":
  server.run()

