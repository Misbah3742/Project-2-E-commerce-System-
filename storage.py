import sqlite3

DB_FILE = "data.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    
    #user table
    cursor.execute('''
        CEATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    ''')
    
    #product table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INEGER PRIMARY KEY AUTOCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )'''
    )
    
    
    #cart table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carts (
            username TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            PRIMARY KEY (username, product_id),
            )''')
    
    #order table
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOCREMENT,
            username TEXT NOT NULL,
            total_price REAL NOT NULL,
            discount_code TEXT,
            discount_amount REAL DEFAULT 0,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )''')
    
    #order_items table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            order_item_id INTEGER PRIMARY KEY AUTOCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            price REAL NOT NULL,
            )''')
    
    #discount_codes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS discount_codes (
            code TEXT PRIMARY KEY,
            percent REAL NOT NULL,
            active INTEGER DEFUALT 1
        )''')
    
    conn.commit()
    conn.close()