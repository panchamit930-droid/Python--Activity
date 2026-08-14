products = {}

def add_products():
    product_id = input("Enter product id:")
    
    if product_id in products:
        print("ID already exist!")
        return
    
    product_name = input("Enter Product name:")
    category = input("Enter category:")
    try:
        price = int(input("Enter price:"))
        stock_quantity = int(input("Enter stock_quantity:"))
    except ValueError:
        print("Invalid value entered!")
        
    products[product_id] = {
        "Product ID" : product_id,
        "Product name" : product_name,
        "Category" : category,
        "Price" : price,
        "Stock quantity" : stock_quantity
    }
    
def display_products():
    if not products:
        print("No products available!")
    
    for product in products.values():
        print("\n===Products===")
        print(f"Product id : {product["Product ID"]}")     
        print(f"Product name : {product["Product name"]}")     
        print(f"Category : {product["Category"]}")     
        print(f"Price : {product["Price"]}")     
        print(f"Stock quantity : {product["Stock quantity"]}")  
        
def search_products():
    id = input("Enter Product id:")
    
    if id in products:
        product = products[id]
        
        print("Product details")
        print(f"Product id : {product["Product ID"]}")     
        print(f"Product name : {product["Product name"]}")     
        print(f"Category : {product["Category"]}")     
        print(f"Price : {product["Price"]}")     
        print(f"Stock quantity : {product["Stock quantity"]}")
    else:
        print("No Product found")
        
def delete_products():
    id = input("Enter Product id:")
    
    if id in products:
        del products[id]
        print("Product deleted!")
    else:
        print("No products found!")
        
while True:
    print("==Product Management System==")
    print("1. Add product")
    print("2. Display all products")
    print("3. Search product")
    print("4. Delete product")
    print("5. Exit")
    
    choice = int(input("Enter your choice:"))
    
    if choice == 1:
        add_products()
    elif choice == 2:
        display_products()
    elif choice == 3:
        search_products()
    elif choice == 4:
        delete_products()
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
    
    
       
    
    
            
    