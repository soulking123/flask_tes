import requests
from flask import jsonify

inputs = {
        "gender": "Men",
        "usage": "Casual",
        "baseColour": "Blue"
    }

resp = requests.post("http://localhost:5000/", files={"id": "0"})

print(resp)