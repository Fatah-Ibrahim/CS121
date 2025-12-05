
#1

# while True:
#     try:
#         user_input = input('Enter a number: ')
#         result = 10/int(user_input)
#         print(result)
#         break
#     except ValueError:
#             print('Please enter a vaild number.')
#     except ZeroDivisionError:
#             print("Cannot be divided by zero.")

#2 

# fruits = ['apple', 'banana', 'cherry','date']
# user_input = input("Enter a index number: ")

# try:
#     index = int(user_input)
#     print(fruits[index])
# except ValueError:
#     print('Invaild index format')
# except IndexError:
#     print('Index out of range')

#3 

# products = {'apple': 1.5, 'banana': 0.9, 'cherry': 2.2}
# user_input = input('Enter name of product: ')

# if not user_input.strip():
#         print('Please enter a product name.')
# else:
#     try:
#         print(products[user_input])
#     except KeyError:
#         print('Product not found.')

#4 

# user_input = input('Enter the file name: ')

# try:
#     with open(user_input, 'r') as f:
#         print(f.read())

# except FileNotFoundError: 
#     print('File not found.') 

#5

# dict = {'Alice': 90, 'Bob': 75, 'Charlie': 60}

# user_name = input('Enter student name: ')
# user_num = input('Enter number to add: ')

# try:
#     dict[user_name] += int(user_num)
#     print(dict[user_name])
# except KeyError:
#     print('Student not found.')
# except ValueError:
#     print('Invalid Number')

#6

# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# try:
#     user_input = int(input('Enter a number (0-6): '))
#     print(days[(user_input)])
# except ValueError:
#     print("Invalid input.")
# except IndexError:
#     print('Index out of range.')

#7 


# try:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     print(f'Difference: {num1 - num2}, Ratio: {num1/num2}')
# except ValueError:
#     print('Invalid input.')
# except ZeroDivisionError:
#     print('Cannot divide by zero.')
# except OverflowError:
#     print('Result too large.')

#8

# colors = ['red', 'green', 'blue', 'yellow', 'purple']

# while True:
#     try:
#         user_input = input('Enter an index: ')
#         print(colors[int(user_input)])
#         break
#     except ValueError:
#         print('Invalid input. Try again.')
#     except IndexError:
#         print('Index out of range. Try again.')

# 9

# countries = {'US': 'United States', 'FR': 'France', 'JP': 'Japan', 'BR': 'Brazil' }

# while True:
#     try:
#         user_input = input('Enter a country code: ')
#         print(countries[user_input])
#         break
#     except KeyError:
#         print('Code not found. Try again.')

#10
# while True:
#     try:
#         prize_amount = int(input('Enter the prize amount in dollars: '))
#         winners = int(input('Enter the number of winners: '))
#         print(prize_amount/winners)
#         break
#     except ValueError:
#         print('Invalid input. Try again.')
#     except ZeroDivisionError:
#         print('Must have one winner. Try again')


