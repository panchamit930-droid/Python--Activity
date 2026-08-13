# Create a simple Single Inheritance example (Parent -> Child). 

# class Vehicle:
#     def display_data(self):
#         print("Its a vehicle")
# class Car(Vehicle):
#     def display_data(self):
#         print("CAR")
#         super().display_data()
# ob1= Car()
# ob1.display_data()

# Demonstrate Multilevel Inheritance using Grandparent -> Parent -> Child. 
        
# class Animal:
#     def display_Animal(self):
#         print("Its an animal.")
# class Dog(Animal):
#     def display_Animal(self):
#         print("Its a Dog.")
#         return super().display_Animal()
# class Breed(Dog):
#     def display_Animal(self):
#         print("Breed : Beagle.")
#         return super().display_Animal()
# ob1 = Breed()
# ob1.display_Animal()

# Build a Multiple Inheritance example
# class Employee:
#     def display1(self):
#         print("Works at ABC company.")
# class Student:
#     def display2(self):
#         print("Studied at ABC school.")
# class Person(Student,Employee):
#     def display(self):
#         print("Name : Joy")
# p1 = Person()
# p1.display()
# p1.display1()
# p1.display2()

# Implement Hierarchical Inheritance using a base class Animal → Dog, Cat, Cow

# class Animal:
#     def display_Animal(self):
#         print("Its an animal.")
# class Dog(Animal):
#     def display_Animal(self):
#         print("Dog.")
#         return super().display_Animal()
# class Cat(Animal):
#     def display_Animal(self):
#         print("Cat.")
#         return super().display_Animal()
# class Cow(Animal):
#     def display_Animal(self):
#         print("Cow.")
#         return super().display_Animal()
# ob1 = Dog()
# ob1.display_Animal()
# ob2 = Cat()
# ob2.display_Animal()
# ob3 = Cow()
# ob3.display_Animal()

        