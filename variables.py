# Create a Student class with instance and static variables. 
# class Student:
#     college = "ABC college"
#     def __init__(self,name, grade):
#         self.name = name
#         self.grade = grade
#     def show_grade(self):
#         print(f"Student name : {self.name} , Grade : {self.grade}")
# s1 = Student("Anu" , "A")
# s1.show_grade()
# print(s1.college)
        

# Demonstrate instance methods vs class methods. 
# instance method
# class Student:
#     def __init__(self,name, grade):
#         self.name = name
#         self.grade = grade
#     def show_grade(self):
#         print(f"Student name : {self.name} , Grade : {self.grade}")
# s1 = Student("Anu" , "A")
# s1.show_grade()
# class method
# class Student:
#     college = "ABC college"
#     def __init__(self,name, grade):
#         self.name = name
#         self.grade = grade
#     def show_grade(self):
#         print(f"Student name : {self.name} , Grade : {self.grade}")
#     def show_college(cls):
#         print(f"Collge : {cls.college}")
# s1 = Student("Anu" , "A")
# s1.show_grade()
# s1.show_college()


#  Add a static method to validate data.


# 1. Create a class Employee containing: 
# a. instance variables (name, salary) 
# b. static variable (company) 
# c. class method to change company 
# d. static method to check valid salary 
# e. Create objects and test all methods.
# class Employee:
#     company= "ABC company"
    
#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary
#     @classmethod
#     def change_Company(cls):
        