# Predicting Human Development Index (HDI) Using Machine Learning

An end-to-end Machine Learning web application that predicts Human Development Index scores using Linear Regression and classifies countries into UNDP-standard development tiers (Very High, High, Medium, Low) with contextual insights and policy recommendations.

---

## 🎥 Live Video Demonstration

Watch our complete team presentation, user interface walkthrough, and scenario simulations:
👉 **[Watch Project Video Demonstration (Google Drive)](https://drive.google.com/file/d/1SGMQ0ISFxUGTr5hJNGJdoDYp_xgMIbGE/view?usp=drivesdk)**

---

## 🌟 Key Features

- **ML-Powered Prediction**: Trained Linear Regression model predicting HDI scores from five key development indicators with R² = 0.8834.
- **Model Info Dashboard**: Transparent analytics page displaying metrics (R², RMSE), formulation weight impacts, and exploratory data plots (correlation heatmap, strip distributions).
- **UNDP Tier Classification**: Automatic classification into Very High (≥0.800), High (≥0.700), Medium (≥0.550), and Low (<0.550) development tiers.
- **Contextual Insights**: Scenario-based recommendations and urgent policy guides tailored to each development tier.
- **Premium Dark UI**: Responsive Glassmorphism design with animated backdrops, tier badges, and live progress gauges.
- **Validation Form**: Client and server-side range validation checks ensuring prediction stability.

---

## 📂 Project Structure

```
HDI/
│
├── 1.Brainstorming & Ideation/       # Empathy Map, Problem Statements, Prioritization (.docx)
├── 2.Requirement Analysis/            # Customer Journey, Data Flow, Tech Stack (.docx)
├── 3.Project Design Phase/            # Architecture, Proposed Solution, Problem-Solution Fit (.docx)
├── 4.Project Planning Phase/          # Sprint planning and project timeline (.docx)
│
├── 5.Project Development Phase/       # System development folder
│   ├── Code-Layout...docx             # Coding standard details
│   ├── Coding & Solution.docx         # Preprocessing & algorithm details
│   ├── No. of Functional Features...  # Features checklist doc
│   └── code/                          # Application source directory
│       ├── app.py                     # Flask backend router & classification engines
│       ├── ml_model.py                # ML pipeline: training, evaluation & model serialization
│       ├── data_preprocessing.py      # Data loading, cleaning, encoding & splitting
│       ├── visualization.py           # HDI distribution & correlation visualizations
│       ├── eda_visualizations.py      # Exploratory data analysis strip plots
│       ├── feature_selection.py       # Feature importance analysis
│       ├── requirements.txt           # Python dependencies
│       ├── test_app.py                # Unit test suite
│       │
│       ├── data/
│       │   └── hdi_data.csv           # Training dataset (200 records)
│       │
│       ├── models/
│       │   ├── hdi_model.pkl          # Serialized Linear Regression model
│       │   └── encoder.pkl            # Serialized LabelEncoder
│       │
│       ├── static/
│       │   ├── style.css              # Premium dark-mode design system stylesheet
│       │   └── images/                # Saved EDA visual plots
│       │
│       └── templates/
│           ├── home.html              # Landing dashboard page
│           ├── indexnew.html          # Dynamic prediction simulator
│           └── model_info.html        # Model statistics & plots dashboard
│
├── 6.Project Testing/                 # Functional, performance & UAT docs (.docx)
├── 7.Project Documentation/           # Final project reports & setup guidelines (.docx)
└── 8.Project Demonstration/           # Presentation plans, demo scripts & future roadmap (.docx)
```

---

## 📊 Model Performance

| Metric | Value | Description |
|--------|-------|-------------|
| **Algorithm** | Linear Regression | Scikit-learn baseline model |
| **R² Score** | 0.8834 | Explains 88.34% of validation variance |
| **RMSE** | 0.0361 | Root Mean Squared Error on test splits |
| **Training Samples** | 160 | 80% split dataset |
| **Test Samples** | 40 | 20% split dataset |

---

## 💻 Tech Stack

- **Core**: Python 3.12, Flask 3.1.3 (WSGI Web Framework)
- **Machine Learning**: Scikit-learn 1.9.0 (Linear Regression), NumPy, Pandas
- **Visualization**: Matplotlib 3.11.0, Seaborn 0.13.2
- **Frontend**: HTML5, CSS3 (Glassmorphism Dark Mode), Jinja2, Google Fonts (Inter)
- **Version Control**: Git & GitHub

---

## 🚀 Getting Started

### 1. Clone & Setup
```bash
git clone https://github.com/Jaswanth258/A-COMPREHENSIVE-MEASURE-OF-WELL-BEING-HUMAN-DEVELOPMENT-INDEX-HDI-PREDICTOR.git
cd "HDI/5.Project Development Phase/code"
python -m venv venv
.\venv\Scripts\Activate          # Windows PowerShell
pip install -r requirements.txt
```

> **Note**: If you run into script execution policy blocks in PowerShell, execute:  
> `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

### 2. Train the Model (Optional)
```bash
python ml_model.py
```
*(Preprocesses the dataset and outputs `hdi_model.pkl` and `encoder.pkl` in the `models/` directory)*

### 3. Run the Application
```bash
python app.py
```

### 4. Open in Browser
Open your browser and navigate to: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🎯 Use Case Scenarios

| Scenario | Input Profile | Predicted HDI | Classification Tier |
|----------|--------------|---------------|---------------------|
| **Very High Development** | LE=82, EYS=16, MYS=13, GNI=$55K | 1.0 | 🟢 Very High |
| **Developing Economy** | LE=62, EYS=10, MYS=6, GNI=$8K | ~0.70 | 🔵 High |
| **Low Development** | LE=52, EYS=5, MYS=3, GNI=$1.5K | 0.5408 | 🔴 Low |
