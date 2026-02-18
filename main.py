from storage import init_db
from users import register, login
from products import list_products, search_products, get_product, add_product
from cart import add_to_cart, remove_from_cart, get_cart
from orders import checkout, get_order_history, setup_discount_codes


def setup_default_products():
    # Add some products if database is empty
    products = list_products()
    if len(products) == 0:
        # Cables & Connectors
        add_product("USB-C Cable", 9.99, 50)
        add_product("USB-A to USB-C Adapter", 8.99, 45)
        add_product("HDMI 2.1 Cable 6ft", 14.99, 40)
        add_product("USB 3.0 Hub 4-Port", 19.99, 35)
        add_product("Lightning Cable 2-Pack", 12.99, 55)
        add_product("Micro USB Cable 3-Pack", 9.99, 60)
        add_product("DisplayPort Cable", 15.99, 30)
        add_product("Ethernet Cable 25ft", 11.99, 38)
        add_product("VGA Cable", 7.99, 42)
        add_product("USB-C Hub 7-in-1", 29.99, 25)
        
        # Mice & Keyboards
        add_product("Wireless Mouse", 19.99, 50)
        add_product("Mechanical Keyboard RGB", 79.99, 22)
        add_product("Optical Gaming Mouse", 34.99, 28)
        add_product("Wireless Keyboard", 39.99, 20)
        add_product("Bluetooth Mouse Pro", 44.99, 18)
        add_product("Quiet Mechanical Keyboard", 89.99, 15)
        add_product("Ergonomic Mouse", 29.99, 32)
        add_product("Wired Gaming Mouse", 24.99, 35)
        add_product("Laptop Keyboard USB", 34.99, 25)
        add_product("Compact Wireless Keyboard", 32.99, 27)
        
        # Monitors & Displays
        add_product("4K Monitor 27-inch", 299.99, 8)
        add_product("Gaming Monitor 144Hz", 249.99, 12)
        add_product("Portable Monitor 15.6", 169.99, 14)
        add_product("Ultrawide Monitor 34-inch", 399.99, 6)
        add_product("22-inch FHD Monitor", 149.99, 18)
        add_product("32-inch Curved Monitor", 329.99, 9)
        add_product("USB-C Monitor", 379.99, 7)
        add_product("Touchscreen Monitor 24-inch", 449.99, 5)
        
        # Headphones & Speakers
        add_product("Wireless Headphones Noise Cancelling", 149.99, 20)
        add_product("Gaming Headset", 79.99, 28)
        add_product("Bluetooth Speaker Portable", 59.99, 35)
        add_product("Earbuds Wireless Pro", 119.99, 30)
        add_product("Studio Headphones", 199.99, 12)
        add_product("Sports Earbuds", 49.99, 40)
        add_product("Stereo Speakers Powered", 89.99, 22)
        add_product("Wireless Charging Earbuds", 99.99, 25)
        add_product("Professional Mic USB", 89.99, 18)
        add_product("Docking Speaker", 69.99, 24)
        
        # Storage Devices
        add_product("SSD 1TB NVMe", 79.99, 35)
        add_product("External SSD 1TB", 99.99, 30)
        add_product("USB Flash Drive 64GB", 12.99, 50)
        add_product("Portable Hard Drive 2TB", 69.99, 28)
        add_product("Memory Card MicroSD 256GB", 24.99, 45)
        add_product("USB Flash Drive 128GB", 19.99, 40)
        add_product("SSD 2TB NVMe", 139.99, 20)
        add_product("Memory Card SD 128GB", 29.99, 35)
        add_product("External SSD 2TB", 179.99, 15)
        add_product("USB 3.1 Flash Drive 32GB", 9.99, 60)
        
        # Laptop Accessories
        add_product("Laptop Stand Adjustable", 29.99, 40)
        add_product("Laptop Cooling Pad", 34.99, 32)
        add_product("Laptop Sleeve 15.6 inch", 19.99, 45)
        add_product("Laptop Backpack", 49.99, 25)
        add_product("Laptop Lock Cable", 12.99, 50)
        add_product("Laptop Riser Desk Mount", 39.99, 28)
        add_product("Laptop Docking Station", 99.99, 18)
        add_product("Laptop Screen Protector", 24.99, 35)
        add_product("Laptop Keyboard Cover", 9.99, 55)
        add_product("Laptop Power Bank 30000mAh", 59.99, 22)
        
        # Gaming Peripherals
        add_product("Gaming Mouse Pad XL", 24.99, 40)
        add_product("Gaming Controller Wireless", 59.99, 30)
        add_product("RGB Gaming Keyboard", 99.99, 20)
        add_product("Gaming Desk Mat", 34.99, 35)
        add_product("VR Headset", 299.99, 8)
        add_product("Gaming Eye Care Glasses", 39.99, 25)
        add_product("Gaming Chair", 249.99, 10)
        add_product("Cable Management Kit", 14.99, 50)
        add_product("Gaming Desk Organizer", 29.99, 32)
        add_product("RGB LED Strip 16ft", 19.99, 38)
        
        # Smart Home
        add_product("Smart LED Bulb RGB", 14.99, 45)
        add_product("Smart Plug", 9.99, 55)
        add_product("Smart Speaker Mini", 29.99, 40)
        add_product("Smart Camera Indoor", 54.99, 25)
        add_product("Smart Doorbell", 99.99, 15)
        add_product("Motion Sensor Light", 19.99, 38)
        add_product("Smart Thermostat", 149.99, 12)
        add_product("Smart Door Lock", 179.99, 10)
        add_product("WiFi Extender", 34.99, 28)
        add_product("Smart Outlet Surge Protector", 24.99, 35)
        
        # Mobile Accessories
        add_product("Phone Case Universal", 9.99, 60)
        add_product("Screen Protector Tempered Glass", 6.99, 70)
        add_product("Phone Screen Cleaner", 7.99, 65)
        add_product("Phone Mount Car", 12.99, 50)
        add_product("Wireless Charging Pad", 19.99, 40)
        add_product("Fast Charger 65W", 34.99, 32)
        add_product("Phone Ring Stand", 8.99, 55)
        add_product("Phone Tripod", 14.99, 45)
        add_product("Screen Protector Film", 4.99, 80)
        add_product("Phone Cooling Fan", 14.99, 40)
        
        # Networking
        add_product("WiFi Router Mesh", 129.99, 16)
        add_product("Network Switch 8-Port", 44.99, 22)


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
        print("\n========== STORE MENU ==========")
        print("1. Browse products")
        print("2. Search products")
        print("3. View cart")
        print("4. Checkout")
        print("5. View order history")
        print("6. Logout")
        print("================================")

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
    # Initialize database
    init_db()
    setup_discount_codes()
    setup_default_products()

    print("=" * 40)
    print("   WELCOME TO MINI-AMAZON SYSTEM")
    print("=" * 40)

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        print("===============================")

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
