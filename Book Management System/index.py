books = {}

def add_books():
    book_id = input("Enter book id:")
    
    if book_id in books:
        print("ID already exist!")
        return
    
    book_name = input("Enter Book name:")
    auther = input("Enter auther:")
    category = input("Enter category:")
    try:
        price = int(input("Enter price:"))
    except ValueError:
        print("Invalid value entered!")
        
    books[book_id] = {
        "Book ID" : book_id,
        "Book name" : book_name,
        "Auther" : auther,
        "Category" : category,
        "Price" : price,
    }
    
def display_books():
    if not books:
        print("No books available!")
        print("\n===Books===")
    for book in books.values():
        print(f"Book id : {book["Book ID"]}")     
        print(f"Book name : {product["Product name"]}")     
        print(f"Category : {product["Category"]}")     
        print(f"Price : {product["Price"]}")     


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