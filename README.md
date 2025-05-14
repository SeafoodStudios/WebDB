# WebDB
WebDB is free storage method with a simple REST API and a completely open-source frontend AND backend! It is suitable for small developer projects so that you don't need to build your own server. It also serves as a temporary, working placeholder if you still want to build your own backend.
Its features are:
- Free REST API
- No API Key
- Open Source
- Self Hostable
- Key Value
- Secure With Passwords
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
print(response.json())
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
print(create_response.json())
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
print(delete_response.json())
```
You can also use the wrapper for this API. It is located in the "pywrapper" folder in the "src" folder in the code.
## How To Use REST API with Javascript
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
## How to Self Host
To self host, follow the instructions in the repository's build folder. Self hosting can be helpful for a more isolated server, or custom code.
## Thanks!
Please remember to use this service gently, and to not try to abuse it. Please don't overload or inject the server. But you may reasonably make as many variables as you like! Please remember that if you have the variable name, you can get the variable's value, and it is not password protected. If you liked this service, please keep using it!
