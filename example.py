class Item:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, category, quantity, price):
        item = Item(name, category, quantity, price)
        self.items.append(item)

    def view_inventory(self):
        print("Inventory:")
        for item in self.items:
            print(f"Name: {item.name}, Category: {item.category}, Quantity: {item.quantity}, Price: ${item.price:.2f}")

# Sample usage
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item("Whiskey", "Spirits", 50, 25.0)
    inventory.view_inventory()
