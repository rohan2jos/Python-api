first-api

For screenshots and more description: https://github.com/rohan2jos/Python-api/blob/master/readme.md

basic api for getting a list of stores, adding a store, getting the items in a store and adding an item to a particular store

the stores is a python list

endpoints:

POST /store data: {name:}
- create a new store with a given name

GET /store/<string:name>
- Get a store for the given name with the data

GET /store
- Get the list of all stores

POST /store/<string:name>/item
- Create an item with a specific name inside of the store

GET /store/<string:name>/item
- Get all the items in the specific store
