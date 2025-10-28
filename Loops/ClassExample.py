# while loop

'''
#print the numbers 1 through 10
number = 1 
while number <= 10:
    print(number)
    number += 1
'''
'''
number = 1
while number <= 10:
    print(number)
    number *= 2
'''

'''
number = 1 
while number <= 10:
    if number % 2 == 0: 
        print(number)
    number += 1
'''

#print all odd numbers betwwen 5 and some number even by user


'''
basenum= 5
number = int(input("Enter a number: "))


while basenum <= number :
    if number % 2 == 1:
        print(number)
    basenum += 1
'''

'''
number = 0

while number < 50:
    number += 1
    if number % 2 == 0:
        if number % 3 == 0:
            continue
        print(number)
    number += 1
'''

#write a program that prints number until user says stop
'''
total = 0

user_number = (input("Enter a number or type q to end: "))

while user_number != 'q':
    total += int(user_number)
    user_number = (input("Enter a number or type q to end: "))

print(f' total = {total}')
'''


# for loops

#example 1



'''
for number in range(1,10+1):
    print(number)
'''

'''
for number in range (1,10+1):
    if number % 2 == 0:
        print(number)
'''

'''
user_num = int(input("Pick a number: "))
for number in range (5,user_num):
    if number % 2 == 1:
        print(number)
'''



#write a program that prints number until user says stop
'''
total = 0

user_number = (input("Enter a number or type q to end: "))

while user_number != 'q':
    total += int(user_number)
    user_number = (input("Enter a number or type q to end: "))

print(f' total = {total}')
'''
'''

total = 0

user_num = int(input("Enter a number or type q to end: "))
for number in range (0,user_num):
    if user_num != 'q':
        total += int(user_num)
        user_number = (input("Enter a number or type q to end: "))
print(number)
'''


'''
# Index Syntax
x = "Hello World"
print(x[8])

#Grouping Syntax
#String Slicing

x = "Hello World"
print(x[2:8])
'''
'''
word = "Hello World"

for letter in word: 
    print(letter)
'''


'''
x = 123
for number in x:
    print(number)
'''