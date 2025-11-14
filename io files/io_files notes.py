
# total = 0
# user_input = input('Enter a number or type done: ')
# while user_input != 'done':
#     user_number = float(user_input)
#     total += user_number
#     user_input = input('Enter a number or type done: ')

# print(f'total = {total}')
    
'''from random import randint
# variable name = open('filename.ext', 'r')

my_file = open('numbers.txt', 'w')

for index in range(0,100):
    number = randint(50, 250)
    my_file.write(f'{number}\n')


other_file = open('numbers.txt', 'r')

my_file.close()'''

'''my_file = open('numbers.txt', 'r')

data = my_file.readlines()
# print(data)

total = 0
count = 0
for line in data:
    number = float(line)
    total += number
    count += 1
    average = (total) / count
print(f'total = {total}')
print(f'average = {average}')'''



new_file = open('family.txt', 'w')

new_file.write('Name,Age,Occupation,Hobby\n')
new_file.write('Matt,39,Teacher,Running\n')
new_file.write('Dexter,8,Student,Ready\n')
new_file.write('Ashley,38,Important Teacher,Learning\n')

new_file.close()

my_file = open('family.txt', 'r')
count = 0
total = 0
data = my_file.readlines()
for line in data[1:]:
    line_data = line.split(',')
    name = line_data[0]
    age = float(line_data[1])
    occupation = line_data[2]
    hobby = line_data[3]
    total += age
    count += 1 

print(f'avg age = {total//count}')