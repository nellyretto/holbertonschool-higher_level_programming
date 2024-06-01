from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(users)

@app.route('/status', methods=['GET'])
def status():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    if 'username' in user_data and 'name' in user_data and 'age' in user_data and 'city' in user_data:
        username = user_data['username']
        users[username] = user_data
        return jsonify(user_data), 201
    else:
        return "Invalid user data", 400

if __name__ == "__main__":
    app.run(debug=True)
