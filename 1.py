'''Items in the inventory.txt file'''
# Marie, Cookies, 20.0, 10, 2025-01-04
# Pineapple,Fruits,0.5,100,2024-12-31
# Milk,Dairy,1.5,50,2024-07-01
# Carrot,Vegetables,0.7,200,2024-08-15
# Cheese,Dairy,2.5,20,2024-06-30
# Banana,Fruits,0.3,150,2024-06-20
# Cucumber,Vegetables,1.2,80,2024-07-05
# Chicken,Meat,5.0,30,2024-06-25
# Fish,Seafood,6.0,25,2024-07-05
# Shrimp,Seafood,8.0,15,2024-06-30

class Product:
    def __init__(self, name, category, price, quantity, expiration_date):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date

class InventoryManagementSystem:
    def __init__(self):
        self.products = []
        self.load_inventory_from_file('inventory.txt')

    def add_product_to_inventory(self, product):
        self.products.append(product)

    def remove_product_from_inventory(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def search_products(self, search_term):
        return [product for product in self.products if search_term.lower() in product.name.lower() or search_term.lower() in product.category.lower()]

    def list_all_products(self):
        for product in self.products:
            print(f"Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}, Expiration Date: {product.expiration_date}")

    def categorize_products(self):
        categorized_products = {}
        for product in self.products:
            if product.category not in categorized_products:
                categorized_products[product.category] = []
            categorized_products[product.category].append(product)
        return categorized_products

    def check_and_remove_expired_products(self):
        today = "2024-06-17" #Change the accordingly as the day you see this 
        self.products = [product for product in self.products if product.expiration_date >= today]

    def save_inventory_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for product in self.products:
                    file.write(f"{product.name}, {product.category}, {product.price}, {product.quantity}, {product.expiration_date}\n")
        except IOError as e:
            print(f"An error occurred while saving the inventory to file: {e}")

    def load_inventory_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, category, price, quantity, expiration_date = line.strip().split(',')
                    product = Product(name, category, float(price), int(quantity), expiration_date)
                    self.products.append(product)
        except FileNotFoundError:
            print(f"No inventory file found. Starting with an empty inventory.")
        except IOError as e:
            print(f"An error occurred while loading the inventory from file: {e}")

ims = InventoryManagementSystem()

while True:
    print("\nInventory Management System")
    print("1. Add a product")
    print("2. Remove a product")
    print("3. Search for products")
    print("4. List all products")
    print("5. Categorize products")
    print("6. Check for expired products and remove them")
    print("7. Save inventory to file")
    print("8. Load inventory from file")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        expiration_date = input("Enter product expiration date (YYYY-MM-DD): ")
        product = Product(name, category, price, quantity, expiration_date)
        ims.add_product_to_inventory(product)
        print("Product added successfully!")

    elif choice == 2:
        name = input("Enter product name to remove: ")
        ims.remove_product_from_inventory(name)
        print("Product removed successfully!")

    elif choice == 3:
        search_term = input("Enter product name or category to search: ")
        results = ims.search_products(search_term)
        if results:
            for product in results:
                print(f"Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}, Expiration Date: {product.expiration_date}")
        else:
            print("No products found matching the search term.")

    elif choice == 4:
        ims.list_all_products()

    elif choice == 5:
        categorized_products = ims.categorize_products()
        for category, products in categorized_products.items():
            print(f"\nCategory: {category}")
            for product in products:
                print(f"  Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Expiration Date: {product.expiration_date}")

    elif choice == 6:
        ims.check_and_remove_expired_products()
        print("Expired products removed successfully!")

    elif choice == 7:
        ims.save_inventory_to_file('inventory.txt')
        print("Inventory saved to file successfully!")

    elif choice == 8:
        ims.load_inventory_from_file('inventory.txt')
        print("Inventory loaded from file successfully!")

    elif choice == 9:
        print("Exiting the system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
