from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret

# Enable CORS so your frontend (Angular) can communicate with the backend
CORS(app)

# Set up SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Root route for testing
@app.route('/')
def index():
    return "Chat backend is running."

# Handle incoming chat messages
@socketio.on('message')
def handle_message(data):
    print(f"Message from {data['sender']} to {data['receiver']}: {data['message']}")
    emit('message', data, broadcast=True)

# Run the app
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
