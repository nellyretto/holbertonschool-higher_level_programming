from flask import request, Flask, jsonify

app = Flask(__name__)
users = users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    return jsonify(users)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return "Usern not found", 404


@app.route("/add_user", methods=['POST'])
def add_user():
    user_data = request.get_json()
    username = user_data.get('username')
    if username in users:
        return "User already exists", 400
    users[username] = user_data
    return jsonify(user_data)


if __name__ == "__main__":
    app.run(port=5000)
