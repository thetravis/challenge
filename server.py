# coding=utf8
'''
 Simple Python Flask server for running a web application for
 a produt catalog by Heikki Pitkänen 20.10.2016. v0.1
 Serves catalog.html and frontpage.html, css and js files. Answers to search, add
 and edit (TODO) calls by the front-end UI.
'''

# General TODO: MySQL implementations for adding, searching and editing products.
# General TODO: unit testing
# General TODO: exceptions handling 

from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'server'
app.config['MYSQL_DATABASE_PASSWORD'] = 'radiobutton2'
app.config['MYSQL_DATABASE_DB'] = 'catalog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#def readfile(filename):
    #try:
        #file_object = open(filename, 'r')
	#return file_object.read()
    #except FileNotFound:
        #file_object = open(filename, 'w+')
    #finally:
        #file_object.close()
    
'''
This is supposed to read the database and return it for AJAX
TODO: How am I going to actually use this?
TODO: How about rather return whole database for front-end and let it 
      do the work?
'''

@app.route("/catalog/<int:x>/<int:y>",methods=['GET','POST'])
def catalogxy(x,y):
    if request.method == 'GET':
      return str(x) + " products per page, page number " + str(y)

def addProduct(name, amount, price):
  #Add product to catalog
  #TODO: mySQL database
  return "Database answers: " + str(name) + " " + str(amount) + " " + str(price)

'''
Search in the database
TODO: This should be able to return something else than just the whole database
'''

def search(search_text):
  # Return data from the database
  # TODO: return what is actually searched for
  cursor.execute("SELECT * FROM tbl_product") # WHERE name_product STARTS WITH search_text ?
  name = cursor.fetchone()
  if data is None:
     return "No results"
  else:
     return str(data)

'''
Route for the catalog page. 
GET and obtain catalog.html
POST and obtain data from the database
'''

@app.route("/catalog",methods=['GET','POST'])
def catalog():
    if request.method == 'POST':
      # read the posted values from the UI
      search_text = request.form.get('searchText', "Couldn't find the name")
      return search(search_text)
    if request.method == 'GET':
      return render_template("catalog.html")
    # default action
    return render_template("catalog.html");
    
'''
Route for adding new products into the database.
TODO: MySQL implementation for adding. INSERT x,y,z VALUES j,k,l etc.
TODO: Should return "success" or "failure" 
'''
    
@app.route("/catalog/add",methods=['GET','POST'])
def add():
    if request.method == 'POST':
      # read the posted values from the UI
      name = request.form.get('addProductName', "Couldn't find addProductName")
      amount = request.form.get('addProductAmount', "Couldn't find the addProductAmount")
      price = request.form.get('addProductPrice', "Couldn't find the addProductPrice")
      # TODO add the product into the database and return the the successfullness
      return addProduct(name, amount, price)
    if request.method == 'GET':
      return render_template("catalog.html")
    # default action. Is this really needed?
    return render_template("catalog.html");    
    
'''
Returns the front page
'''

@app.route("/")
def frontpage():
    return render_template("frontpage.html")

if __name__ == "__main__":
  app.run()

