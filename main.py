from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")

model = pickle.load(open("model/model.pkl", "rb"))
le = pickle.load(open("model/label_encoder.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form["N"]),
            float(request.form["P"]),
            float(request.form["K"]),
            float(request.form["temperature"]),
            float(request.form["humidity"]),
            float(request.form["ph"]),
            float(request.form["rainfall"])
        ]
        final_input = pd.DataFrame([{
                        "N": features[0],
                        "P": features[1],
                        "K": features[2],
                        "temperature": features[3],
                        "humidity": features[4],
                        "ph": features[5],
                        "rainfall": features[6]}])
        pred = model.predict(final_input)[0]
        prediction = le.inverse_transform([pred])[0]
        return render_template("index.html", prediction=prediction)
    except Exception as e:
        print(e)
        return render_template("index.html", prediction="Error in input")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)