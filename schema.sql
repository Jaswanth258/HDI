-- Loan Approval Prediction System - Database Schema
-- Based on ER Diagram (HDI-focused entities)

CREATE TABLE "User" (
    user_id     SERIAL PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    email       VARCHAR(255) NOT NULL UNIQUE,
    role        VARCHAR(50)  NOT NULL,
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Country" (
    country_id   SERIAL PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL,
    country_code VARCHAR(10)  NOT NULL UNIQUE,
    region       VARCHAR(100)
);

CREATE TABLE "Dataset" (
    dataset_id   SERIAL PRIMARY KEY,
    dataset_name VARCHAR(255) NOT NULL,
    source       VARCHAR(255),
    record_count INTEGER,
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "ML Model" (
    model_id     SERIAL PRIMARY KEY,
    dataset_id   INTEGER NOT NULL REFERENCES "Dataset"(dataset_id),
    model_name   VARCHAR(255) NOT NULL,
    model_type   VARCHAR(100),
    accuracy     DECIMAL(5,4),
    trained_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "HDI Input Data" (
    input_id                 SERIAL PRIMARY KEY,
    user_id                  INTEGER      NOT NULL REFERENCES "User"(user_id),
    country_id               INTEGER      NOT NULL REFERENCES "Country"(country_id),
    year                     INTEGER      NOT NULL,
    life_expectancy          DECIMAL(5,2),
    expected_years_schooling DECIMAL(4,2),
    mean_years_schooling     DECIMAL(4,2),
    gni_per_capita           DECIMAL(10,2),
    submitted_at             TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "HDI Prediction" (
    prediction_id      SERIAL PRIMARY KEY,
    input_id           INTEGER       NOT NULL UNIQUE REFERENCES "HDI Input Data"(input_id),
    model_id           INTEGER       NOT NULL REFERENCES "ML Model"(model_id),
    predicted_hdi      DECIMAL(4,3),
    predicted_category VARCHAR(50),
    confidence_score   DECIMAL(5,4),
    predicted_at       TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Visualization Report" (
    report_id     SERIAL PRIMARY KEY,
    prediction_id INTEGER   NOT NULL REFERENCES "HDI Prediction"(prediction_id),
    report_type   VARCHAR(100),
    report_data   TEXT,
    generated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE "Session" (
    session_id    SERIAL PRIMARY KEY,
    user_id       INTEGER      NOT NULL REFERENCES "User"(user_id),
    session_token VARCHAR(255) NOT NULL UNIQUE,
    started_at    TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    ended_at      TIMESTAMP
);

-- Indexes for foreign keys and frequent queries
CREATE INDEX idx_hdi_input_user    ON "HDI Input Data"(user_id);
CREATE INDEX idx_hdi_input_country ON "HDI Input Data"(country_id);
CREATE INDEX idx_hdi_prediction_model ON "HDI Prediction"(model_id);
CREATE INDEX idx_report_prediction ON "Visualization Report"(prediction_id);
CREATE INDEX idx_ml_model_dataset  ON "ML Model"(dataset_id);
CREATE INDEX idx_session_user      ON "Session"(user_id);
