# Predicting Human Development Index (HDI) Using Machine Learning

An end-to-end Machine Learning web application that predicts Human Development Index scores using Linear Regression and classifies countries into UNDP-standard development tiers (Very High, High, Medium, Low) with contextual insights and policy recommendations.

## 🌟 Key Features

- **ML-Powered Prediction**: Trained Linear Regression model predicting HDI scores from five key development indicators with R² = 0.8834
- **UNDP Tier Classification**: Automatic classification into Very High (≥0.800), High (≥0.700), Medium (≥0.550), and Low (<0.550) development tiers
- **Contextual Insights**: Scenario-based recommendations tailored to each development tier
- **Premium Dark UI**: Glassmorphism design with animated backgrounds, tier-specific color coding, and HDI gauge visualization
- **Interactive Prediction Form**: Validated input fields with real-time HDI score prediction
- **Data Visualizations**: HDI distribution plots, correlation heatmaps, and actual vs. predicted charts

## 📂 Project Structure

```
HumanDevelopmentIndex/
│
├── 1.Brainstorming & Ideation/       # Empathy Map, Problem Statements, Prioritization
├── 2.Requirement Analysis/            # Customer Journey, Data Flow, Requirements, Tech Stack
├── 3.Project Design Phase/            # Architecture, Problem-Solution Fit, Proposed Solution
├── 4.Project Planning Phase/          # Sprint planning and project timeline
│
├── 5.Project Development Phase/       # Project Development Phase
│   ├── Code-Layout, Readability and Reusability.md  # System details doc
│   ├── Coding & Solution.md                         # Architecture doc
│   ├── No. of Functional Features Included in the Solution.md  # Feature checklist
│   └── code/                          # Application source directory
│       ├── app.py                     # Flask backend with prediction API & tier classification
│       ├── ml_model.py                # ML pipeline: training, evaluation & model serialization
│       ├── data_preprocessing.py      # Data loading, cleaning, encoding & splitting
│       ├── visualization.py           # HDI distribution & correlation visualizations
│       ├── eda_visualizations.py      # Exploratory data analysis
│       ├── feature_selection.py       # Feature importance analysis
│       ├── requirements.txt           # Python dependencies
│       ├── test_app.py                # Unit tests
│       │
│       ├── data/
│       │   └── hdi_data.csv           # Training dataset (200 records, 5 countries)
│       │
│       ├── models/
│       │   ├── hdi_model.pkl          # Trained Linear Regression model
│       │   └── encoder.pkl            # Trained LabelEncoder
│       │
│       ├── static/
│       │   └── style.css              # Premium dark-mode design system
│       │
│       └── templates/
│           ├── home.html              # Landing page with HDI dimension overview
│           ├── indexnew.html          # Prediction form with tier results
│           └── index.html             # Alternative prediction page
│
├── 6.Project Testing/                 # Functional, Performance & Acceptance testing
├── 7.Project Documentation/           # Full documentation & executable instructions
└── 8.Project Demonstration/           # Demo scenarios & future scalability
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **RMSE** | 0.0361 |
| **R² Score** | 0.8834 |
| **Training Samples** | 160 |
| **Test Samples** | 40 |

## 💻 Tech Stack

- **Core**: Python 3.12, Flask 3.1.3 (WSGI Web Framework)
- **Machine Learning**: Scikit-learn 1.9.0 (Linear Regression), NumPy, Pandas
- **Visualization**: Matplotlib 3.11.0, Seaborn 0.13.2
- **Frontend**: HTML5, CSS3 (Glassmorphism Dark Mode), Jinja2, Google Fonts (Inter)
- **IDE**: PyCharm

## 🚀 Getting Started

### 1. Clone & Setup
```bash
git clone https://github.com/BeldhariSwapna/HumanDevelopmentIndex.git
cd "HumanDevelopmentIndex/5.Project Development Phase/code"
python -m venv venv
.\venv\Scripts\Activate          # Windows
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python ml_model.py
```

### 3. Run the Application
```bash
python app.py
```

### 4. Open in Browser
Navigate to **http://127.0.0.1:5000**

## 🎯 Use Case Scenarios

| Scenario | Input Profile | Predicted HDI | Tier |
|----------|--------------|---------------|------|
| Very High Development | LE=82, EYS=16, MYS=13, GNI=$55K | 1.0 | 🟢 Very High |
| Developing Economy | LE=62, EYS=10, MYS=6, GNI=$8K | ~0.70 | 🔵 High |
| Low Development | LE=52, EYS=5, MYS=3, GNI=$1.5K | 0.5408 | 🔴 Low |
