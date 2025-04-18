import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(data_path: str, model_path: str = 'ml/model.pkl'):
    # Load and preprocess data
    df = pd.read_csv(data_path)
    df = encode_features(clean_data(df))
    
    # Prepare features
    X = df[['env_encoded', 'vector_encoded', 'cvss_score']]
    y = df['potential_result']  # From Table 2
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Save artifacts
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    return model.score(X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default='data/cleaned_data.csv')
    parser.add_argument('--output', default='ml/model.pkl')
    args = parser.parse_args()
    
    score = train_model(args.data, args.output)
    print(f"Model accuracy: {score:.2f}")
