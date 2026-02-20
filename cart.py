from storage import get_connection
from products import get_product


def add_to_cart(username, product_id, qty):
    if qty <= 0:
        return False, "Quantity must be greater than zero."

    product = get_product(product_id)
    if not product:
        return False, "Product not found."

    if qty > product["stock"]:
        return False, "Not enough stock available."

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT qty FROM carts WHERE username = ? AND product_id = ?",
        (username, product_id),
    )
    result = cursor.fetchone()

    if result:
        oldQty = result["qty"]
        new_qty = oldQty + qty
        if new_qty > product["stock"]:
            conn.close()
            return False, "Total quantity exceeds available stock."
        cursor.execute(
            "UPDATE carts SET qty = ? WHERE username = ? AND product_id = ?",
            (new_qty, username, product_id),
        )
    else:
        # first time add
        cursor.execute(
            "INSERT INTO carts (username, product_id, qty) VALUES (?, ?, ?)",
            (username, product_id, qty),
        )

    conn.commit()
    conn.close()
    return True, "Added to cart!"


def remove_from_cart(username, product_id, qty=None):
    if qty is not None and qty <= 0:
        return False, "Quantity to remove must be greater than zero."

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT qty FROM carts WHERE username = ? AND product_id = ?",
        (username, product_id),
    )
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False, "Item not in cart."

    current_qty = result["qty"]

    if qty is None or qty >= current_qty:
        # remove full row
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
        q = row["qty"]
        pr = row["price"]
        subtotal = q * pr
        total = total + subtotal

        item = {}
        item["product_id"] = row["product_id"]
        item["name"] = row["name"]
        item["qty"] = q
        item["price"] = pr
        item["subtotal"] = subtotal
        item["stock"] = row["stock"]
        items.append(item)

    return items, total


def clear_cart(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carts WHERE username = ?", (username,))
    conn.commit()
    conn.close()
