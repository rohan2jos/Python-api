import logging
logging.basicConfig(filename="logs/app.log", level=logging.DEBUG, format='%(asctime)s %(funcName)5s() %(levelname)s: %(lineno)d  %(message)s', datefmt='%I:%M:%S %p')

'''
400: Bad request, this is the client's fault
404: Item not found
201: Item created
202: Accepted - when delaying the creation (the creation has been accepted and is happening in the background)
'''

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

#1.  initialize the app as a Flask app
app = Flask(__name__)

#2. set a secret key for the Flask app which is used for session management
app.secret_key = 'rohan'

#3. initialize the api as Api with app as the Flask app
api = Api(app)


'''
jwt creates a new endpoint /auth
when we call /auth, we send it a username and a password
the jwt extension takes this username and password and sends it to
the authenticate function
authenticate(username, password) [in security.py]
if the user is found, then the jwt extension returns a jw token for the user
this token is used in identity(payload) in security.py
'''
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):

    '''
    return the item with the name specified
    if the item is not found, return a message and 404: Not found

    jwt_required is required to authenticate the user before the get is called
    '''
    @jwt_required()
    def get(self, name):
        logging.debug('get for Item')
        for x in items:
            if x['name'] == name:
                return x, 200
        return 404


    '''
    insert an item with the specified name
    create a temporary item and insert it into items
    after creating, return the created item and 201: Created
    If the request is bad, and the client has requested a name that is already
    present in the list, then return a 400: Bad request message/error
    '''
    def post(self, name):
        '''
        if next(filter(lambda x: x['name'] == name, items)):
            return {"message", "item with name {} already exists".format(name)}, 400
        '''
        for x in items:
            if x['name'] == name:
                return {"message": "the item already exits"}, 400

        data = request.get_json(force=True)
        data_price = data['price']
        logging.debug('post for Item ' + name + " with price " + str(data_price))
        temp_item = {'name': name, 'price': data_price}
        items.append(temp_item)
        return temp_item, 201


'''
class for a list of items
'''
class ItemList(Resource):
    def get(self):
        print "get in ItemList"
        return {'items': items}, 200


# ensure that the argument in the signature is the same as the json arg
# in this case, name because <string:name>
api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/itemlist')
app.run(port=5002, debug=True)