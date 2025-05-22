# WebDB
WebDB is free storage method with a simple REST API and a completely open-source frontend AND backend! It is suitable for small developer projects so that you don't need to build your own server. It also serves as a temporary, working placeholder if you still want to build your own backend.

<img src="https://raw.githubusercontent.com/SeafoodStudios/WebDB/refs/heads/main/static/logo.png" height="200">

Its features are:
- Free REST API
- No API Key
- Open Source
- Self Hostable
- Key Value
- Secure With Passwords
- Limit Of 1000 Characters Per Variable
- 100 Requests Per Minute
- If you need more features, please email <contact@seafoodstudios.com>.
## How To Use REST API with Bash
Code for getting variables:
```
curl https://webdb.pythonanywhere.com/get/example
```
Code for creating variables:
```
curl -X POST https://webdb.pythonanywhere.com/create/ \
-H "Content-Type: application/json" \
-d '{"variable": "example", "password": "securepassword123", "value": "ABC123"}'
```
Code for deleting variables:
```
curl -X POST https://webdb.pythonanywhere.com/delete/ \
-H "Content-Type: application/json" \
-d '{"variable": "example", "password": "securepassword123"}'
```
## How To Use REST API with Python
Code for getting variables:
```
import requests
response = requests.get('https://webdb.pythonanywhere.com/get/example')
print(response.text)
```
Code for creating variables:
```
import requests
create_payload = {
    "variable": "example",
    "password": "securepassword123",
    "value": "ABC123"
}
create_response = requests.post(
    'https://webdb.pythonanywhere.com/create/',
    headers={'Content-Type': 'application/json'},
    json=create_payload
)
print(create_response.text)
```
Code for deleting variables:
```
import requests
delete_payload = {
    "variable": "example",
    "password": "securepassword123"
}
delete_response = requests.post(
    'https://webdb.pythonanywhere.com/delete/',
    headers={'Content-Type': 'application/json'},
    json=delete_payload
)
print(delete_response.text)
```
You can also use the wrapper for this API. It is located in the "pywrapper" folder in the "src" folder in the code.
## How To Use REST API with Javascript
*Please note that the Javascript code was generated using ChatGPT, because I have not learned it yet.*

Code for getting variables:
```
fetch('https://webdb.pythonanywhere.com/get/example')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
```
Code for creating variables:
```
const createVariableData = {
  variable: "example",
  password: "securepassword123",
  value: "ABC123"
};

fetch('https://webdb.pythonanywhere.com/create/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(createVariableData)
})
  .then(response => response.json())
  .then(data => console.log('Variable created:', data))
  .catch(error => console.error('Error:', error));
```
Code for deleting variables:
```
const deleteVariableData = {
  variable: "example",
  password: "securepassword123"
};

fetch('https://webdb.pythonanywhere.com/delete/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(deleteVariableData)
})
  .then(response => response.json())
  .then(data => console.log('Variable deleted:', data))
  .catch(error => console.error('Error:', error));
```
## How to use the REST API with Scratch Modifications
Using Scratch modifications to save data permanently on the cloud is hard. This is why I created a wrapper for WebDB called BlockDB so that it can accessible directly with GET commands. Please make sure to not use your real passwords using BlockDB, because it uses GET commands, and they can be logged by browsers.

Download it here:

[Scratch Modification WebDB Wrapper](https://raw.githubusercontent.com/SeafoodStudios/WebDB/refs/heads/main/src/scratchwrapper/BlockDB.sb3)

[mBlock WebDB Wrapper](https://raw.githubusercontent.com/SeafoodStudios/WebDB/refs/heads/main/src/scratchwrapper/mBlockDB.mblock)

## How to Self Host
To self host, follow the instructions in the repository's build folder. Self hosting can be helpful for a more isolated server with more variables, or custom code. The current code in the build folder will only create a server locally, so if you want it publically, you have to use a WSGI server.
## Attribution
Thanks to PythonAnywhere for the free full Python enviroment that hosts my Flask app and thanks to TinyDB, the library I use for simple JSON storage.
## A Few Notes
Please remember to use this service gently, and to not try to abuse it. Please don't overload or inject the server. But you may reasonably make as many variables as you like! Please remember that if you have the variable name, you can get the variable's value, and it is not password protected. To update a variable, delete the variable and create it again.
## Thanks!
Alright, that's it. If you liked this service, please keep using it!
> SeafoodStudios
