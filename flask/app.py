from flask import Flask
from  flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "12345697hbhbh"

app.config['MONGO_URI'] = "mongodb://localhost:27017/crud"

mongo = PyMongo(app)
@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _pwd = _json['pwd']

    if _name and _email and _pwd and request.method == 'POST':
        _hashed_password = generate_password_hash(_pwd)

        id = mongo.db.user.insert({"name":_name, "email":_email, 'pwd':_hashed_password})
        resp = jsonify("User adeed")
        resp.status_code = 200
        return resp

    else:
        return not_found()

app.errorhandler(404)
def not_found():
    message = {
        "status":"404",
        "message": "not found"
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)

