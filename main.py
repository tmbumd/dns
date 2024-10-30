from flask import Flask, request, jsonify

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return 'Welcome to the server!'


# Endpoint to receive commands from the client
@app.route('/command', methods=['POST'])
def command():
    command = request.json.get('command')
    # Process the command here (e.g., store it, log it, or prepare it to be sent to clients)
    return jsonify({"status": "success", "command": command})

# Endpoint to receive data from the client
@app.route('/report', methods=['POST'])
def report():
    data = request.json.get('data')
    # Handle the reported data here (e.g., log it or process it)
    return jsonify({"status": "received", "data": data})

if __name__ == '__main__':
    app.run(port=5000)
