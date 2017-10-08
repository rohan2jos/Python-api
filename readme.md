Github repository for python api learning

Purpose: This repository contains all the code that I have written when learning Python restful api's with Flask

Contents:

The folders in the repository are for the following:
	- first-api
		- This contains basic code for an in memory data object
		- Code for setting up basic endpoints


		ENDPOINTS:

		1. GET endpoint for store list - /store:

		![first_api_get](https://user-images.githubusercontent.com/12286807/31319878-b5ea9c8e-ac30-11e7-849a-73cd7045e920.jpg)
		
		2. GET endpoint for store with particular name - /store/<name>:
	
		![first_api_get_store_by_name](https://user-images.githubusercontent.com/12286807/31321438-c10898da-ac4b-11e7-8e3b-f3c2b1e9a2f2.jpg)

		3. POST endpoint to create a new store - /store:

		![first_api_create_new_store](https://user-images.githubusercontent.com/12286807/31321454-f29bcf48-ac4b-11e7-82ee-7d0c6bf2c9a4.jpg)

		4. POST endpoint to create a new item in the store specified by a particular name: /store/<name>/item

		![first_api_create_new_item](https://user-images.githubusercontent.com/12286807/31321462-1905cbc0-ac4c-11e7-91e0-cff84c1e04b0.jpg


	-first-api-mongo
		- This contains code for the same endpoints, but with the data in mongo-db
	- api-venv
		- This contains code for Flask-restful and JWT
		- This contains test first code and authentication and session management
