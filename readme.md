Github repository for python api learning
=========================================
Purpose: This repository contains all the code that I have written when learning Python restful api's with Flask

Contents:

The folders in the repository are for the following:
	- first-api
		- This contains basic code for an in memory data object
		- Code for setting up basic endpoints


ENDPOINTS:
---------
		1. GET endpoint for store list - /store:
		The GET endpoint for /store returns a list of stores in the in-memory Dictionary 'stores'
			- We return a jsonified version of the dictionary, since the Python 'stores' in the code is a list of dictionaries

A screenshot of the GET endpoint for /store returning the list of stores is shown below:

![first_api_get](https://user-images.githubusercontent.com/12286807/31319878-b5ea9c8e-ac30-11e7-849a-73cd7045e920.jpg)
		
		2. **GET endpoint for store with particular name - /store/<name>:**
		The GET endpoint for /store/<name> takes the name of the particular store in the url
			- We use the name that is sent in the url, and iterate over the 'stores'
			- If the store is found, we return a jsonified store
			- If the store is not found, we return a jsonified message telling the store was not found

A screenshot of the GET endpoint for /store/<name> returning a particular store by name is shown below:

![first_api_get_store_by_name](https://user-images.githubusercontent.com/12286807/31321479-62ce810c-ac4c-11e7-9379-24fdf90e78ef.jpg)


		3. **POST endpoint to create a new store - /store:**
		The POST endpoint to create a new store takes the data in the Body of the Header
			- The JSON data - name and list of items is sent via the Body in the header of the request
			- The request.get_json() is used to extract the supplied data
			- Once the data is taken, the new store is created and appended to the in-memory 'stores'

A screenshot of the POST endpoint creating a new store with the data sent in the header of the request is shown below:

![first_api_create_new_store](https://user-images.githubusercontent.com/12286807/31321454-f29bcf48-ac4b-11e7-82ee-7d0c6bf2c9a4.jpg)

		4. **POST endpoint to create a new item in the store specified by a particular name: /store/<name>/item**
		The POST endpoint to create a new item in a particular store uses the name of the store passed in through the url and
		the item details passed in through the header of the request
			- The name will be searched for in the in-memory 'stores' and then if found, a new item will be appended
			to the list of items for that store
			- We will then return a jsonified item that has just been created
			- If the name is not found in the in-memory 'stores', we will return a jsonified message saying so

A screenshot of the POST endpoint to create a new item in a particular store is shown below:

![first_api_create_new_item](https://user-images.githubusercontent.com/12286807/31321462-1905cbc0-ac4c-11e7-91e0-cff84c1e04b0.jpg)


	-first-api-mongo
		- This contains code for the same endpoints, but with the data in mongo-db
	- api-venv
		- This contains code for Flask-restful and JWT
		- This contains test first code and authentication and session management
