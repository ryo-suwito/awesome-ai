import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def run_regression_example():
    print("--- Linear Regression Example ---")

    # 1. Generate Synthetic Data
    # y = 2x + 1 + noise
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 4. Predict
    y_pred = model.predict(X_test)

    print(f"Model Intercept (bias): {model.intercept_[0]:.2f} (Expected ~4)")
    print(f"Model Coefficient (weight): {model.coef_[0][0]:.2f} (Expected ~3)")
    print("Predictions for first 5 test items:")
    for i in range(5):
        print(f"Input: {X_test[i][0]:.2f}, Predicted: {y_pred[i][0]:.2f}, Actual: {y_test[i][0]:.2f}")

if __name__ == "__main__":
    run_regression_example()
