import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB
import os
import joblib

INPUT_FILE = "data/features_dataset.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "ensemble_model.pkl")

def train_and_evaluate(df):
    """Trains, evaluates, and saves an ensemble of classifiers."""
    
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    # --- Data Preparation ---
    df = df.drop(['Date', 'HomeTeam', 'AwayTeam'], axis=1)
    
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop('FTR', axis=1)
    y = df['FTR']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # --- Baseline Models ---
    clf1 = LogisticRegression(max_iter=1000, random_state=42)
    clf2 = RandomForestClassifier(random_state=42)
    clf3 = GaussianNB()
    clf4 = DecisionTreeClassifier(random_state=42)

    print("--- Training and Evaluating Baseline Models ---")
    for clf, name in [(clf1, "Logistic Regression"), (clf2, "Random Forest"), (clf3, "Naive Bayes"), (clf4, "Decision Tree")]:
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        print(f"  - {name} Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    
    # --- Ensemble Model ---
    print("\n--- Training Ensemble Model ---")
    # A simple majority-vote ensemble
    eclf1 = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3), ('dt', clf4)], voting='hard')
    eclf1 = eclf1.fit(X_train, y_train)
    y_pred_ensemble = eclf1.predict(X_test)
    
    ensemble_accuracy = accuracy_score(y_test, y_pred_ensemble)
    print(f"  - Ensemble Accuracy: {ensemble_accuracy:.4f}")
    
    # --- Save the final model ---
    print(f"\nSaving final ensemble model to {MODEL_PATH}...")
    joblib.dump(eclf1, MODEL_PATH)
    print("Model saved.")

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