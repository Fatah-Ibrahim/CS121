# write function the returns a dictonary of how may time each letter appears

# my_word = "peter pepper picked a peck of pickled peppers"

# def letter_counter(word):
#     letter_dictionary = {}
#     count = 0 
#     for letter in word:
#         if letter in letter_dictionary:
#             letter_dictionary[letter] = letter_dictionary[letter] + 1
#         else:
#             letter_dictionary[letter] = 1
    
#     return letter_dictionary

# my_word = "peter piper picked a peck of pickled pepprs"
# # print(letter_counter(my_word))

# letter_dict = letter_counter(my_word)

# for letter in letter_dict:
#     print(letter, letter_dict[letter])
# # result...
# # d = ('p': 9, 'e':???)


# def add_three(x):
#     y = x + 3
#     return y

# var0 = 7
# var1 = add_three(var0)



smaller_num = int(input('Enter a number: '))
larger_num = int(input('Enter a number bigger than the last: '))
result = []
for n in range(smaller_num, larger_num + 1):
         if n % 2 == 0:
             result.append(n)
print(result) 