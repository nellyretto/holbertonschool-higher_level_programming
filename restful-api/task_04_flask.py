from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return {"error": "User not found"}, 404
    return user

@app.route("/add_user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if not username:
        return {"error": "Username is required"}, 400
    if username in users:
        return {"error": "User already exists"}, 400
    users[username] = user_data
    return {"message": "User added", "user": user_data}, 201

if __name__ == "__main__":
    app.run(port=5000)