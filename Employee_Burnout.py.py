import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv("employee_burnout_dataset_1000_records.csv")

# Data Preprocessing
df = df.drop("employee_id", axis=1)
X = df.drop("burnout_risk_score", axis=1)
y = df["burnout_risk_score"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)
print("\nModel Trained Successfully")

# Prediction
y_pred = model.predict(X_test)

# Evaluation Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2 Score:", round(r2, 4))

# Feature Importance
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\nRegression Coefficients")
print(coefficients)

# Scenario Analysis
weekly_coef = coefficients.loc[coefficients["Feature"] == "weekly_work_hours", "Coefficient"].values[0]
sleep_coef = coefficients.loc[coefficients["Feature"] == "sleep_hours", "Coefficient"].values[0]
exercise_coef = coefficients.loc[coefficients["Feature"] == "exercise_hours_week", "Coefficient"].values[0]

avg_hours = df["weekly_work_hours"].mean()
reduction = avg_hours * 0.10


# Scenario Analysis
baseline_avg = df["burnout_risk_score"].mean()

scenario1 = reduction * weekly_coef
scenario2 = sleep_coef
scenario3 = exercise_coef * 3

new_avg1 = baseline_avg + scenario1
new_avg2 = baseline_avg + scenario2
new_avg3 = baseline_avg + scenario3

print("\nScenario Analysis")

if scenario1 < 0:
    print(f"1. If employees reduce weekly work hours by 10%, "
          f"the average burnout risk decreases by {abs(scenario1):.2f} points "
          f"(Baseline: {baseline_avg:.2f} → New Average: {new_avg1:.2f}).")
else:
    print(f"1. If employees reduce weekly work hours by 10%, "
          f"the average burnout risk increases by {scenario1:.2f} points "
          f"(Baseline: {baseline_avg:.2f} → New Average: {new_avg1:.2f}).")

if scenario2 < 0:
    print(f"2. If employees sleep one extra hour per day, "
          f"the average burnout risk decreases by {abs(scenario2):.2f} points "
          f"(Baseline: {baseline_avg:.2f} → New Average: {new_avg2:.2f}).")
else:
    print(f"2. If employees sleep one extra hour per day, "
          f"the average burnout risk increases by {scenario2:.2f} points "
          f"(Baseline: {baseline_avg:.2f} → New Average: {new_avg2:.2f}).")

if scenario3 < 0:
    print(f"3. If employees exercise 3 additional hours per week, "
          f"the average burnout risk decreases by {abs(scenario3):.2f} points "
          f"(Baseline: {baseline_avg:.2f} → New Average: {new_avg3:.2f}).")
else:
    print(f"3. If employees exercise 3 additional hours per week, "
          f"the average burnout risk increases by {scenario3:.2f} points "
          f"(Baseline: {baseline_avg:.2f} → New Average: {new_avg3:.2f}).")



print("\nProject Completed Successfully")
