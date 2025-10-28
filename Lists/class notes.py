
#lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

'''
print(x[2])
print(x[1:4])

for element in lyst:
    print(element)
'''



# How to add to a string
'''
word = 'appl'
print(word)   
word += 'e'
print(word)
'''

# How to add to a lyst
'''
print(lyst)
lyst.append('Saturday')
lyst.append('Sunday')
print(lyst)
'''
# Slicing Certain parts of a list. first [] is the thing. second [] is the amount.

'''
print(lyst[2][3:6])
'''

# Changing the element inside the varible

'''
print(lyst)
lyst[4] = 'Funday'
print(lyst)

word = 'apfle'
print(word)

word[2] = 'p'
print(word)
'''


#Mutable object []

'''
x = lyst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
y = x

print(x)
print(y)

x[4] = 'Funday'
print(x)
print(y)
'''

#Immutable object ()

'''workdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
x = workdays
y = x

print(x)
print(y)

x[4] = 'Funday'
print(x)
print(y)
'''

# # Write a function that takes a string as an arguement, and returns a list 
# # containing all the worlds in that string
my_word = 'Peter piper picked a peck of pickle peppers'
# def string_to_lyst(word):
#     words = []
# #collect a word
#     built_word = ''
#     for letter in word:
#         if letter == ' ':
#             #add built_word into the list
#             words.append(built_word)
#             built_word = ''
#     #Once we have a full word, lets add it to the list of words
#         else:
#             built_word += letter
#     words.append(built_word)
#     return words


# print(string_to_lyst(my_word))



# def string_to_list_alt(word):
#     words = []
#     built_word = ''
#     for index in range(len(word)):
#         if word[index] == ' ': 
#             words.append(built_word)
#             built_word = ''
#         elif  index == len(word)-1:
#             built_word += word[index]
#             words.append(built_word)
#         else: 
#             built_word += word[index] 
#     return words

# print(string_to_list_alt(my_word))



# def string_to_lyst(word):
#     words = []
# #collect a word
#     built_word = ''
#     vowel_count = 0
#     for letter in word:
#         if letter == ' ':
#             if vowel_count >= 2:
#             #add built_word into the list
#                 words.append(built_word)
#             built_word = '' 
#             vowel_count = 0
#     #Once we have a full word, lets add it to the list of words
#         else:
#             built_word += letter
#             if letter in 'aeiou':
#               vowel_count +=1
#     if vowel_count >= 2:
#         words.append(built_word)
#     return words


# print(string_to_lyst(my_word))



phonebook = {'matt': 5073891438, 'ashley': 12345 }

# print(phonebook)

# # to add to a dictionary, we use name_of_dict { key } = value

phonebook['waters'] = 789
print(phonebook)

# # to look up a value in a dictionary, use name_of_dict {key}

# print(phonebook['matt'])

for person in phonebook:
    print(person, phonebook[person])






# write a function that takes a string as an argument and returns a dictionary
# all of the number of times each word was used

# def string_to_dictionary(word):
#     string_as_list = word.split()
#     word_dictionary = []
#     for word in string_as_list:
#         if word in word_dictionary:
#             word_dictionary[word] = word_dictionary[word] + 1
#         else:
#             word_dictionary[word] = 1
