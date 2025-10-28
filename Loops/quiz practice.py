#4
'''
your_age = int(input("Enter your age: "))
your_athleticism_goal = input("Enter your athleticism goal: ")

if your_age >= 20 and your_age <= 39:
    if your_athleticism_goal == 'Below average':
        print("Your resting heart rate should be between 73-93")
if your_age >= 20 and your_age <= 39:
    if your_athleticism_goal == 'Above average':
        print("Your resting heart rate should be between 47 - 71")
if your_age >= 40 and your_age <= 59:
    if your_athleticism_goal == 'Below average':
        print("Your resting heart rate should be between 72-94")
if your_age >= 40 and your_age <= 59:
    if your_athleticism_goal == 'Above average':
        print("Your resting heart rate should be between 46-71")
if your_age >= 60 and your_age <= 79:
    if your_athleticism_goal == 'Below average':
        print("Your resting heart rate should be between 71-97")
if your_age >= 60 and your_age <= 79:
    if your_athleticism_goal == 'Above average':
        print("Your resting heart rate should be between 45-70")
'''
#5 smallest to largest


'''
num1 = int(input())
num2 = int(input()) 
num3 = int(input())

if num1 <= num2 and num1 <= num3
    if num2 <= num3:
        print(num2, num3,num1)
     else: 
    print(num1, num3,num2)
elif num2 <= num1 and num2 <= num3
    if num1 <= num3:
        print(num3, num1,num2)
     else: 
    print(num1, num3,num2)
elif num3 <= num1 and num3 <= num2
    if num1 <= num2:
        print(num2, num1,num3)
     else: 
    print(num1, num2,num3)

'''
# smallest number
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 <= num1 and num2 <= num3:
    print(num2)
else:
    print(num3)
'''

# largest number
'''
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
'''

# question 10

'''
health_points = -1
your_race = input("What is your race: ")
your_class = input("What is your class: ")

if your_race == 'Elf':
    if your_class == "Warrior":
        health_points = 150
    elif your_class == "Bard":
        health_points = 75
    elif your_class == "Wizard":
        health_points = 25
if your_race == 'Ogre':
    if your_class == "Warrior":
        health_points = 200
    elif your_class == "Bard":
        health_points = 100
    elif your_class == "Wizard":
        health_points = 50
print(health_points)

''' 

'''

#Question 11

from random import randint
value = randint(0,1)

coin = input("Heads or Tails: ")

if value == 0:
    print('Heads')
elif value == 1:
    print('Tails')

'''

#Question 12
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

if num1 == num2:
    print("You have entered the same number twice.")
elif num1 == num3:
    print("You have entered the same number twice.")
elif num1 != num3 and num2:
    print("Each number is unique.")
elif num2 == num1:
    print("You have entered the same number twice.")
elif num2 == num3:
    print("You have entered the same number twice.")
elif num2 != num1 and num3:
    print("Each number is unique.")
elif num3 == num1:
    print("You have entered the same number twice.")
elif num3 == num2:
    print("You have entered the same number twice.")
elif num3 != num1 and num2:
    print("Each number is unique.")
'''

#18
'''
triangle_side1 = int(input("Enter the length of the side: "))
triangle_side2 = int(input("Enter the length of the side: "))
triangle_side3 = int(input("Enter the length of the side: "))

if triangle_side1 == triangle_side2 and triangle_side1 == triangle_side3:
    print("Equilateral Triangle")
elif triangle_side1 == triangle_side2 and triangle_side1 != triangle_side3:
    print("Isoceles Triangle")
elif triangle_side1 != triangle_side2 and triangle_side1 == triangle_side3:
    print("Isoceles Triangle")
elif triangle_side2 == triangle_side1 and triangle_side2 == triangle_side3:
    print("Equilateral Triangle")
elif triangle_side2 == triangle_side1 and triangle_side2 != triangle_side3:
    print("Isoceles Triangle")
elif triangle_side2 != triangle_side1 and triangle_side2 == triangle_side3:
    print("Isoceles Triangle")
elif triangle_side3 == triangle_side1 and triangle_side3 == triangle_side2:
    print("Equilateral Triangle")
elif triangle_side3 == triangle_side1 and triangle_side3 != triangle_side2:
    print("Isoceles Triangle")
elif triangle_side3 != triangle_side1 and triangle_side3 == triangle_side2:
    print("Isoceles Triangle")
    
'''

#7

Knuts = int(input("How many Knuts do you have?: "))

# 29 knuts = 1 Sickle
# 17 Sickle = 1 Galleon 

sickles = Knuts // 29
