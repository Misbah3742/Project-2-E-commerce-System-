from storage import init_db
from users import register, login
from products import list_products, search_products, get_product, add_product
from cart import add_to_cart, remove_from_cart, get_cart
from orders import checkout, get_order_history, setup_discount_codes


def setup_default_products():
    products = list_products()
    if len(products) == 0:
        add_product("USB Cable", 8.0, 20)
        add_product("Wireless Mouse", 15.0, 15)
        add_product("Keyboard", 25.0, 12)
        add_product("Headphones", 30.0, 10)
        add_product("Phone Charger", 10.0, 25)
        add_product("Laptop Stand", 22.0, 8)
        add_product("Bluetooth Speaker", 35.0, 9)
        add_product("USB Drive 64GB", 12.0, 18)


def show_products(products):
    if len(products) == 0:
        print("No products found.")
        return

    print("\n=== PRODUCTS ===")
    for p in products:
        print(
            "ID:",
            p["product_id"],
            "| Name:",
            p["name"],
            "| Price: $" + str(p["price"]),
            "| Stock:",
            p["stock"],
        )
    print()


def browse_products_menu(username):
    products = list_products()
    show_products(products)

    product_id = input("Enter product ID to add to cart (or press Enter to go back): ")
    if not product_id:
        return

    try:
        product_id = int(product_id)
    except ValueError:
        print("Invalid product ID.")
        return

    product = get_product(product_id)
    if not product:
        print("Product not found.")
        return

    qty = input("Enter quantity: ")
    try:
        qty = int(qty)
    except ValueError:
        print("Invalid quantity.")
        return

    success, message = add_to_cart(username, product_id, qty)
    print(message)


def search_products_menu(username):
    keyword = input("Enter search keyword: ")
    if not keyword:
        return

    products = search_products(keyword)
    show_products(products)

    product_id = input("Enter product ID to add to cart (or press Enter to go back): ")
    if not product_id:
        return

    try:
        product_id = int(product_id)
    except ValueError:
        print("Invalid product ID.")
        return

    product = get_product(product_id)
    if not product:
        print("Product not found.")
        return

    qty = input("Enter quantity: ")
    try:
        qty = int(qty)
    except ValueError:
        print("Invalid quantity.")
        return

    success, message = add_to_cart(username, product_id, qty)
    print(message)


def view_cart_menu(username):
    items, total = get_cart(username)

    if len(items) == 0:
        print("Your cart is empty.")
        return

    print("\n=== YOUR CART ===")
    for item in items:
        print("Product:", item["name"])
        print("  Quantity:", item["qty"])
        print("  Unit Price: $" + str(item["price"]))
        print("  Subtotal: $" + str(item["subtotal"]))
        print()

    print("Total: $" + str(total))
    print()

    remove = input("Do you want to remove an item? (y/n): ")
    if remove.lower() != "y":
        return

    product_id = input("Enter product ID to remove: ")
    try:
        product_id = int(product_id)
    except ValueError:
        print("Invalid product ID.")
        return

    qty = input("Enter quantity to remove (or press Enter to remove all): ")
    if qty:
        try:
            qty = int(qty)
        except ValueError:
            print("Invalid quantity.")
            return
    else:
        qty = None

    success, message = remove_from_cart(username, product_id, qty)
    print(message)


def checkout_menu(username):
    items, total = get_cart(username)

    if len(items) == 0:
        print("Your cart is empty.")
        return

    print("\n=== CHECKOUT ===")
    for item in items:
        print(item["name"], "x", item["qty"], "= $" + str(item["subtotal"]))
    print("Total: $" + str(total))
    print()

    discount_code = input("Enter discount code (or press Enter to skip): ")
    if not discount_code:
        discount_code = None

    success, message, receipt = checkout(username, discount_code)
    print(message)

    if success and receipt:
        print("\n=== RECEIPT ===")
        print("Order ID:", receipt["order_id"])
        print("Date:", receipt["timestamp"])
        print()
        for item in receipt["items"]:
            print(item["name"], "x", item["qty"], "@ $" + str(item["price"]))
        print()
        print("Subtotal: $" + str(receipt["total"]))
        if receipt["discount_code"]:
            print(
                "Discount ("
                + receipt["discount_code"]
                + "): -$"
                + str(receipt["discount_amount"])
            )
        print("Final Total: $" + str(receipt["final_total"]))
        print()


def order_history_menu(username):
    orders = get_order_history(username)

    if len(orders) == 0:
        print("You have no orders yet.")
        return

    print("\n=== ORDER HISTORY ===")
    for order in orders:
        print("\nOrder ID:", order["order_id"])
        print("Date:", order["created_at"])
        print("Status:", order["status"])
        print("Items:")
        for item in order["items"]:
            print("  -", item["name"], "x", item["qty"], "@ $" + str(item["price"]))
        if order["discount_code"]:
            print(
                "Discount:",
                order["discount_code"],
                "(-$" + str(order["discount_amount"]) + ")",
            )
        print("Total: $" + str(order["total_price"]))


def store_menu(username):
    while True:
        print("\n--- STORE MENU ---")
        print("1. Browse products")
        print("2. Search products")
        print("3. View cart")
        print("4. Checkout")
        print("5. View order history")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            browse_products_menu(username)
        elif choice == "2":
            search_products_menu(username)
        elif choice == "3":
            view_cart_menu(username)
        elif choice == "4":
            checkout_menu(username)
        elif choice == "5":
            order_history_menu(username)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    init_db()
    setup_discount_codes()
    setup_default_products()

    print("Mini Shop Project")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- REGISTRATION ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = register(username, password)
            print(message)

        elif choice == "2":
            print("\n--- LOGIN ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login(username, password)
            print(message)

            if success:
                store_menu(username)

        elif choice == "3":
            print("Thank you for using Mini-Amazon! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
