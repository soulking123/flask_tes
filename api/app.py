from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    data = request.get_json()
    # return jsonify(data) 

    # return "OK"
    prediction = predict_pipeline(data)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)