cart = [
    {"name": "Apple", "quantity": 2, "price": 3.0},
    {"name": "Banana", "quantity": 5, "price": 1.5},
    {"name": "Orange", "quantity": 3, "price": 2.0}
]



def add_item(name, quantity, price):
    """Add item to cart. If already exists, increase quantity."""
    for item in cart:
        if item["name"].lower() == name.lower():
            item["quantity"] += quantity
            print(f"✅ Updated {name}: {item['quantity']} in cart")
            return
    cart.append({"name": name, "quantity": quantity, "price": price})
    print(f"🛒 Added {name} (x{quantity}) to cart")
    
    
def view_cart():
"""Display all items in the cart with total price"""
if not cart:
    print("🛒 Cart is empty")
    return

print("\nYour Cart:")
total = 0
for i, item in enumerate(cart, start=1):
    item_total = item["quantity"] * item["price"]
    total += item_total
    print(f"{i}. {item['name']} (x{item['quantity']}) - ${item_total:.2f}")
print(f"---\nTotal: ${total:.2f}\n")



def remove_item(name):
    if name in cart:
        del cart[name]
        print(f"❌ {name} removed from cart")
    else:
        print("⚠️ Item not found")


cart = []

add_item("Apple", 2, 3.0)      # 🛒 Added Apple (x2) to cart
add_item("Banana", 5, 1.5)     # 🛒 Added Banana (x5) to cart
add_item("Apple", 1, 3.0)      # ✅ Updated Apple: 3 in cart

view_cart()
# Output:
# Your Cart:
# 1. Apple (x3) - $9.00
# 2. Banana (x5) - $7.50
# ---
# Total: $16.50

remove_item(1)                 # ❌ Apple removed from cart
view_cart()
# Output:
# Your Cart:
# 1. Banana (x5) - $7.50
# ---
# Total: $7.50
