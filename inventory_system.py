def sell_product(inventory, product, quantity):
    if product not in inventory:
        print(f"{product} not found")
        return

    if inventory[product]["stock"] < quantity:
        print(f"Insufficient stock for {product}")
        return

    inventory[product]["stock"] -= quantity
    print(f"{quantity} {product}(s) sold successfully")


def total_inventory_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["price"] * item["stock"]
    print("Total Inventory Value =", total)


def low_stock_items(inventory):
    low_stock = [name for name, item in inventory.items() if item["stock"] < 10]
    print("Low Stock Items:", ", ".join(low_stock))

if __name__ == "__main__":
    inventory = {
        "Laptop": {"price": 60000, "stock": 5},
        "Mouse": {"price": 500, "stock": 50},
        "Keyboard": {"price": 1500, "stock": 20}
    }

    sell_product(inventory, "Mouse", 5)
    total_inventory_value(inventory)
    low_stock_items(inventory)
