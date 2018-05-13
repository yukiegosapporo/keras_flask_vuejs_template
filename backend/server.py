from ml import *
from flask import jsonify, request, Flask, render_template
from flask_cors import CORS
import pprint
import requests

pp = pprint.PrettyPrinter()

app = Flask(__name__,
            static_folder = "../dist/static",
            template_folder = "../dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route("/recipes", methods=['POST'])
def recipes():    
    try:
        imagefile = request.files['file']
        objects = image2obj(imagefile, topx=1)
        return jsonify(objects)
    except ValueError:
        raise 

if __name__ == "__main__":
    app.run(debug=True)
    # httpie post example
    # http --form POST localhost:5000 imagefile@/Users/yuki/Downloads/802f7cdc166aa144a295d0315ca6be7a_4066cd9d-8ef6-464b-a8f1-1210d63a37ec.png
