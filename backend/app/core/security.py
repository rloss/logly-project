from jose import JWTError, jwt
from datetime import datetime, timedelta

def create_access_token(data: dict, secret_key: str, algorithm: str, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)
