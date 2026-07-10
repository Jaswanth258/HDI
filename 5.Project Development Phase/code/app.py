import numpy as np
import pickle
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "hdi_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "encoder.pkl")
model = None
encoder = None

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully")
else:
    print("Warning: No trained model found. Train the model first using ml_model.py")

if os.path.exists(ENCODER_PATH):
    with open(ENCODER_PATH, "rb") as f:
        encoder = pickle.load(f)
    print("Encoder loaded successfully")
else:
    print("Warning: No encoder found. Train the model first using ml_model.py")

countries = list(encoder.classes_) if encoder else ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]


def classify_hdi(score):
    """Classify HDI score into UNDP tiers."""
    if score >= 0.800:
        return "Very High"
    elif score >= 0.700:
        return "High"
    elif score >= 0.550:
        return "Medium"
    else:
        return "Low"


def get_tier_color(tier):
    """Return CSS color class for each tier."""
    colors = {
        "Very High": "#10b981",
        "High": "#3b82f6",
        "Medium": "#f59e0b",
        "Low": "#ef4444",
    }
    return colors.get(tier, "#6b7280")


def get_hdi_insights(tier, score):
    """Return contextual insights based on HDI tier."""
    insights = {
        "Very High": {
            "title": "Excellent Human Development",
            "description": (
                "This profile indicates very high human development, placing it among "
                "the most developed nations globally. Strong performance across health, "
                "education, and income dimensions contributes to this outstanding score."
            ),
            "recommendations": [
                "Sustain investments in healthcare and education systems",
                "Focus on reducing inequality within high-performing areas",
                "Share development best practices with emerging economies",
            ],
        },
        "High": {
            "title": "Strong Human Development",
            "description": (
                "This profile shows high human development with solid foundations across "
                "key indicators. There are opportunities for targeted improvements in "
                "specific areas to reach the highest tier of development."
            ),
            "recommendations": [
                "Invest in higher education quality and accessibility",
                "Strengthen healthcare infrastructure for broader coverage",
                "Promote inclusive economic growth and income equality",
            ],
        },
        "Medium": {
            "title": "Developing — Gaps Identified",
            "description": (
                "This profile reflects medium human development, indicating a developing "
                "nation with moderate life expectancy, average educational attainment, and "
                "a moderate income level. Improvements in healthcare, education, or income "
                "generation could significantly enhance human development outcomes."
            ),
            "recommendations": [
                "Prioritize primary and secondary education enrollment",
                "Expand access to preventive healthcare and sanitation",
                "Implement policies to increase GNI per capita through job creation",
            ],
        },
        "Low": {
            "title": "Critical — Intervention Required",
            "description": (
                "This profile indicates low human development with significant challenges "
                "across health, education, and living standards. Countries at this level "
                "require urgent policy interventions and international support to improve "
                "outcomes for their populations."
            ),
            "recommendations": [
                "Urgently invest in basic healthcare and disease prevention",
                "Expand access to primary education, especially for girls",
                "Develop infrastructure and create economic opportunities",
                "Seek international development partnerships and aid",
            ],
        },
    }
    return insights.get(tier, insights["Medium"])


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("indexnew.html", countries=countries,
                               prediction=None, form_data=None)

    if model is None or encoder is None:
        return jsonify({"error": "Model or encoder not loaded. Please train the model first."}), 500

    country = request.form.get("country", countries[0])
    life_exp = float(request.form.get("life_expectancy"))
    eys = float(request.form.get("expected_years_schooling"))
    mys = float(request.form.get("mean_years_schooling"))
    gni = float(request.form.get("gni_per_capita"))

    country_enc = encoder.transform([country])[0]
    features = np.array([[country_enc, life_exp, eys, mys, gni]])
    prediction = model.predict(features)[0]
    hdi = round(float(prediction), 4)

    # Clamp between 0 and 1
    hdi = max(0.0, min(1.0, hdi))

    tier = classify_hdi(hdi)
    tier_color = get_tier_color(tier)
    insights = get_hdi_insights(tier, hdi)

    return render_template("indexnew.html", countries=countries,
                           prediction=hdi, tier=tier, tier_color=tier_color,
                           insights=insights, form_data=request.form)


if __name__ == "__main__":
    app.run(debug=True)
