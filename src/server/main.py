from tinydb import TinyDB, Query
from markupsafe import escape
from flask import Flask, Response, request
import bcrypt
import base64

db = TinyDB('db.json')
User = Query()
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the REST API for WebDB. Go here for the documentation: https://github.com/SeafoodStudios/WebDB'

@app.route('/get/<path:subpath>', methods=['GET'])
def get(subpath):
    data = db.search(User.variable == str(subpath))
    if not data:
        return "ERROR: Variable does not exist."
    else:
        return Response(escape(data[0]['value']), mimetype='text/html')

@app.route('/create/', methods=['POST'])
def create():
    data = request.get_json()

    variable = data.get('variable')
    password = data.get('password').encode('utf-8')
    hashedpassword = bcrypt.hashpw(password, bcrypt.gensalt())
    value = data.get('value')

    if all([variable, password, value]):
        if len(variable) < 1001 and len(password) < 1001 and len(value) < 1001:
            if db.search(User.variable == str(variable)):
                status = "ERROR: Variable taken."
            else:
                db.insert({'variable': str(variable), 'password': base64.b64encode(hashedpassword).decode('utf-8'), 'value': str(value)})
                status = "SUCCESS: Variable created."
        else:
            status = "ERROR: Maximum input length is 200."
    else:
        status = "ERROR: Missing input/s."

    return str(status)

@app.route('/delete/', methods=['POST'])
def delete():
    status = "ERROR: Request in progress."
    data = request.get_json()

    variable = data.get('variable')
    password = data.get('password')
    user_data = db.search(User.variable == variable)
    if user_data and user_data[0].get('password'):
        stored_hash = base64.b64decode(user_data[0]['password'])
    else:
        status = "ERROR: Password empty."
    if not status == "ERROR: Password empty.":
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            db.remove(User.variable == variable)
            status = "SUCCESS: Variable deleted."
        else:
            status = "ERROR: Incorrect password."

    return str(status)
