import requests

class WebDB:
    def get(self, variable):
        return(requests.get('https://webdb.pythonanywhere.com/get/' + variable).text)
    def create(self, variable, password, value):
        create_payload = {
            "variable": str(variable),
            "password": str(password),
            "value": str(value)
        }
        create_response = requests.post(
            'https://webdb.pythonanywhere.com/create/',
            headers={'Content-Type': 'application/json'},
            json=create_payload
        )
    def delete(self, variable, password, value):
        create_payload = {
            "variable": str(variable),
            "password": str(password),
        }
        create_response = requests.post(
            'https://webdb.pythonanywhere.com/delete/',
            headers={'Content-Type': 'application/json'},
            json=create_payload
        )
    def update(self, variable, password, newvalue):
        create_payload = {
            "variable": str(variable),
            "password": str(password),
        }
        create_response = requests.post(
            'https://webdb.pythonanywhere.com/delete/',
            headers={'Content-Type': 'application/json'},
            json=create_payload
        )
        create_payload = {
            "variable": str(variable),
            "password": str(password),
            "value": str(newvalue)
        }
        create_response = requests.post(
            'https://webdb.pythonanywhere.com/create/',
            headers={'Content-Type': 'application/json'},
            json=create_payload
        )
