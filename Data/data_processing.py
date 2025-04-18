# data_processing.py
import pandas as pd
import nvdlib
from datetime import datetime

# Configuration from research paper Tables 1-2
ENV_MAPPING = {
    'Windows 10': 0,
    'Windows 8': 1,
    'Linux Kernel': 2,
    'MySQL': 3,
    'Postgres': 4,
    'Apache': 5,
    'Apple': 6,
    'Samba': 7
}

ATTACK_VECTOR_MAPPING = {
    'PHYSICAL': 0,
    'NETWORK': 1,
    'ADJACENT_NETWORK': 2,
    'LOCAL': 3
}

def fetch_nist_data(years: list):
    """Fetch and preprocess NIST data as per Algorithm 1"""
    all_cves = []
    
    for year in years:
        results = nvdlib.searchCVE(pubStartYear=year, pubEndYear=year)
        
        for cve in results:
            entry = {
                'cve_id': cve.id,
                'description': cve.descriptions[0].value if cve.descriptions else '',
                'cvss_score': cve.v3score or cve.v2score,
                'attack_vector': cve.v3vector.split('/')[1] if cve.v3vector else '',
                'environment': _extract_env(cve.configurations),
                'inputs': _extract_inputs(cve.descriptions)
            }
            all_cves.append(entry)
    
    df = pd.DataFrame(all_cves)
    return _clean_data(df)

def _clean_data(df: pd.DataFrame):
    """Clean data as per Algorithm 1 in research paper"""
    # Remove reserved/rejected entries
    clean_df = df[~df['description'].str.contains('RESERVED|REJECT', case=False, na=False)]
    
    # Feature encoding (Tables 1-2)
    clean_df['env_encoded'] = clean_df['environment'].map(ENV_MAPPING)
    clean_df['vector_encoded'] = clean_df['attack_vector'].map(ATTACK_VECTOR_MAPPING)
    
    return clean_df.dropna()

def generate_output(clean_df: pd.DataFrame):
    """Generate Output.xlsx with vulnerability analysis results"""
    # Create formatted output as per research paper Fig.6
    output_df = clean_df.copy()
    
    # Add additional analysis columns
    output_df['Potential_Results'] = output_df['description'].apply(_classify_results)
    output_df['Attack_Count'] = output_df.groupby('env_encoded')['env_encoded'].transform('count')
    
    # Save to Excel with formatting
    with pd.ExcelWriter('data/Output.xlsx') as writer:
        output_df[[
            'cve_id', 
            'env_encoded',
            'vector_encoded',
            'inputs',
            'Potential_Results',
            'Attack_Count'
        ]].to_excel(writer, sheet_name='Vulnerability Analysis', index=False)

# Helper functions
def _extract_env(configurations):
    """Extract environment from CVE configurations"""
    # Implementation from research paper's environment extraction logic
    pass

def _extract_inputs(descriptions):
    """Extract prerequisite inputs from descriptions"""
    # Implementation from research paper's input extraction logic  
    pass

def _classify_results(desc: str):
    """Classify potential results based on description"""
    results = []
    if 'credential' in desc.lower():
        results.append('Credential Acquisition')
    if 'privilege' in desc.lower():
        results.append('Privilege Escalation')
    if 'remote' in desc.lower():
        results.append('Remote Access')
    return ', '.join(results)

if __name__ == "__main__":
    # Generate cleaned dataset
    years = range(1999, 2025)
    cleaned_df = fetch_nist_data(years)
    cleaned_df.to_csv('data/cleaned_data.csv', index=False)
    
    # Generate analysis output
    generate_output(cleaned_df)
