from storage import get_connection
import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(username, password):
    username = username.strip()

    if not username:
        return False, "Username cannot be empty."

    if len(password)<6:
        return False, "Password must be at least 6 characters."

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        conn.close()
        return False, "Username already exists."

    password_hash = hash_password(password)

    cursor.execute(
        "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
        (username, password_hash, ""),
    )

    conn.commit()
    conn.close()
    return True, "Registration successful!"


def login(username, password):
    username = username.strip()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False, "User not found."

    saved_hash = result["password_hash"]
    password_hash = hash_password(password)

    conn.close()

    if password_hash == saved_hash:
        return True, "Login successful!"
    return False, "Incorrect password."
