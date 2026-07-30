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


def main():
    """Command-line application loop."""
    manager = InventoryManager()

while True:
    print("\n=== Inventory Manager ===")
    print("1. Add a new product")
    print("2. List all products")
    print("3. Update product quantity")
    print("4. Remove a product")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")
        try:
            new_product = Product(name, category, price, quantity)
            manager.add_product(new_product)
        except ValueError:
            print("\nError: Price must be a number and Quantity must be an integer.")

    elif choice == '2':
        manager.list_products()

    elif choice == '3':
        name = input("Enter product name to update: ")
        quantity = input("Enter new quantity: ")
        try:
            manager.update_quantity(name, quantity)
        except ValueError:
            print("\nError: Quantity must be an integer.")

    elif choice == '4':
        name = input("Enter product name to remove: ")
        manager.remove_product(name)

    elif choice == '5':
        print("\nExiting Inventory Manager. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 5.")

    if __name__ == "__main__":
        main()