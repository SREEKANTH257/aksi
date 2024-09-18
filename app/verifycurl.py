from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    # Simple validation
    if not username or not password or not role:
        return jsonify({'message': 'Missing fields'}), 400

    # Perform your login logic here (e.g., check credentials)

    return jsonify({'message': 'Login successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)


