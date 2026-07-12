# Level 1 – Basic
# numbers = [10, 20, 30, 40, 50]
# # Print the first element. 
# print(numbers[0])
# # Print the last element. 
# print(numbers[4])
# # Print the third element. 
# print(numbers[2])
# # Print the first three elements. 
# print(numbers[0 : 3])
# # Print the last two elements. 
# print(numbers[-2:-1])
# # Reverse the list using slicing. 
# print(numbers[::-1])
# # Find the length of the list. 
# print(len(numbers))
# # Find the maximum number. 
# print(max(numbers))
# # Find the minimum number. 
# print(min(numbers))
# # Find the sum of all numbers.
# print(sum(numbers))

# Level 2 – List Methods
# fruits = ["Apple", "Banana", "Orange"]
# Add "Mango" to the end. 
# fruits.append("Mango")
# print(fruits)
# # Insert "Grapes" at index 1. 
# fruits.insert(1,"Grapes")
# print(fruits)
# # Remove "Banana". 
# fruits.remove("Banana")
# print(fruits)
# # Remove the last item. 
# fruits.pop()
# print(fruits)
# # Remove the item at index 0. 
# fruits.pop(0)
# print(fruits)
# # Clear the entire list. 
# fruits.clear()
# print(fruits)
# Find the index of "Orange".
# print(fruits.index("Orange"))

# Count how many times "Apple" appears.
fruits = ["Apple", "Banana", "Apple", "Orange"]
print(fruits.count("Apple"))


# Sort the numbers.
num = [45, 10, 78, 22, 5]
num.sort()
print(num)

# Sort in descending order.
num.sort(reverse=True)
print(num)

# Level 3 – Slicing

# numbers = [1,2,3,4,5,6,7,8]
# # Print every second element. 
# print(numbers[1:8:2])
# # Print elements from index 2 to 5. 
# print(numbers[2:6])
# # Print every third element.
# print(numbers[2:8:3])
# # Print all elements except the first. 
# print(numbers[1:8])
# # Print all elements except the last.
# print(numbers[0:7])




# Level 4 – Operators

# Join two lists.
list1=[1,2,3] 
list2=[4,5,6]
new_list = list1 + list2
print(new_list)

# Repeat the list three times.
colors=["Red","Blue"]
print(colors * 3)

languages=["Java","Python","C++"]
# Check whether "Python" exists. 
print('Python' in languages)
# Check whether "PHP" does not exist. 
print("PHP" not in languages)
# Find the length after joining two lists.
print(len(colors + languages))

# Level 5 – Logical Thinking
# Without changing the original list, create a reversed copy.
num_list = [2,3,6,9,4,8,1]
reversed_list = num_list[::-1]
print(reversed_list)

# Find the difference between the maximum and minimum value.
diff = max(num_list) - min(num_list)
print(diff)

# Find the average.
numbers=[10,20,30,40,50]
avg = sum(numbers) / len(numbers)
print(avg)

# Create a new list containing the first and last elements only.
# new_numList = 

# Duplicate the list.
# print(numbers * 2)

# Replace the last element with 100.
# numbers[-1] = 100
# print(numbers)

# Replace the first element with 0.
# numbers[0] = 0
# print(numbers)

# Create a copy of a list. 
copy_list = numbers.copy()
print(copy_list)

# Find the second largest number after sorting. 
numbers.sort()
print(numbers[-2])

# Find the second smallest number after sorting.
print(numbers[1])

# Challenge Questions

# Find the middle element.


# Swap the first and last elements using indexing.
l = numbers[0]
numbers[0] = numbers[-1]
numbers[-1] = l
print(numbers)


