# app/controllers/mutuals_controller.py
from flask import Blueprint, request, jsonify
from utils.jwt_utils import decode_token
from queries.get_mutual_followers import get_mutual_followers

bp = Blueprint("mutuals", __name__)

@bp.route('/get-mutuals', methods=['GET'])
def get_mutuals():
    try:
        auth_header = request.headers.get("Authorization")
        user_id = decode_token(auth_header)
    except Exception as e:
        return jsonify({"error": str(e)}), 401

    mutuals = get_mutual_followers(user_id)
    return jsonify(mutuals), 200
