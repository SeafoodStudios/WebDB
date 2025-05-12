# WebDB
WebDB is free storage method with a simple REST API and a completely open-source frontend AND backend!
Its features are:
- Free REST API
- No API Key
- Open Source
- Self Hostable
- Key Value
- Secure With Passwords
## How To Use REST API with Bash
Command for getting variables:
```
curl https://webdb.pythonanywhere.com/get/example
```
Command for creating variables:
```
curl -X POST https://webdb.pythonanywhere.com/create/ \
-H "Content-Type: application/json" \
-d '{"variable": "example", "password": "securepassword123", "value": "ABC123"}'
```
Command for deleting variables:
```
curl -X POST https://webdb.pythonanywhere.com/delete/ \
-H "Content-Type: application/json" \
-d '{"variable": "example", "password": "securepassword123"}'
```
## How To Use REST API with Python
Command for getting variables:
```
import requests

response = requests.get('https://webdb.pythonanywhere.com/get/example')
print(response.json())
```
Command for creating variables:
```
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
Command for deleting variables:
```
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
