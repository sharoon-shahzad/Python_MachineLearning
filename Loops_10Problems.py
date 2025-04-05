
# # counting the positive numbers
# numbers = [ 1, 2, 3, -4, -5, 6, -7, -8, 9, 10]

# for i in numbers:
#     if i > 0:
#         print(i)

# # sum of even numbers upto to given number n

# n = 10
# sum_even = 0

# for i in range(0,n+1):
#     if i % 2 == 0:
#         sum_even += i
    
# print(sum_even)

# # multiplication table skipping the fifth iteration

# n = 10
# for i in range(0,n+1):
#     if i == 5:
#         continue
#     print(i*5)

# # reverse String

# _str = "sharoon"
# reversed_str = ""

# for char in _str:
#     reversed_str = char + reversed_str

# print(reversed_str)

# # Find first non repeated Character

# var  = "sharoon"

# for char in var:
#     if(var.count(char) == 1):
#         print(char)
#         break
# print(char)


# # factorial using while loop

# n = 5
# factorial = 1

# while n > 0:
#     factorial *= n
#     n -= 1

# print('factorial of number is:', factorial)


# # validate the input 

# while True:
#     number = int(input('Enter value btw  1 and 10:'))
#     if 1 <= number <=10:
#         print("valid number")
#         break
#     else:
#         print("invalid number")
#         print("try again")


# checking the prime number
# import math
# number = 25

# if number > 1:
#     for i in range(2, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             print(f"{number} is divisible by {i}")
#             break
#     else:
#         print(f"{number} is a prime number")


# # List uniqueness checker 
# items = ["apple","banana" , "orange","apple"]
# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate Iitem is :" , item)
#         break
#     unique_item.add(item)
     


# exponential backoff 
import time

# algo: set the expo backoff time to 1 sec 
# if password on the first go matches it provides the access 
# if user fails and retries : backoff time will increase to (backofftime) to power 2
#after 5 retries it locks the account of user

backofftime = 1
total_tries = 2
attempts =0
checkpass = "hello"
while attempts < total_tries:
    print("Attempts", attempts+1)
    print("Wait time" , backofftime)
    password = input("Enter your password")
    if password == checkpass:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        attempts += 1
        backofftime *= 2
        time.sleep(backofftime)

if attempts > total_tries:
    print("Account locked")