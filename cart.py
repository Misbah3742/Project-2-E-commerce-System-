from storage import get_connection
from products import get_product


def add_to_cart(username, product_id, qty):
    # Check quantity
    if qty <= 0:
        return False, "Quantity must be greater than zero."

    # Check if product exists
    product = get_product(product_id)
    if not product:
        return False, "Product not found."

    # Check stock
    if qty > product["stock"]:
        return False, "Not enough stock available."

    conn = get_connection()
    cursor = conn.cursor()

    # Check if product already in cart
    cursor.execute(
        "SELECT qty FROM carts WHERE username = ? AND product_id = ?",
        (username, product_id),
    )
    result = cursor.fetchone()

    if result:
        # Update quantity
        new_qty = result["qty"] + qty
        if new_qty > product["stock"]:
            conn.close()
            return False, "Total quantity exceeds available stock."
        cursor.execute(
            "UPDATE carts SET qty = ? WHERE username = ? AND product_id = ?",
            (new_qty, username, product_id),
        )
    else:
        # Add new item
        cursor.execute(
            "INSERT INTO carts (username, product_id, qty) VALUES (?, ?, ?)",
            (username, product_id, qty),
        )

    conn.commit()
    conn.close()
    return True, "Added to cart!"


def remove_from_cart(username, product_id, qty=None):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if item in cart
    cursor.execute(
        "SELECT qty FROM carts WHERE username = ? AND product_id = ?",
        (username, product_id),
    )
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False, "Item not in cart."

    current_qty = result["qty"]

    # Remove all or reduce quantity
    if qty is None or qty >= current_qty:
        cursor.execute(
            "DELETE FROM carts WHERE username = ? AND product_id = ?",
            (username, product_id),
        )
    else:
        new_qty = current_qty - qty
        cursor.execute(
            "UPDATE carts SET qty = ? WHERE username = ? AND product_id = ?",
            (new_qty, username, product_id),
        )

    conn.commit()
    conn.close()
    return True, "Cart updated."


def get_cart(username):
    conn = get_connection()
    cursor = conn.cursor()

    # Get cart items with product details
    cursor.execute(
        """
        SELECT c.product_id, c.qty, p.name, p.price, p.stock
        FROM carts c
        JOIN products p ON c.product_id = p.product_id
        WHERE c.username = ?
    """,
        (username,),
    )

    rows = cursor.fetchall()
    conn.close()

    items = []
    total = 0

    for row in rows:
        subtotal = row["qty"] * row["price"]
        total = total + subtotal

        item = {
            "product_id": row["product_id"],
            "name": row["name"],
            "qty": row["qty"],
            "price": row["price"],
            "subtotal": subtotal,
            "stock": row["stock"],
        }
        items.append(item)

    return items, total


def clear_cart(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carts WHERE username = ?", (username,))
    conn.commit()
    conn.close()
