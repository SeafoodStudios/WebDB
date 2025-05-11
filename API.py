from tinydb import TinyDB, Query
from flask import Flask, request
import bcrypt
import base64

db = TinyDB('db.json')
User = Query()
app = Flask(__name__)

@app.route('/get/<path:subpath>', methods=['GET'])
def get(subpath):
    data = db.search(User.domain == str(subpath))
    if not data:
        return "ERROR: Domain does not exist."
    else:
        return str(data[0]['code'])

@app.route('/create/', methods=['POST'])
def create():
    data = request.get_json()

    domain = data.get('domain')
    password = data.get('password').encode('utf-8')
    hashedpassword = bcrypt.hashpw(password, bcrypt.gensalt())
    code = data.get('code')

    if db.search(User.domain == str(domain)):
        status = "ERROR: Domain taken."
    else:
        db.insert({'domain': str(domain), 'password': base64.b64encode(hashedpassword).decode('utf-8'), 'code': str(code)})
        status = "SUCCESS: Domain created."

    return str(status)

@app.route('/delete/', methods=['POST'])
def delete():
    data = request.get_json()

    domain = data.get('domain')
    password = data.get('password')
    user_data = db.search(User.domain == domain)

    stored_hash = base64.b64decode(user_data[0]['password'])
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        db.remove(User.domain == domain)
        status = "SUCCESS: Website deleted."
    else:
        status = "ERROR: Incorrect password."

    return str(status)
