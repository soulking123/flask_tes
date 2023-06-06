from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def index():
    data = request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)