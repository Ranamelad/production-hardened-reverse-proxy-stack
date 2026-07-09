from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "The server is running! Go to /api/data to see the output."


@app.route('/api/data')
def get_data():
    return jsonify({"status": "success", "message": "Hello from the Hardened Python Backend"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)