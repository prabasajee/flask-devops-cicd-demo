from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, DevOps CI/CD Pipeline!'


@app.route('/health')
def health():
    return jsonify(status='ok', message='App is healthy'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
