// JavaScript file by Heikki Pitkänen 20.10.2016 v0.1
// Contains the functions that are called by ../templates/catalog.html
// or ../templates/frontpage.html

// General TODO: Use actual json to move the data
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
        
function keypress(e, f){
  if(f == 'search' ) {
        if(e.keyCode === 13){
            e.preventDefault(); // Ensure it is only this code that rusn
	    update();
        }
  }
  if(f == 'add' ) {
        if(e.keyCode === 13){
            e.preventDefault(); // Ensure it is only this code that rusn
	    addProduct();
        }    
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
  document.getElementById("addProductName").value = ""
  document.getElementById("addProductAmount").value = ""
  document.getElementById("addProductPrice").value = ""
  update()
}

// Function to update page when search/sorting changes or after addition, editions and deletions 
    
function update() {
  var sorting = document.getElementById("sort_by")
  var selection = sorting.options[sorting.selectedIndex].value
  var searchCriteria = document.getElementById('searchCriteria').value
  search(searchCriteria, selection)
}

// Function to edit products 
// TODO: move onto another page
// TODO: How am I going to bind the product with its id? json? 
        
function edit_product(id) {
  
  console.log("TODO: Edit product " + id)
  
  update()
}

// Function to remove remove product from catalog

function removeProduct(id) {
  console.log("Remove " + id)
  $.ajax({
    url: '/catalog/remove/' + encodeURIComponent(id),
    data: '',
    type: 'GET',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
  update()
}

// Function to search from database
// Updates the product list with search results corresponding to
// user input of search and sorting selection.
        
function search(searchCriteria, sorting) {

  $.ajax({
            url: '/catalog/search/'+encodeURIComponent(searchCriteria)+'/'+encodeURIComponent(sorting),
            data: '' ,
            type: 'GET',
            success: function(response) {
                console.log(response);
		var searchResults = JSON.parse(response)
// 		console.log(searchResults)
		var old_tbody = document.getElementById("productTableBody");
		var new_tbody = document.createElement("tbody")
		new_tbody.id = "productTableBody"
		for ( i = 0; i < searchResults.length; ++i ) {
		 var row = new_tbody.insertRow(-1)
		 var cell1 = row.insertCell(0)
		 var cell2 = row.insertCell(1)
		 var cell3 = row.insertCell(2)
		 var cell4 = row.insertCell(3)
		 cell1.innerHTML = searchResults[i][1];
		 cell2.innerHTML = searchResults[i][2];
		 cell3.innerHTML = searchResults[i][3];
		 cell4.innerHTML = '<input type="button" value="Edit" onclick="edit_product(' + searchResults[i][0] + ')"> <input type="button" value="Remove" onclick="removeProduct(' + searchResults[i][0] + ')">'
		}
		 old_tbody.parentNode.replaceChild(new_tbody, old_tbody)
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
    
// This is some AngularJS BS that is not used yet
// 
// var catalog = angular.module("catalog", []);
// 
// catalog.controller('catalogCtrl', catalogCtrl);
// 
// function catalogCtrl($scope, $http) {
//     function updateView() {
//       $http.get("/catalog/search/").then(function(response) {
//             $scope.searchResults = response.data;
// 	});
//     }
//     updateView();
//     $scope.searchCriteria = "";
//     $scope.search = function(searchCriteria) {
// 	$http.get("/catalog/search/"+encodeURIComponent(searchCriteria)).then(function(response) {
//             $scope.searchResults = response.data;
// 	},function(response){
// 	    console.log(response)
// 	});
//     };
// } 
