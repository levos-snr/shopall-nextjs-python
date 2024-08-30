from flask import request, jsonify
from . import app, db
from .models import User

@app.route("/api/welcome")
def hello_world():
    return jsonify({"message": "Welcome to the API"}), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_json() for user in users]), 200
    except Exception as e:
        app.logger.error(f"Error fetching users: {str(e)}")
        return jsonify({"error": "An error occurred while fetching users"}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])    
def get_user(user_id):    
    try:
        user = User.query.get_or_404(user_id)    
        return jsonify(user.to_json()), 200
    except Exception as e:
        app.logger.error(f"Error fetching user {user_id}: {str(e)}")
        return jsonify({"error": f"An error occurred while fetching user {user_id}"}), 500

@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    try:
        data = request.json
        user = User.query.get_or_404(user_id)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.is_active = data.get('is_active', user.is_active)
        user.is_admin = data.get('is_admin', user.is_admin)
        db.session.commit()
        return jsonify(user.to_json()), 200
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error updating user {user_id}: {str(e)}")
        return jsonify({"error": f"An error occurred while updating user {user_id}"}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error deleting user {user_id}: {str(e)}")
        return jsonify({"error": f"An error occurred while deleting user {user_id}"}), 500

# Error handling for 404 and 500 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({"error": "Internal server error"}), 500