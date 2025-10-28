''' name = input("What is your name? ")

print(f'Hello', name, '. How are you?')

# we use an f' before the string to get a formatted string
#E.g. f' something {variable} '

msg = f'Hello {name}. How are you?'
print(msg)

# f' strings can be formatted any way you want compare to regular strings
'''
'''
user_number = int(input("Pick a number: "))
print(f'Your number is {user_number}.')

one_larger = user_number + 1
msg = f' {one_larger} is one number larger than yours.'

print(msg)
'''

user_number = int(input("Pick a number: "))
user_number2 = int(input("Pick another number: "))
operator = input("Pick an operator (+, -, *, /): ")


total = user_number + user_number2
sum  = f' {user_number} + {user_number2} = {total}'
print(sum)

import math