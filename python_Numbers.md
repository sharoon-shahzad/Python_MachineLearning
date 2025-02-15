# Python Numbers: A Comprehensive Guide

## Introduction
Numbers are fundamental in Python programming. Python supports various numerical types, including integers, floating-point numbers, complex numbers, and more. This guide covers Python numbers from beginner to advanced levels, including concepts useful for AI/ML engineers.

---

## 1. Integer (`int`)
### 🔹 Basics
- Whole numbers, positive or negative.
- No decimal points.

```python
x = 10
print(type(x))  # <class 'int'>
```

### 🔹 Operations
```python
print(5 + 3)   # Addition -> 8
print(5 - 3)   # Subtraction -> 2
print(5 * 3)   # Multiplication -> 15
print(5 // 2)  # Floor Division -> 2
print(5 % 2)   # Modulus -> 1
print(5 ** 3)  # Exponentiation -> 125
```

### 🔹 Special Cases
- Large integers (Python supports arbitrary precision)
- Binary, Octal, and Hexadecimal representation

```python
binary = 0b1010  # 10 in decimal
hexadecimal = 0x1A  # 26 in decimal
octal = 0o12  # 10 in decimal
```

---

## 2. Floating-Point Numbers (`float`)
### 🔹 Basics
- Numbers with decimals.
- Can represent very large or very small values.

```python
x = 10.5
print(type(x))  # <class 'float'>
```

### 🔹 Operations
```python
print(5.5 + 2.2)   # 7.7
print(5.5 * 2)     # 11.0
print(10 / 4)      # 2.5 (division always returns float)
```

### 🔹 Special Cases
- Scientific notation (`e` or `E` for exponentiation)

```python
x = 1.2e3  # 1.2 * 10^3 -> 1200.0
```
- Precision issues due to floating-point arithmetic

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

---

## 3. Complex Numbers (`complex`)
### 🔹 Basics
- Represented as `a + bj`, where `j` is the imaginary unit.

```python
z = 3 + 4j
print(z.real)  # 3.0
print(z.imag)  # 4.0
```

### 🔹 Operations
```python
a = 1 + 2j
b = 2 + 3j
print(a + b)  # (3+5j)
print(a * b)  # (-4+7j)
```

---

## 4. Type Conversion
### 🔹 Converting Between Types
```python
print(int(10.9))  # 10
print(float(10))  # 10.0
print(complex(10))  # (10+0j)
```

---

## 5. Advanced Numerical Operations
### 🔹 Using `math` Module
Python’s `math` module provides advanced mathematical operations.

```python
import math
print(math.sqrt(25))  # 5.0
print(math.pi)        # 3.141592653589793
print(math.sin(math.radians(90)))  # 1.0
```

### 🔹 Using `random` Module
For generating random numbers.

```python
import random
print(random.randint(1, 100))  # Random integer between 1 and 100
print(random.uniform(1.5, 5.5))  # Random float in range
```

---

## 6. Numbers in AI & ML
### 🔹 Handling Large Numbers with `numpy`
```python
import numpy as np
arr = np.array([1.2, 3.4, 5.6])
print(arr.mean())  # 3.4 (computing mean)
```

### 🔹 Floating-Point Precision in ML
```python
np.set_printoptions(precision=3)
data = np.array([0.12345678, 0.987654321])
print(data)  # [0.123 0.988]
```

---

## Conclusion
- **Integers** are used for counting and indexing.
- **Floats** handle precision-based calculations.
- **Complex numbers** help in scientific computing.
- **Advanced operations** use `math`, `random`, and `numpy` for AI/ML applications.

Understanding numbers in Python is crucial for writing efficient and scalable code, especially in data science and machine learning! 🚀
