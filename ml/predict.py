import argparse
import pandas as pd
import joblib

def predict(input_data: dict, model_path: str = 'ml/model.pkl'):
    """Make predictions using trained model"""
    # Load artifacts
    model = joblib.load(model_path)
    encoders = joblib.load('ml/encoders.pkl')
    
    # Preprocess input
    input_df = pd.DataFrame([input_data])
    input_df['env_encoded'] = input_df['environment'].map(encoders['env'])
    input_df['vector_encoded'] = input_df['attack_vector'].map(encoders['vector'])
    
    # Predict
    return model.predict(input_df[['env_encoded', 'vector_encoded', 'cvss_score']])[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--environment', required=True)
    parser.add_argument('--attack_vector', required=True)
    parser.add_argument('--cvss_score', type=float, required=True)
    args = parser.parse_args()
    
    prediction = predict(vars(args))
    print(f"Predicted impact: {prediction}")
