
# total = 0
# user_input = input('Enter a number or type done: ')
# while user_input != 'done':
#     user_number = float(user_input)
#     total += user_number
#     user_input = input('Enter a number or type done: ')

# print(f'total = {total}')
    
from random import randint
# variable name = open('filename.ext', 'r')

my_file = open('numbers.txt', 'w')

for index in range(0,100):
    number = randint(50, 250)
    my_file.write(f'{number}\n')


other_file = open('numbers.txt', 'r')

my_file.close()