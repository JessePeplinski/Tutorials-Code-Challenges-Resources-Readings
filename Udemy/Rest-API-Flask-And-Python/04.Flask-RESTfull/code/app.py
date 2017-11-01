from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) # allows us to add resources to the API

items = []
# inherits from resource
class Item(Resource): 
    def get(self, name):
        return {'student': name}

api.add_resource(Item, '/item/<string:name>') # get at with localhost/student/<name>. kind of like @app.route(), but we dont need the decorator

app.run(port=5000)
    