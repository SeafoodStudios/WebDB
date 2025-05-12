# WebDB
### WebDB is free storage method with a simple REST API and a completely open-source frontend AND backend!

#### How To Use REST API
Command for opening sites:
```
curl https://webdb.pythonanywhere.com/get/example
```
Command for creating sites:
```
curl -X POST https://webdb.pythonanywhere.com/create/ \
-H "Content-Type: application/json" \
-d '{"domain": "newdomain", "password": "securepassword123", "code": "ABC123"}'
```
Command for deleting sites:
```
curl -X POST https://webdb.pythonanywhere.com/delete/ \
-H "Content-Type: application/json" \
-d '{"domain": "newdomain", "password": "securepassword123"}'
```
