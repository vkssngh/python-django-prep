# Shopping Cart Project (Lists & Tuples)

cart = []  # list to hold items (each item = tuple(name, price))

def add_item(name, price):
    """Add an item (tuple) to the cart"""
    item = (name, price)
    cart.append(item)
    print(f"✅ {name} added to cart")

def view_cart():
    """Display all items in the cart"""
    if not cart:
        print("🛒 Your cart is empty!")
        return
    print("\n🛍️ Your Cart:")
    for idx, (name, price) in enumerate(cart, start=1):
        print(f"{idx}. {name} - ₹{price}")
    print("-" * 30)

def total_price():
    """Calculate total price"""
    total = sum(price for _, price in cart)
    print(f"💰 Total: ₹{total}")
    return total

def remove_item(index):
    """Remove item by index (1-based)"""
    if 1 <= index <= len(cart):
        removed = cart.pop(index-1)
        print(f"❌ {removed[0]} removed from cart")
    else:
        print("⚠️ Invalid index")

# --- Demo ---
if __name__ == "__main__":
    add_item("Laptop", 50000)
    add_item("Mouse", 500)
    add_item("Keyboard", 1500)

    view_cart()
    total_price()

    remove_item(2)  # remove Mouse
    view_cart()
    total_price()
    
    
    
✅ Laptop added to cart
✅ Mouse added to cart
✅ Keyboard added to cart

🛍️ Your Cart:
1. Laptop - ₹50000
2. Mouse - ₹500
3. Keyboard - ₹1500
------------------------------
💰 Total: ₹52000

❌ Mouse removed from cart

🛍️ Your Cart:
1. Laptop - ₹50000
2. Keyboard - ₹1500
------------------------------
💰 Total: ₹51500
