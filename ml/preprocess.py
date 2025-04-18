import pandas as pd
import joblib

ENV_MAPPING = {
    'Windows 10': 0, 'Windows 8': 1, 'Linux Kernel': 2,
    'MySQL': 3, 'Postgres': 4, 'Apache': 5, 'Apple': 6, 'Samba': 7
}

VECTOR_MAPPING = {
    'PHYSICAL': 0, 'NETWORK': 1, 'ADJACENT_NETWORK': 2, 'LOCAL': 3
}

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data as per Algorithm 1 in research paper"""
    clean_df = df[~df['description'].str.contains('RESERVED|REJECT', case=False, na=False)]
    return clean_df.dropna()

def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """Encode categorical features using research paper's Tables 1-2"""
    df['env_encoded'] = df['environment'].map(ENV_MAPPING)
    df['vector_encoded'] = df['attack_vector'].map(VECTOR_MAPPING)
    return df

def save_encoders():
    """Save encoding mappings for inference"""
    joblib.dump({'env': ENV_MAPPING, 'vector': VECTOR_MAPPING}, 'ml/encoders.pkl')
