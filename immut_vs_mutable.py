# Mutable vs Immutable Objects in Python

# Immutable Objects
# ----------------
# Immutable objects cannot be changed after creation.
# Examples: int, float, string, tuple, frozenset

print("Immutable Objects")

x = 10
print(f"ID of x before modification: {id(x)}")
x = x + 1  # A new integer object is created
print(f"ID of x after modification: {id(x)}")  # Different ID

s = "hello"
print(f"ID of s before modification: {id(s)}")
s = s + " world"  # A new string object is created
print(f"ID of s after modification: {id(s)}")  # Different ID

# Behind the scenes:
# When an immutable object is modified, Python creates a new object
# instead of modifying the original one.

print("\nMutable Objects")

# Mutable Objects
# ---------------
# Mutable objects can be changed after creation.
# Examples: list, dict, set

lst = [1, 2, 3]
print(f"ID of lst before modification: {id(lst)}")
lst.append(4)  # The same list object is modified
print(f"ID of lst after modification: {id(lst)}")  # Same ID

# Dictionary Example
my_dict = {"a": 1, "b": 2}
print(f"ID of my_dict before modification: {id(my_dict)}")
my_dict["c"] = 3  # Dictionary is modified in place
print(f"ID of my_dict after modification: {id(my_dict)}")  # Same ID

# Behind the scenes:
# Mutable objects can be modified in place, meaning the ID remains the same.

# Key Takeaways:
# - Immutable objects create a new instance when modified.
# - Mutable objects modify the same instance in place.
# - Be cautious with mutable objects in function calls and default parameters!

def modify_list(lst):
    lst.append(99)
    return lst

original_list = [1, 2, 3]
modified_list = modify_list(original_list)
print(f"Original List after function call: {original_list}")  # [1, 2, 3, 99]

# Since lists are mutable, the function modifies the original list,
# which might lead to unexpected behavior if not handled carefully.
