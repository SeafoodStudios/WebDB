from flask import Flask
import requests
from itertools import cycle
import base64
import hashlib

app = Flask(__name__)
password = "YOUR_SECRET_PASSWORD"

def xor_encrypt(text: str, password: str) -> str:
    text = "MAGIC|" + text
    xor_bytes = bytes([ord(c) ^ ord(k) for c, k in zip(text, cycle(password))])
    return base64.urlsafe_b64encode(xor_bytes).decode()

def xor_decrypt(encoded: str, password: str) -> str:
    xor_bytes = base64.urlsafe_b64decode(encoded)
    decrypted = ''.join(chr(b ^ ord(k)) for b, k in zip(xor_bytes, cycle(password)))
    if not decrypted.startswith("MAGIC|"):
        raise ValueError("Incorrect password or corrupted data")
    return decrypted[len("MAGIC|"):]

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/create/<path:subpath>', methods=['GET'])
def create(subpath):
    # https://example.com/create/username-password
    if subpath.count("-") == 1:
        inputs = subpath.split("-")
        if inputs[0].isalpha() and inputs[1].isalpha():
            try:
                variable = xor_encrypt(hash_password(inputs[1]) + "-0", password)
                create_payload = {
                "variable": inputs[0],
                "password": password,
                "value": variable
                }
                create_response = requests.post(
                    'https://webdb.pythonanywhere.com/create/',
                    headers={'Content-Type': 'application/json'},
                    json=create_payload
                )
                return "Success: " + str(create_response.text)
            except Exception as e:
                return "Error: Creation Error: " + str(e)
        else:
            return "Error: Non-alphabetical inputs cannot be sent."
    else:
        return "Error: Too many dashes/inputs"
@app.route('/transfer/<path:subpath>', methods=['GET'])
def transfer(subpath):
    # https://example.com/transfer/username-password-amount-receiver
    if subpath.count("-") == 3:
        inputs = subpath.split("-")
        if inputs[0].isalpha() and inputs[1].isalpha() and inputs[3].isalpha():
            if inputs[2].isdigit() and inputs[0] != inputs[3]:
                try:
                    response = requests.get("https://webdb.pythonanywhere.com/get/" + str(inputs[0]))
                    data = xor_decrypt(response.text, password)
                    info = data.split("-")
                    if str(info[0]) == hash_password(inputs[1]):
                        if int(info[1]) >= int(inputs[2]) and int(inputs[2]) > 0:
                            try:
                                delete_payload = {
                                    "variable": inputs[0],
                                    "password": password
                                }
                                delete_response = requests.post(
                                    'https://webdb.pythonanywhere.com/delete/',
                                    headers={'Content-Type': 'application/json'},
                                    json=delete_payload
                                )
                                create_payload = {
                                    "variable": inputs[0],
                                    "password": password,
                                    "value": str(xor_encrypt(hash_password(inputs[1]) + "-" + str(int(info[1])-int(inputs[2])), password))
                                }
                                create_response = requests.post(
                                    'https://webdb.pythonanywhere.com/create/',
                                    headers={'Content-Type': 'application/json'},
                                    json=create_payload
                                )
                                newresponse = requests.get("https://webdb.pythonanywhere.com/get/" + str(inputs[3]))
                                newvalues = xor_decrypt(newresponse.text, password)
                                newvalues = newvalues.split("-")
                                delete_payload = {
                                    "variable": inputs[3],
                                    "password": password
                                }
                                delete_response = requests.post(
                                    'https://webdb.pythonanywhere.com/delete/',
                                    headers={'Content-Type': 'application/json'},
                                    json=delete_payload
                                )
                                create_payload = {
                                    "variable": inputs[3],
                                    "password": password,
                                    "value": str(xor_encrypt(newvalues[0] + "-" + str(int(newvalues[1])+int(inputs[2])), password))
                                }
                                create_response = requests.post(
                                    'https://webdb.pythonanywhere.com/create/',
                                    headers={'Content-Type': 'application/json'},
                                    json=create_payload
                                )
                                return "Success: Transaction complete."
                            except Exception as e:
                                return "Error: Transaction Error: " + str(e)
                        else:
                            return "Error: You don't have enough currency and/or you entered a negative or neutral number!"
                    else:
                        return "Error: Incorrect Input/s"
                except Exception as e:
                    return "Error: Process Error: " + str(e)
            else:
                return "Error: Non-numerical amounts cannot be sent. Also, you cannot send currency to yourself."
        else:
            return "Error: Non-alphabetical inputs cannot be sent."
    else:
        return "Error: Too many dashes/inputs"
@app.route('/balance/<path:subpath>', methods=['GET'])
def balance(subpath):
    # https://example.com/balance/username-password
    try:
        if subpath.count("-") == 1:
            inputs = subpath.split("-")
            if inputs[0].isalpha() and inputs[1].isalpha():
                response = requests.get("https://webdb.pythonanywhere.com/get/" + str(inputs[0]))
                values = xor_decrypt(response.text, password)
                values = values.split("-")
                if str(hash_password(inputs[1])) == values[0]:
                    return str(values[1])
                else:
                    return 'Error: Incorrect input/s'
            else:
                return "Error: Non-alphabetical inputs cannot be sent."
        else:
            return "Error: Too many inputs/dashes."
    except Exception as e:
        return "Error: Fatal Error: " + str(e)
