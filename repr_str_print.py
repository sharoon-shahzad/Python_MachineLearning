# Difference Between repr(), str(), and print() in Python

class Example:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Example(value={self.value})"  # Formal string representation
    
    def __str__(self):
        return f"Example with value: {self.value}"  # Human-readable string

# Creating an instance
obj = Example(42)

# Using repr()
print("Using repr():")
print(repr(obj))  # Calls __repr__()

# Using str()
print("\nUsing str():")
print(str(obj))  # Calls __str__()

# Using print()
print("\nUsing print():")
print(obj)  # Calls __str__() implicitly

# Key Differences:
# - repr() is meant for debugging and development, giving an unambiguous representation.
# - str() is meant for user-friendly output.
# - print() internally calls str() by default.

# Example without __str__()
class WithoutStr:
    def __repr__(self):
        return "WithoutStr Object"

obj2 = WithoutStr()
print("\nWithout __str__():")
print(obj2)  # Falls back to __repr__()

# Example without __repr__()
class WithoutRepr:
    def __str__(self):
        return "WithoutRepr Object"

obj3 = WithoutRepr()
print("\nWithout __repr__():")
print(repr(obj3))  # Falls back to default object representation
