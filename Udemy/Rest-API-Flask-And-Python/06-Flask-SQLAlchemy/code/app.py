from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose' # JWT is json web token
api = Api(app) # allows us to add resources to the API

jwt = JWT(app, authenticate, identity) # creates /auth endpoint, send username and password

api.add_resource(Item, '/item/<string:name>') # get at with localhost/student/<name>. kind of like @app.route(), but we dont need the decorator
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
    