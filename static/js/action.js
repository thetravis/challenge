// JavaScript file by Heikki Pitkänen 20.10.2016 v0.1
// Contains the functions that are called by ../templates/catalog.html
// or ../templates/frontpage.html

// General TODO: Use json to move the data 
// General TODO: unit testing
// General TODO: exceptions handling

// simple ajax library for reading files
// TODO: Don't copy and paste, write it yourself 

function IO(U, V) {//LA MOD String Version. A tiny ajax library.  by, DanDavis
           var X = !window.XMLHttpRequest ? new ActiveXObject('Microsoft.XMLHTTP') : new XMLHttpRequest();
            X.open(V ? 'PUT' : 'GET', U, false);
            X.setRequestHeader('Content-Type', 'text/html')
            X.send(V ? V : '');
            return X.responseText;
        }

// Do the search when pressing Enter on the text field
// TODO: Should be able to add a function that is called on Enter 
        
function keypress(e){
        if(e.keyCode === 13){
            e.preventDefault(); // Ensure it is only this code that rusn
	    search();
        }
    }
    
var catalog = angular.module("catalog", []);

catalog.controller('catalogCtrl', catalogCtrl);

function catalogCtrl($scope, $http) {
    function updateView() {
      $http.get("phonebook/person/search/").then(function(response) {
            $scope.searchResults = response.data;
	});
    }
}
    
// Function to add products in the catalog
// TODO: draw the response on the screen
    
    
function addProduct() {
        $.ajax({
            url: '/catalog/add',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
}

// Function to update page when search/sorting changes
// TODO: Yet to be implemented
// param products list of products that are shown
    
function update(products) {

  
}

// Function to edit products 
// TODO: move onto another page
// TODO: How am I going to bind the product with its id? json? 
// TODO: Google 'how to use json to get data from database'
        
function edit_product() {
  
}

// Function to remove remove product from catalog
// TODO: Yet to be implemented

function remove_product() {
  
}

// Function to search from database
// TODO: Implementation on back-end side
// TODO: Should use update(response) to update page 
// 	 with search results
        
function search(searchCriteria) {
 
        $.ajax({
            url: '/catalog/search/'+encodeURIComponent(searchCriteria),
            data: '' ,
            type: 'GET',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }