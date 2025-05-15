from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the REST API for BlockDB. This is an API wrapper that makes WebDB available to Scratch modifications. Go here for the documentation: https://github.com/SeafoodStudios/WebDB'

@app.route('/get/<path:subpath>', methods=['GET'])
def get(subpath):
    parameters = subpath.split("/")
    data = requests.get("https://webdb.pythonanywhere.com/get/" + str(parameters[0]))
    return str(data.text)

@app.route('/create/<path:subpath>', methods=['GET'])
def create(subpath):
    parameters = subpath.split("/")

    create_payload = {
        "variable": str(parameters[0]),
        "password": str(parameters[1]),
        "value": str(parameters[2])
    }
    create_response = requests.post(
        'https://webdb.pythonanywhere.com/create/',
        headers={'Content-Type': 'application/json'},
        json=create_payload
    )
    return "Creation Attempted."

@app.route('/delete/<path:subpath>', methods=['GET'])
def delete(subpath):
    parameters = subpath.split("/")
    delete_payload = {
        "variable": str(parameters[0]),
        "password": str(parameters[1])
    }
    delete_response = requests.post(
        'https://webdb.pythonanywhere.com/delete/',
        headers={'Content-Type': 'application/json'},
        json=delete_payload
    )
    return "Deletion Attempted."
