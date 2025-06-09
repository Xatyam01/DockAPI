from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Flask API is it"})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy one"})

@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({"result": "42"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
