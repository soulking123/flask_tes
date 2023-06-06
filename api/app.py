from flask import Flask, jsonify, request
from utilities import predict_pipeline

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        file = request.files.get('file')
        return file
        # file = file.decode('utf-8')
        # return file.read()
        if file is None or file.filename == "":
            return jsonify({"error":"no files"})
        return file.read()

    return "OK"
    # data = request.json
    # print(data)
    # prediction = predict_pipeline(data)
    # return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)