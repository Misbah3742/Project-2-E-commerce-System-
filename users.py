from storage import get_connection
import hashlib
import secrets


def hash_password(password, salt):
    # Combine salt and password, then hash
    data = salt + password
    return hashlib.sha256(data.encode()).hexdigest()


def register(username, password):
    # Check if username is empty
    if not username:
        return False, "Username cannot be empty."

    # Check password length
    if len(password) < 6:
        return False, "Password must be at least 6 characters."

    # Connect to database
    conn = get_connection()
    cursor = conn.cursor()

    # Check if username already exists
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        conn.close()
        return False, "Username already exists."

    # Generate random salt and hash password
    salt = secrets.token_hex(16)
    password_hash = hash_password(password, salt)

    # Insert new user
    cursor.execute(
        "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
        (username, password_hash, salt),
    )

    conn.commit()
    conn.close()
    return True, "Registration successful!"


def login(username, password):
    # Connect to database
    conn = get_connection()
    cursor = conn.cursor()

    # Find user
    cursor.execute(
        "SELECT password_hash, salt FROM users WHERE username = ?", (username,)
    )
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False, "User not found."

    # Check password
    stored_hash = result["password_hash"]
    salt = result["salt"]
    password_hash = hash_password(password, salt)

    conn.close()

    if password_hash == stored_hash:
        return True, "Login successful!"
    else:
        return False, "Incorrect password."
