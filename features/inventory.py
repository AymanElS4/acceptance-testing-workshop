class Product:
    """Fulfills the requirement of having a minimum of 4 attributes."""
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

class InventoryManager:
    """Main application logic for managing the inventory."""
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        self.inventory[product.name] = product
        print(f"\nSuccess: Product '{product.name}' added to inventory.")

    def list_products(self):
        if not self.inventory:
            print("\nInventory is empty.")
            return
        
        print("\nProducts:")
        for name, p in self.inventory.items():
            print(f"- {name} | Category: {p.category} | Price: ${p.price:.2f} | Quantity: {p.quantity}")

    def update_quantity(self, name, new_quantity):
        if name in self.inventory:
            self.inventory[name].quantity = int(new_quantity)
            print(f"\nSuccess: Product '{name}' quantity updated to {new_quantity}.")
        else:
            print(f"\nError: Product '{name}' not found.")

    def remove_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"\nProduct {name} was removed")
        else:
            print(f"\nProduct {name} was not found")