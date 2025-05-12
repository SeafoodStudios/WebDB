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
