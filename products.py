from storage import get_db_connection

def add_product(name, price, stock):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', (name, price, stock))
    conn.commit()
    conn.close()
    
def list_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT product_id, name, price, stock FROM products')
    rows = cursor.fetchall()
    conn.close()
    
    products = []
    
    for row in rows:
        product = {
            'product_id': row['product_id'],
            'name': row['name'],
            'price': row['price'],
            'stock': row['stock']   
        }
        products.append(product)
    return products

def search_products(keyword):
    conn = get_db_connection()
    cursor = conn.cursor()
    search_term = "%" + keyword.lower() + "%"
    cursor.execute(
        'SELECT product_id, name, price, stock FROM products WHERE LOWER(name) LIKE ?', (search_term,),
   )
    rows = cursor.fetchall()
    conn.close()
    
    products = []
    
    for row in rows:
        product = {
            'product_id': row['product_id'],
            'name': row['name'],
            'price': row['price'],
            'stock': row['stock']   
        }
        products.append(product)
    return products

def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'SELECT product_id, name, price, stock FROM products WHERE product_id = ?',
        (product_id,),
    )
    row = cursor.fetchone()
    conn.close()
    
    if row:
        product = {
            'product_id': row['product_id'],
            'name': row['name'],
            'price': row['price'],
            'stock': row['stock']   
        }
        return product
    return None
