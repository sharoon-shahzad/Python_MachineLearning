# Age group Categorization

age = 22

if age < 13:
    print("underAge")
elif age <= 22:
    print('teenager')
elif age < 60:
    print('adult')
else:
    print('Senior')

# Movie Ticket Pricing
# problem Movie tickects are priced on age : $12 for adults (18 and over), $7 for teenagers (13-17), and $5 for children (12 and under). Write a program that asks the user their age and then prints the price of their movie ticket.EveryOne gets the $2 discount on the wednesday

age = 22
day = "wednesday"

price = 12 if age>=18 and day != "wednesday" else 7 if age>=13 and day != "wednesday" else 5

if day == "wednesday":
    price -= 2

print(price)
# other solution
age = 22
day = "wednesday"
if age >=18 and day != "wednesday":
    price = 12
elif age >=13 and day != "wednesday":
    price = 7
else:
    price = 5

if day == "wednesday":
    price -= 2

print(price)


# Grading problem
score = 90

if score >= 101:
    print("Invalid score")
    exit()

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(grade)

#Ripeness Checker

fruit = "banana"
color = 'green'

if fruit == "banana" and color == "green":
    print("Unripe")
elif fruit == "banana":
    if color == "yellow":
        print("Ripe")
elif fruit == "banana" and color == "brown":
    print("Overripe")
else:
    print("Invalid fruit or color")


# Suggest activit based on the weather
weather = "snowy"

if weather == "snowy":
    print("Go skiing")
elif weather == "rainy":
    print("Go hiking")
elif weather == "sunny":
    print("Go to the beach")
else:
    print("Stay home")

# coffee Customization

coffee = "espresso"
coffeeOrder = ""
extraShot = False

if coffee == "espresso":
    if coffeeOrder == "small":
        print("coffee ")
    elif coffeeOrder == "medium":
        print("coffee ordered placed")
    elif coffeeOrder == "large":
        print("coffee")
    else:
        if extraShot:
            print("coffee with extra shot")
else:
    print("Invalid coffee type")


# password checker
password = "secured@Nasa.com"
pass_lengt= len(password)

if pass_lengt < 6:
    print("Password is too short")
elif pass_lengt > 20:
    print("Password is too long")
else:
    print("Password is valid")



# Leap Year