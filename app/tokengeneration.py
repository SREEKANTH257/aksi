import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = 'your_secret_key'  

def generate_token(username, role):
    token = jwt.encode({
        'username': username,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm='HS256')
    return token

def main():
    username = 'test_user'
    role = 'admin' #generate token accoring to role here
    token = generate_token(username, role)
    print(f"Generated token: {token}")

if __name__ == "__main__":
    main()

