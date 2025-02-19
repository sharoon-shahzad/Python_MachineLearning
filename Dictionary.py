

chai = {"Masala":"Spicy" , "Ginger":"Zesty" , "Green":"Mild"}

#  accessing the values of the dictionary chai
print(chai["Masala"])

# changing dictionaries items
chai["Green"] = "fresh"

# adding new items to the dictionary
chai["Black"] = "Strong"

# looping through the dictionary
for key, value in chai.items():
    print(key, value)

# looping through the keys of the dictionary
for key in chai.keys():
    print(key)

# looping through the values of the dictionary
for value in chai.values():
    print(value)

# checking if a key is in the dictionary
if "Masala" in chai:
    print("Yes, Masala chai  is in the dictionary")


# checking the length of the dictionary
print(len(chai))

# removing an item from the dictionary
chai.pop("Green")

# deleting  an item from the dictionary
del chai["Black"]

# dictionaries in dictionaries
tea_shop ={
    "chai": {"Masala":"Spicy" , "Ginger":"Zesty" , "Green":"Mild"},
    "coffee": {"Black":"Strong" , "White":"Mild" , "Latte":"Creamy"}
}
print(tea_shop["chai"]["Masala"]) 



# Python Dictionaries - Key-Value Data Storage

# 1. Creating a Dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

person = dict(name="Bob", age=25, city="New York")
print(student)
print(person)

# 2. Accessing Dictionary Elements
print(student["name"])  # Alice
print(student.get("age"))  # 21
print(student.get("GPA", "Not available"))  # Not available

# 3. Adding and Updating Values
student["GPA"] = 3.9  # Add new key-value pair
student["age"] = 22   # Update existing key
print(student)

# 4. Removing Items
del student["major"]  # Remove key-value pair
print(student)

gpa = student.pop("GPA", "Not found")  # Safe removal
print(gpa)

student.clear()  # Clears dictionary
print(student)

# 5. Iterating Over a Dictionary
student = {"name": "Alice", "age": 21, "major": "CS"}
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f"{key}: {value}")

# 6. Dictionary Methods
print(student.keys())
print(student.values())
print(student.items())

# 7. Nested Dictionaries
students = {
    "Alice": {"age": 21, "major": "CS"},
    "Bob": {"age": 23, "major": "Math"}
}
print(students["Alice"]["major"])

# 8. Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)

# 9. Checking Key Existence
if "name" in student:
    print("Key exists!")
