# app/utils/jwt_utils.py
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def decode_token(auth_header):
    if not auth_header or not auth_header.startswith("Bearer "):
        raise ValueError("Token missing or invalid")

    token = auth_header.replace("Bearer ", "")
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    
    user_id = decoded.get("user_id")
    if not user_id:
        raise ValueError("Invalid token data")

    return user_id
