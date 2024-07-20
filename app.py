from flask import Flask, request

app = Flask(__name__)

# Where we are going to store our data?

# List storage
stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }     
]

# This method displays the stores, items inside each store and the name of the store
@app.get("/store")
def get_stores():
    return {"stores": stores}

# This method creates a new storage on store list variable
@app.post("/store")
def create_store():
    request_data = request.get_json() # This line catches the answer of the client
    new_store = {"name": request_data['name'], "items": []} # This line retrieves the variable needed to create a store
    stores.append(new_store) # This line adds the new store to the list
    return new_store, 201 # This line return a HTTP response