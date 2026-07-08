import numpy as np
import pickle
import os
from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "hdi_model.pkl")
model = None

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully")
else:
    print("Warning: No trained model found. Train the model first using ml_model.py")

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]
encoder = LabelEncoder()
encoder.fit(countries)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("indexnew.html", countries=countries,
                               prediction=None, form_data=None)

    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    country = request.form.get("country", "Country_A")
    life_exp = float(request.form.get("life_expectancy"))
    eys = float(request.form.get("expected_years_schooling"))
    mys = float(request.form.get("mean_years_schooling"))
    gni = float(request.form.get("gni_per_capita"))

    country_enc = encoder.transform([country])[0]
    features = np.array([[country_enc, life_exp, eys, mys, gni]])
    prediction = model.predict(features)[0]
    hdi = round(float(prediction), 4)

    return render_template("indexnew.html", countries=countries,
                           prediction=hdi, form_data=request.form)


if __name__ == "__main__":
    app.run(debug=True)
