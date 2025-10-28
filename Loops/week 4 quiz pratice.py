# 1
'''
larger_num = int(input("Enter a large number: "))
smaller_num = int(input("Enter a smaller number: "))


count = 0

while larger_num/2  > smaller_num:
        larger_num = larger_num / 2
        count +=1 
print(count)
'''
#2
'''
user_word = input("Enter a word: ")

for letter in range(1, len(user_word), 2):
    print(user_word[1:len(user_word):2])
'''

#3
'''
for number in range (37, 1051):
    if number % 2 == 0:
        print(number)
'''
#4
'''
letter = ""
word = ""

while letter != "done":
    word += letter
    letter = input("Enter a letter (or type done): ")
print(word)
'''
#5
'''
total = 0
for number in range(50, 518):
    if number % 2 != 0:
        total += number
print(total)
'''
#6
'''
user_int = user_int = int(input("Enter an interger: "))

total = 0 

while user_int > 0:
    total += user_int
    user_int = int(input("Enter an interger: "))
print(total)
'''
#7
'''
number = int(input("Enter a number: "))
while number != 1:
    if number % 2 == 0:
        number = number // 2 
    elif number % 2 == 1:
        number = 3 * number + 1
    print(number)
'''
#8



#13

# width = int(input())
# length = int(input())
# pattern = input()

# for i in range(length):
#     print(width * pattern)


