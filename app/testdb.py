import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = 'users.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def register_user(username, password, role):
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)',
                       (username, generate_password_hash(password), role))
        conn.commit()
        return 'Registration successful!'
    except sqlite3.IntegrityError:
        return 'User already exists!'
    except Exception as e:
        return f'An error occurred: {e}'
    finally:
        conn.close()

def query_users(role):
    conn = get_db()
    cursor = conn.cursor()
    
    if role == 'root':
        query = 'SELECT username FROM users'
    elif role == 'admin':
        query = 'SELECT username FROM users WHERE role IN ("developer", "trainee")'
    elif role == 'developer':
        query = 'SELECT username FROM users WHERE role = "trainee"'
    else:
        return []

    cursor.execute(query)
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return users

def main():
    action = input("Enter 'register' to register a user or 'query' to query users: ").strip().lower()
    
    if action == 'register':
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (root/admin/developer/trainee): ")
        result = register_user(username, password, role)
        print(result)
    
    elif action == 'query':
        role = input("Enter role (root/admin/developer/trainee): ")
        users = query_users(role)
        print(f"Users: {users}")

if __name__ == "__main__":
    main()

