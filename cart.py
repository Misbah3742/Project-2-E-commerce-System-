from storage import Storage
from products import get_product

def add_to_cart(user_id, product_id, qty):
    
    #check if product exists
    if qty <= 0:
        return False, "Quantity must be greater than 0"
    
    #check if product exists
    product = get_product(product_id)
    if not product:
        return False, "Product not found"
    
    #check if stock is sufficient
    if qty > product['stock']:
        return False, "Insufficient stock"  
    
    conn = get_connection()
    cursor = conn.cursor()
    
    #check if item is already in cart
    cursor.execute(
        'SELECT cart_id, quantity FROM cart WHERE user_id = ? AND product_id = ?',
        (user_id, product_id)
    )
    result = cursor.fetchone()  
    
    if result:
        #update quantity
        new_qty = result['quantity'] + qty
        if new_qty > product['stock']:
            conn.close()
            return False, "Insufficient stock for the updated quantity"
        cursor.execute(
            'UPDATE cart SET qty = ? WHERE username = ? and product_id = ?',
            (new_qty, user_id, product_id)
        )
    else:   
        cursor.execute(
            'INSERT INTO cart (username, product_id, qty) VALUES (?, ?, ?)',
            (user_id, product_id, qty),
            )
    conn.commit()
    conn.close()
    return True, "Product added to cart successfully"

def remove_from_cart(user_id, product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM cart WHERE username = ? AND product_id = ?',
        (user_id, product_id)
    )
    conn.commit()
    conn.close()
    return True, "Product removed from cart successfully"