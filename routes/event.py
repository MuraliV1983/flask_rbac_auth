from flask import Blueprint, request, jsonify, session

event_bp = Blueprint("event", __name__)

def role_required(roles):
    def wrapper(func):
        def decorated(*args, **kwargs):
            user = session.get('user')
            if not user or user['role'] not in roles:
                return jsonify({"error": "Unauthorized"}), 403
            return func(*args, **kwargs)
        decorated.__name__ = func.__name__
        return decorated
    return wrapper

@event_bp.route('/create', methods=['POST'])
@role_required(['admin', 'editor'])
def create_event():
    data = request.json
    return jsonify({"message": f"Event '{data['title']}' created by {session['user']['username']}!"})
