# PyNet
### PyNet is Python powered browser & system with a custom domain name system, simple REST API, and a completely open-source frontend AND backend!

#### How To Use Browser
THIS PART IS A WORK IN PROGRESS, PLEASE CHECK BACK LATER!

#### How To Use REST API
Command for opening sites:
```
curl https://pynetapi.pythonanywhere.com/get/example
```
Command for creating sites:
```
curl -X POST https://pynetapi.pythonanywhere.com/create/ \
-H "Content-Type: application/json" \
-d '{"domain": "newdomain", "password": "securepassword123", "code": "ABC123"}'
```
Command for deleting sites:
```
curl -X POST https://pynetapi.pythonanywhere.com/delete/ \
-H "Content-Type: application/json" \
-d '{"domain": "newdomain", "password": "securepassword123"}'
```
