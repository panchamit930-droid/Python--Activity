# Activity 1 — Student Management System 
# Create a Student class with: • name • age • email • course 
# Methods: • display_details() • update_course() 
# Task: Create 3 student objects, display their details, and update the course of one student.
# class Student:
#     def __init__(self , name , age , email , course):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.course = course
#     def display_details(self):
#         print(f'Name : {self.name}')
#         print(f'Age : {self.age}')
#         print(f'Email : {self.email}')
#         print(f'Course : {self.course}')
#     def update_course(self, newCourse):
#         self.course = newCourse
# ob1 = Student('Anil', 25, 'anil@gmail.com', 'Python')
# ob1.display_details()
# ob2 = Student('Sona', 25, 'sona@gmail.com', 'Python')
# ob2.display_details()
# ob3 = Student('Sunil', 25, 'sunil@gmail.com', 'Python')
# ob3.display_details()
# ob1.update_course("java")
# ob1.display_details()


# Activity 2 — Bank Account
# Create a BankAccount class with:
# • account_holder
# • account_number
# • balance
# Methods:
# • deposit(amount)
# • withdraw(amount)
# • check_balance()
# Rules:
# • Deposit amount must be greater than 0.
# • Withdrawal should not be allowed if the balance is insufficient.
# Task: Create an account, perform multiple deposits and withdrawals, and display the final balance
# class BankAccount:
#     def __init__(self ,account_holder,account_number,balance):
#         self.account_holder = account_holder
#         self.account_number = account_number
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print("Deposited:", amount)
#             print("Current balance:", self.balance)
#         else:
#             print("Deposit amount must be greater than 0.")
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be greater than 0.")
#         elif amount > self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#             print("Current balance:", self.balance)
#     def check_balance(self):
#         print("Current balance:", self.balance)
    

# account = BankAccount("Panchami", "1234567890", 5000)

# account.check_balance()

# account.deposit(2000)
# account.deposit(1500)

# account.withdraw(1000)
# account.withdraw(2500)

# account.withdraw(10000)

# print("\nFinal Account Details:")
# print("Account Holder:", account.account_holder)
# print("Account Number:", account.account_number)
# account.check_balance()


# Activity 3 — Employee Salary System
# Create an Employee class with:
# • name
# • employee_id
# • basic_salary
# Create methods to calculate:
# • HRA = 20% of basic salary
# • DA = 10% of basic salary
# Page 1
# Python OOP — Practical Activity Sheet
# • Gross salary = Basic + HRA + DA
# Task: Create 3 employees and display their salary details.


# Activity 4 — Inheritance: Vehicle System
# Create a parent class Vehicle with:
# brand
# model
# start()
# stop()
# Create two child classes:
# Car
# Bike
# Override the start() method in both classes.
# Task: Create objects of Car and Bike and demonstrate different start() behavior.
# Concepts: Inheritance, Method Overriding


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Vehicle is starting...")

    def stop(self):
        print("Vehicle is stopping...")

class Car(Vehicle):
    def start(self):
        print(self.brand, self.model, "Car is starting with a key.")

class Bike(Vehicle):
    def start(self):
        print(self.brand, self.model, "Bike is starting with a self-start button.")

car1 = Car("Toyota", "Fortuner")
bike1 = Bike("Yamaha", "R15")

print("Car:")
car1.start()
car1.stop()

print("\nBike:")
bike1.start()
bike1.stop()