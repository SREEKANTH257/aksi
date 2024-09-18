from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

jwt = JWTManager(app)

DATABASE = 'users.db'

def get_db():
    """Create and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    """Initialize the database with required tables."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'message': 'All fields are required!'}), 400

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                       (username, generate_password_hash(password), role))
        conn.commit()
        return jsonify({'message': 'Registration successful!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'message': 'User already exists!'}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred. Please try again later.'}), 500
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    if not username or not password or not role:
        return jsonify({'message': 'Username, password, and role required!'}), 400

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT password, role FROM users WHERE username=? AND role=?', (username, role))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[0], password):
        # Create JWT token
        access_token = create_access_token(identity={'username': username, 'role': user[1]})
        return jsonify({'message': 'Login successful!', 'token': access_token}), 200

    return jsonify({'message': 'Invalid credentials or role!'}), 401

@app.route('/api/dashboard', methods=['GET'])
@jwt_required()
def dashboard_data():
    current_user = get_jwt_identity()
    user_role = current_user['role']

    if user_role == 'root':
        # Root can see all users
        query = 'SELECT username FROM users'
    elif user_role == 'admin':
        # Admin can see developers and trainees
        query = 'SELECT username FROM users WHERE role IN ("developer", "trainee")'
    elif user_role == 'developer':
        # Developer can see only trainees
        query = 'SELECT username FROM users WHERE role = "trainee"'
    else:
        # Trainee sees nothing
        return jsonify({'users': []}), 200

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query)
    users = [row[0] for row in cursor.fetchall()]
    conn.close()

    return jsonify({'users': users}), 200

if __name__ == '__main__':
    init_db()  # Initialize the database when starting the app
    app.run(host='0.0.0.0', port=5000, debug=True)
