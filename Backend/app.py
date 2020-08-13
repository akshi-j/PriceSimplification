from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import pyrebase

config = {
    "apiKey": "AIzaSyA0t_1M9E5IcBO3-9xxHw7VCZqX6uHm_k8",
    "authDomain": "price-by-sku.firebaseapp.com",
    "databaseURL": "https://price-by-sku.firebaseio.com",
    "projectId": "price-by-sku",
    "storageBucket": "price-by-sku.appspot.com",
    "messagingSenderId": "1005343750508",
    "appId": "1:1005343750508:web:be57ca523b0da0db26db49",
    "measurementId": "G-493J25Q82W"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("Products").push({"sku": "50"})
# db.child("Products").child("50").update({"Price" : "100"})
# db.child("Products").child("Product1").update({"LastUpdated" : "01/01/01"})
# db.child("Products").child("Product1").update({"Price" : "100"})
# db.child("Products").child("Product1").push({"Price": "100"})
# db.child("Products").remove()
# db.child("Products").child("150").update({"Price" : "200"})
#db.child("Products").child("50").update({"LastUpdated" : "02/02/02"})

# print (product.val())
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/product/<sku>")
@cross_origin()
def hello(sku: str):
    product = db.child("Products").child(sku).get()
    return product.val()


if __name__ == '__main__':
    app.run(debug=True)
