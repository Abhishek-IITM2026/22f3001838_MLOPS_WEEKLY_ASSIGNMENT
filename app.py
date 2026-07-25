from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model/model.joblib")


@app.route("/")
def home():
    return "IRIS Prediction API"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["features"]

    prediction = model.predict([data])

    return jsonify(
        {
            "prediction": str(prediction[0])
            }
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
