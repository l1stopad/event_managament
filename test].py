import requests

url = "http://127.0.0.1:8000/api-token-auth/"
data = {
    "username": "rarka",
    "password": "qweasdzxc"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
