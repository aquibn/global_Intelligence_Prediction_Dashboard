import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load dataset with validation"""
    df = pd.read_csv(path)
    required_columns = ['cve_id', 'environment', 'attack_vector', 'cvss_score']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Missing required columns in dataset")
    return df
