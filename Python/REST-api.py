from flask import Flask, jsonify, request
import requests
app = Flask(__name__)
API_ENDPOINT = "https://www.travel-advisory.info/api"
DATA_FILE = "data.json"
def fetch_data():
    response = requests.get(API_ENDPOINT)
    return response.json()
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "code": 200})
@app.route('/diag', methods=['GET'])
def diag():
    data = fetch_data()
    status_code = data.get('status')
    return jsonify({"api_status": {"code": status_code, "status": data}})
@app.route('/convert', methods=['POST'])
def convert():
    country_name = request.json.get('country_name')
    data = fetch_data()
    
    for code, info in data.get('data', {}).items():
        if info.get('name') == country_name:
            return jsonify({"country_code": code, "country_name": country_name})
    
    return jsonify({"error": f"Country not found for {country_name}", "code": 404})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
