"""
Training script for Linear Regression on California Housing dataset.
"""
from sklearn.linear_model import LinearRegression
from utils import (
    load_california_housing_data,
    save_model,
    print_model_info
)


def train_model():
    """
    Train Linear Regression model on California Housing dataset.
    
    Returns:
        tuple: (model, X_test, y_test) - Trained model and test data
    """
    print("Loading California Housing dataset...")
    X_train, X_test, y_train, y_test = load_california_housing_data()
    
    print(f"Training data shape: {X_train.shape}")
    print(f"Test data shape: {X_test.shape}")
    
    # Initialize and train the model
    print("\nTraining Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Print model information and performance
    metrics = print_model_info(model, X_test, y_test)
    
    # Save the trained model
    print("\nSaving model...")
    save_model(model, "models/linear_regression_model.joblib")
    print("Model saved successfully!")
    
    return model, X_test, y_test


if __name__ == "__main__":
    train_model() 