from flask import Flask, request, jsonify
from ml.predict import predict
import joblib

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.json
    try:
        result = predict(data)
        return jsonify({
            'cve_id': data.get('cve_id'),
            'predicted_impact': result,
            'confidence': None  # Add probability if needed
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
