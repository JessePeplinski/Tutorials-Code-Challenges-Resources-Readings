import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


# inherits from resource
class Item(Resource): 

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank") # Look into JSON payload
     
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))

        row = result.fetchone()

        connection.close()

        if row:
            return {'item': {
                'name': row[0],
                'price': row[1]
                }
            }
        return {'message': 'Item now found'}, 404

    
    def post(self,name):
        # IF (we've found an item and its not null, it matches the name)
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # error checking for bad request

        data = Item.parser.parse_args()

        item = {
            'name': name,
            'price': data['price']
        }
        items.append(item)
        return item, 201 # created

    def delete(self,name):
        global items # items var in block is outer items var
        items = list(filter(lambda x: x['name'] != name, items)) # look for items except the one we want to delete
        return {'message': 'Item Deleted'}
    
    def put(self,name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None) 

        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
    

class ItemList(Resource):
    def get(self):
        return {'items': items}