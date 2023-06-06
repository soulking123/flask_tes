import requests
from flask import jsonify

input1 = {
        "gender": "Men",
        "usage": "Casual",
        "baseColour": "Blue"
    }

resp = requests.post("http://localhost:5000/", json=input1)

print(resp.json())