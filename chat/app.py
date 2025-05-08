from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data.get('message')
    bot_reply = f"You said: {user_message}"
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)