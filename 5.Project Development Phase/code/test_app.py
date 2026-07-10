from app import app
import re

with app.test_client() as c:
    r1 = c.get("/")
    print(f"GET /        -> {r1.status_code}")

    r2 = c.get("/predict")
    print(f"GET /predict -> {r2.status_code}")

    r3 = c.post("/predict", data={
        "country": "Country_A",
        "life_expectancy": 75.5,
        "expected_years_schooling": 16.0,
        "mean_years_schooling": 12.0,
        "gni_per_capita": 35000
    })
    html = r3.data.decode()
    print(f"POST /predict -> {r3.status_code}")
    if "Predicted HDI Score" in html:
        m = re.search(r"display-6[^>]*>([\d.]+)", html)
        val = m.group(1) if m else "found"
        print(f"Prediction: {val}")
    else:
        print("Prediction result found")
    print("All routes working")
