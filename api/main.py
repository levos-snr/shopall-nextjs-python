from flask import  request, jsonify
from config import app, db
from models import User

@app.route("/api/welcome")
def hello_world():
    return jsonify({"message": "Welcome to the API"}), 200
    
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users]), 200
    
@app.route('/api/users/<int:user_id>', methods=['GET'])    
def get_user(user_id):    
    user = User.query.get_or_404(user_id)    
    return jsonify(user.to_json()), 200
    
@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.email = data['email']
    user.is_active = data['is_active']
    user.is_admin = data['is_admin']
    db.session.commit()
    return jsonify(user.to_json()), 200

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
    
if __name__ == '__main__':
    app.run(debug=True)


