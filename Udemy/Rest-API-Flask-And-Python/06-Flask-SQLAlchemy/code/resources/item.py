import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


# inherits from resource
class Item(Resource): 

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank") # Look into JSON payload
     
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        return {'message': 'Item now found'}, 404        

    def post(self,name):
        # IF (we've found an item and its not null, it matches the name)
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # error checking for bad request

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {"message": "error occured inserting the item"}, 500 # server error

        return item.json(), 201 # created

    def delete(self,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return {'message': 'Item Deleted'}
    
    def put(self,name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name) 
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message" : "error occured inserting the item"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message" : "error occured updating the item"}, 500
        return updated_item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)

        for row in result:
            items.append({
                'name': row[0],
                'price': row[1]
            })

        connection.close()

        return {'items': items}