students = {}

# Add student
def add_student():
    student_id = input("Enter Student ID :")
    
    if student_id in students:
        print("Student id alraedy exist!")
        return
    
    student_name = input("Enter Student name :")
    
    try:
        age = int(input("Enter age :"))
    except ValueError:
        print("Enter a valid age!")
        
    course = input("Enter Course :")
    email = input("Enter email :")
    
    students[student_id] = {
        "Student id" : student_id,
        "Student name" : student_name,
        "age" : age,
        "course" : course,
        "email" : email
    }
    
    print("Student added successfully!")
    
def display_student():
    if not students:
        print("No student records found!")
        return
    
    print("\n===== Student details =====")
    
    for student in students.values():
        print("Student id :", student["Student id"])
        print("Student name :", student["Student name"])
        print("Age :", student["age"])
        print("Course :", student["course"])
        print("Email :", student["email"])
        
def search_student():
    student_id = input("Enter student id:")
    
    if student_id in students:
        student = students[student_id]
        
        print("====Student====")
        print("Student id :", student["Student id"])
        print("Student name :", student["Student name"])
        print("Age :", student["age"])
        print("Course :", student["course"])
        print("Email :", student["email"])
    else:
        print("No student found!")
        
def delete_student():
    student_id = input("Enter student id:")
    
    if student_id in students:
        del students[student_id]
        print("Student deleted!")
    else:
        print("Student not found!")
        
while True:
    print("===student management system===")
    print("1. Add student")
    print("2. Display all student")
    print("3. Search student")
    print("4. Delete student")
    print("5. Exit")
    
    choice = int(input("Select your choice:"))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        display_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Thankyou")
        break
    else:
        print("Invalid choice!")
    
        