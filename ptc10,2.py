products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"]

item = input("Enter product name: ")

if item in products:
    print("Item found!")
    print("Index:", products.index(item))
else:
    print("Item not found.")
