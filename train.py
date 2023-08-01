import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import os

INPUT_FILE = "data/features_dataset.csv"

def train_and_evaluate(df):
    """Trains and evaluates a suite of baseline classifiers."""
    
    # Prepare the data for modeling
    # Drop non-numeric/unnecessary columns
    df = df.drop(['Date', 'HomeTeam', 'AwayTeam'], axis=1)
    
    # Label encode categorical features like form
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = LabelEncoder().fit_transform(df[col])

    # Define features (X) and target (y)
    X = df.drop('FTR', axis=1)
    y = df['FTR']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Define models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "SVM": SVC(),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(),
        "Naive Bayes": GaussianNB()
    }
    
    print("--- Training Baseline Models ---")
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"  - Accuracy: {accuracy:.4f}\n")

def main():
    """Main function to run the training pipeline."""
    if not os.path.exists(INPUT_FILE):
        print(f"Input file not found: {INPUT_FILE}. Please run build_features.py first.")
        return
    
    print(f"Loading features data from {INPUT_FILE}...")
    df = pd.read_csv(INPUT_FILE)
    
    train_and_evaluate(df)

if __name__ == "__main__":
    main()
