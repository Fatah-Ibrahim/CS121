#count the amount of letters
'''
word = 'Hello World'

counter = 0

for letter in word:
    if letter != ' ':
        counter += 1
print(counter)
'''

# count the amount vowels
'''
Word1 = "Hello World"
Word2 = "Apples and Bananas"
Word3 = "Happy Times"

count1 = 0
count2 = 0
count3 = 0


for letter in (Word1):
    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        count1 += 1
for letter in (Word2):
    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        count2+= 1
for letter in (Word3):
    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        count3 += 1


print(f' The amount of vowels in {Word1} is {count1}')
print(f' The amount of vowels in {Word2} is {count2}')
print(f' The amount of vowels in {Word3} is {count3}')
'''


Word1 = "Hello World"
Word2 = "Apples and Bananas"
Word3 = "Happy Times"


def vowels_counter(passed_word):
    count = 0 
    for letter in passed_word:
        if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            count += 1
    print(f' The amount of vowels in {passed_word} is {count}')

vowels_counter(Word1)
#Thurdays class

def operations(number):
    number += 2
    number *= 4
    return number
# to given something back we use the keyword return

# call the function 10 times and 100 times

result = 10
for number in range(0,10):
    result = operations(result)
print(result)

# write a function that returns and product of two arguements

def product(num1, num2):
    product = num1 * num2
    return product
print(product(4,3))