from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose' # JWT is json web token
api = Api(app) # allows us to add resources to the API

jwt = JWT(app, authenticate, identity) # creates /auth endpoint, send username and password

items = []

# inherits from resource
class Item(Resource): 
    @jwt_required()
    def get(self, name):
        # iterate through all items and return the item
        item = next(filter(lambda x: x['name'] == name, items), None) # next gives first item found by filter function, None prevents error from occuring if no values
        return {'item': item}, 200 if item else 404 # not found
    
    def post(self,name):
        # IF (we've found an item and its not null, it matches the name)
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # error checking for bad request

        data = request.get_json(silent=True) # can pass force=True (dont need content type header) or silent=True (doesnt give error, returns none)
        item = {
            'name': name,
            'price': data['price']
        }
        items.append(item)
        return item, 201 # created
    

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') # get at with localhost/student/<name>. kind of like @app.route(), but we dont need the decorator
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
    