# list and tuple
# activity 1 : Add a New Fruit (List)
fruits=['Apple','Banana','Mango']
new_fruit = input("Enter a fruit :")
fruits.append(new_fruit)
print(fruits)

# Activity 2: Remove a Subject 
subjects=['Python','Java','C++','JavaScript'] 
remove_subject=input('Enter subject to remove: ') 
subjects.remove(remove_subject)
print(subjects)

# Activity 3: Find Student Position
students=['Asha','Rahul','Meera','John'] 
student_name=input('Enter student name: ')
print(students.index(student_name))

# Activity 4: Count a Number
numbers=[10,20,10,30,10,40] 
find_number=int(input('Enter number: '))
print(numbers.count(find_number))

# Activity 5: Sort Marks
marks=[65,82,40,95,70]
marks.sort()
print("Sorted Marks:",marks)

# Activity 6: Reverse a List
colors=['Red','Blue','Green','Yellow']
colors.reverse()
print(colors)

# Activity 7: Update a List Item
cities=['Delhi','Mumbai','Chennai']
index=int(input()) 
new_city=input()
cities.pop(index)
cities.insert(index , new_city)
print(cities)

# Activity 8: Create a Tuple
name=input(); 
age=int(input()); 
student=(name,age)
print(student)

# Activity 9: Access Tuple Elements
employee=('John',28,'Developer')
name = employee[0]
age = employee[1]
role = employee[2]
print('Name :' , name , 'Age :' , age , 'Role :', role)

# Activity 10: Count Item in Tuple
numbers=(1,2,3,2,4,2) 
find_value=int(input())
print(find_value, "appears", numbers.count(find_value), 'times')

# Activity 11: Find Index in Tuple
languages=('Python','Java','C','JavaScript')
lang = input("Enter language :")
print(lang , "is at", languages.index(lang))

# Activity 12: Convert Tuple to List
numbers=(10,20,30,40)
print(list(numbers))

# Activity 13: List + Tuple
subjects=['Python','Java'] 
new_subjects=('React','Django')
new_list = list(new_subjects)
subjects.extend(new_list)
print(subjects)

# Activity 14: Maximum & Minimum
marks=[75,82,90,65,88]
print("Highest :", max(marks) , "Lowest :", min(marks))

# Activity 15: List Methods Practice
numbers=[5,10,15]
numbers.remove(10)
numbers.append(20)
numbers.append(7)
numbers.sort(reverse=True)
print(numbers)