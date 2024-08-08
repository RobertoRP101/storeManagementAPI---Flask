import uuid
from flask import Flask, request
from .db import stores, items
app = Flask(__name__)

# Where we are going to store our data?

# List storage
# stores = [
#     {
#         "name": "My store",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 15.99
#             }
#         ]
        
#     },
#     {
#         "name": "My store 2",
#         "items": [
#             {
#                 "name": "Sofa",
#                 "price": 39.99
#             }
#         ]
        
#     }        
# ]



# This method displays the stores, items inside each store and the name of the store
@app.get("/store") # This decorator defines the HTTP's method and the route (GET)
def get_stores():
    return {"stores": list(stores.values())}

# This method creates a new storage on store list variable
@app.post("/store") # This decorator defines the HTTP's method and the route (POST)
def create_store():
    store_data = request.get_json() # This line catches the answer of the client
    store_id = uuid.uuid4().hex # This line create a unique universal id which will be assigned to the new store
    store = {**store_data, "id": store_id} # This line unpacks the variable store_data and save it with store_id
    stores[store_id] = store # This line adds the new store to the dictionary
    return store, 201 # This line return a HTTP response

# Ways to retrieve information from the URL
# localhost/store/My store
# localhost/store?name=My store

# localhost/store/My store/item
# @app.post("/store/<string:name>/item") # This decorator defines the HTTP's method and the route (POST) and retrieve the data
# # from the URL after the domain
# def create_item(name): # This signature function receives a paramenter from the URL 
#     request_data = request.get_json() # This line catches the answer of the client
#     for store in stores:
#         if store['name'] == name:  
#             new_item = {"name": request_data['name'], "price": request_data['price']} 
#             store['items'].append(new_item)
#             return new_item, 201
#     return {'message': 'Store not found'}, 404 # This line returns a known error since there is not a match from the
# # name of a existed store            


@app.post("/item") # This decorator defines the HTTP's method and the route (POST) and retrieve the data
# from the URL after the domain
def create_item(): 
    item_data = request.get_json() # This line catches the answer of the client (item and id store)
    if item_data["store_id"] not in stores: # This line looks for a key to check out if it exists
        return {"message": "Store not found"}, 404 
    item_id = uuid.uuid4().hex # This line create a unique universal id which will be assigned to the new store
    item = {**item_data, "id": item_id} # This line unpacks the variable store_data and save it with store_id
    stores[item_id] = item # This line adds the new store to the dictionary
    return item, 201 # This line returns a known error since there is not a match from the
# name of a existed store       
            
            
@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}
            
# This method returns a store and its items
# @app.get("/store/<string:name>")
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return store
#     return {'message': 'Store not found'}, 404

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {'message': 'Store not found'}, 404

# This method gets a specific store and returns its items
@app.get("/store/<string:name>")
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return {"items": store['items']}
    return {'message': 'Store not found'}, 404

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {'message': 'Item not found'}, 400
    
