import jwt

SECRET_KEY = 'your_secret_key'  

def validate_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data
    except jwt.ExpiredSignatureError:
        return {'error': 'Token has expired!'}
    except jwt.InvalidTokenError:
        return {'error': 'Token is invalid!'}

def main():
    token = input("Enter token to validate: ")
    result = validate_token(token)
    print(f"Validation result: {result}")

if __name__ == "__main__":
    main()

