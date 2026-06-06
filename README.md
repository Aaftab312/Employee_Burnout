# Employee Burnout Risk Prediction System

## Overview

Employee burnout is a major challenge faced by organizations, affecting productivity, employee satisfaction, and overall workplace performance. This project uses Machine Learning to predict employee burnout risk based on workplace, productivity, and lifestyle-related factors.

The objective is to identify employees who may be at risk of burnout and provide insights that can help organizations take preventive measures.

---

## Problem Statement

Develop a Machine Learning model that predicts employee burnout risk using employee-related data and identifies the factors that contribute most to burnout.

---

## Dataset Information

The dataset contains **1000 employee records** with the following features:

* employee_id
* age
* years_experience
* weekly_work_hours
* meetings_per_week
* emails_sent_per_day
* projects_handled
* remote_days_per_month
* sleep_hours
* stress_level
* exercise_hours_week
* sick_leaves_year
* productivity_score

### Target Variable

* burnout_risk_score

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## Project Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Data Visualization
5. Model Training using Linear Regression
6. Model Evaluation
7. Feature Importance Analysis
8. Scenario Analysis
9. Business Insights and Recommendations

---

## Exploratory Data Analysis

The following analyses were performed:

* Missing Value Analysis
* Statistical Summary
* Correlation Analysis
* Distribution Analysis
* Outlier Detection
* Scatter Plot Analysis

### Visualizations

* Correlation Heatmap
* Histograms
* Box Plots
* Scatter Plots

---

## Model Development

A **Linear Regression** model was used to predict employee burnout risk.

### Data Split

* Training Data: 80%
* Testing Data: 20%

---

## Model Evaluation

### Results

| Metric   | Value  |
| -------- | ------ |
| MAE      | 4.65   |
| MSE      | 34.02  |
| RMSE     | 5.83   |
| R² Score | 0.6147 |

### Interpretation

The model explains approximately **61.47%** of the variation in employee burnout risk and achieves a low prediction error, indicating satisfactory predictive performance.

---

## Key Findings

* Higher stress levels increase burnout risk.
* Long working hours contribute to burnout.
* Employees handling multiple projects are more vulnerable to burnout.
* Adequate sleep reduces burnout risk.
* Regular exercise helps improve employee well-being.
* Higher productivity is associated with lower burnout risk.

---

## Scenario Analysis

### Scenario 1: Reduce Weekly Work Hours by 10%

Result:
Reduction in average burnout risk.

### Scenario 2: Increase Sleep by One Hour Per Day

Result:
Decrease in burnout risk.

### Scenario 3: Increase Exercise by Three Additional Hours Per Week

Result:
Largest reduction in burnout risk among all tested scenarios.

---

## Recommendations

* Monitor employee stress levels regularly.
* Reduce excessive workload and overtime.
* Encourage healthy sleep habits.
* Promote fitness and wellness programs.
* Conduct periodic burnout assessments using predictive analytics.

---

## Future Enhancements

* Implement Random Forest Regression.
* Implement XGBoost Regression.
* Build a Streamlit Web Application.
* Deploy the model on cloud platforms.
* Enable real-time burnout monitoring dashboards.

---

## Conclusion

This project successfully demonstrates the application of Machine Learning in predicting employee burnout risk. The generated insights can help organizations make data-driven decisions to improve employee well-being, productivity, and retention.

---
