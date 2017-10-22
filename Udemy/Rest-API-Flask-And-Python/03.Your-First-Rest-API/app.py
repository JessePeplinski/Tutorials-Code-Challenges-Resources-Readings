from flask import Flask, jsonify, request

app = Flask(__name__) # Gives each file a unique name

# Normally we store all these in database. Will move to DB eventually
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

# POST - server is receiving data
# GET - send data back only

@app.route('/') # 'http://www.google.com/ - homepage
def home():
    return "Hello world!"


# POST /store data: {name:} # create a new store 
@app.route('/store', methods=['POST']) # by default, this is get
def create_store():
    request_data = request.get_json()

    new_store = {
        'name':request_data['name'],
        'items':[]
    }

    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name> # return info one one store
@app.route('/store/<string:name>', methods=['GET']) # <string:name> is flask syntax for localhost:5000/store/some_name
def get_store(name):
    # iterate over stores
    # if store name matches, return it
    # if none match, return an error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'message': 'store not found'})
    

# GET /store # list of all stores
@app.route('/store/', methods=['GET']) 
def get_stores():
    return jsonify({
        'stores': stores
    }) 

# POST /store/<string:name>/item {name:, price: # create item within a specific store
@app.route('/store/<string:name>/item', methods=['POST']) 
def create_item_in_store(name):

    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({
        'message': 'store not found'
    })

# GET store/<string:name>/item # get all items within speciic store
@app.route('/store/<string:name>/item', methods=['GET']) 
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(
                {
                    'items': store['items']
                }
            )
        else:
            return jsonify({'message': 'item not found'})

app.run(port=5000)


