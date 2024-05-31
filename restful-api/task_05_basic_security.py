from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if not username or not password:
        return {"error": "Missing username or password"}, 400
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return {"error": "Invalid username or password"}, 401
    token = create_access_token(identity=username)
    return {"access_token": token}, 200

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_role = users.get(current_user, {}).get('role')
    if user_role != 'admin':
        return {"error": "Admin access required"}, 403
    return "Admin Access: Granted"

if __name__ == "__main__":
    app.run(debug=True)