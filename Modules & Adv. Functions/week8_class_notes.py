
# total = 0
# user_number = input("Enter a number or type q to end: ")

# while user_number != 'q':
#     total += int(user_number)
#     user_number = input("Enter a number or type q to end: ")

# print(f'total = {total}')



# def letter_counter(word):
#     letter_dictionary = {}
#     count = 0 
#     for letter in word:
#         if letter in letter_dictionary:
#             letter_dictionary[letter] = letter_dictionary[letter] + 1
#         else:
#             letter_dictionary[letter] = 1
#     return letter_dictionary

# my_word = "peter piper picked a peck of pickled peppers"

# letter_dict = letter_counter(my_word)

# print(letter_counter(my_word))


# Store a list of words of all words with 2 or more vowels
def string_to_list_with_vowels(word):
    words = []
    #collect a word
    built_word = ' '
    vowel_count = 0

    for letter in word:
        if letter == ' ':
            words.append(built_word)
        elif vowel_count == 2:
            built_word = ' '
        else:
            built_word += letter
            if letter in 'aeiou':
                vowel_count =+ 1
    return words

my_word = 'peter piper picked a peck of pickled peppers'

print(string_to_list_with_vowels(my_word))