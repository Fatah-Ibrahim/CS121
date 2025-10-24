from random import randint
# Coin Toss

# def coin_toss(input = 0):

#     value = randint(0,1)

#     if input == value: 
#         return 'Correct!'
#     else:
#         return "Incorrect!"
    
# print(coin_toss(1))

#2

# def odd_or_even(guess = 'even'):
#     value = randint(0,9)
    
#     if guess == 'even' and value % 2 == 0:
#         return 'Correct!'
#     elif guess == 'odd' and value % 2 != 0:
#         return 'Correct!'
#     else:
#         return 'Incorrect!'
    
# print(odd_or_even('odd'))

#3 

# def count_dupes(num1 = 0, num2 = 0, num3= 0):
     
#     if num1 == num2 and num2 == num3:
#         return 'There are 3 of the same number'
#     elif num1 == num2 or num1 == num3 or num2 == num3:
#         return 'There are 2 of the same number'
#     else:
#         return 'Each number is unique'
    
# print(count_dupes(0))

#4

def find_winner(player1 = 'Rock', player2 = 'Rock'):

    if player1 == player2:
        return 'Its a tie'

    rules = { 'Rock': 'Scissors',
         'Scissors' : 'Paper',
         'Paper': 'Rock'}
     
    if rules[player1] == player2:
        return 'Player 1 wins'
    else:
        return 'Player 2 wins'


print(find_winner('Scissors','Scissors'))

#5

# def find_relation(name = 'Unknow'):

#     if name == 'Darth Vader':
#         return 'Father'
#     elif name == 'Leia':
#         return 'Sister'
#     elif name == 'Han':
#         return 'Brother in law'
#     elif name == 'R2D2':
#         return 'Droid'
#     else:
#         return 'Unknown'
    
# print(find_relation('Darth Vader'))

#6

# def hailstone_seq(n = 40):

#     result = [n]

#     while n != 1:
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#         result.append(n)
#     return result
    
# print(hailstone_seq(5))
                
#7

# def ascending_order(num1, num2 = 15, num3 = 5):
    
#     if num1 > num2:
#         num1, num2 = num2, num1
#     if num1 > num3:
#         num1, num3 = num3, num1
#     if num2 > num3:
#         num2, num3 = num3, num2
    
#     return [num1,num2,num3]

# print(ascending_order(2,45))
    
#8

# def descending_order(num1,num2 = 15,num3 = 5):

#     if num1 < num2:
#         num1, num2 = num2, num1
#     if num1 < num3:
#         num1, num3 = num3, num1
#     if num2 < num3:
#         num2, num3 = num3, num2
    
#     return [num1, num2, num3]

# print(descending_order(10))

#9 

# def get_indices(lyst, value = 0):

#     result = []
#     for i in range(len(lyst)):
#         if value == lyst[i]:
#             result.append(i)
#     return result

# print(get_indices(['a','a','b','a','b','a'],'a'))

#10

# def find_factors(num = 36):

#     result = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             result.append(i)
#     return result

# print(find_factors(12))


#11 

# def list_of_multiples(num, length = 5):

#     result = []

#     for i in range(1, length + 1):
#         i = num * i
#         result.append(i)
#     return result

# print(list_of_multiples(2))


#12

# def is_even(num):

#     if num % 2 == 0:
#         return True

# def report_even(num_list): 

#     result = []

#     for num in num_list:
#         if is_even(num):
#             result.append(num)
#     return result

# print(report_even([69,3,5,7,9,1]))


#13 

# def is_vowel(letter):
#     return letter in 'aeiou'
        

# def report_vowel(word):
#     result = []
#     for letter in word:
#         if is_vowel(letter):
#             result.append(letter)
#     return result

# print(report_vowel('run time error'))
    

#14 

# def is_two_digit_number(num):
#     return -99 < num < -10 or  10 < num < 99

# def report_is_two_digit_number(num_list):

#     result = []

#     for n in num_list:
#         if is_two_digit_number(n):
#             result.append(n)
#     return result
# print(report_is_two_digit_number([121,1,2,2]))

#15

# def is_odd(num):
#     return num % 2 != 0

# def is_neg(num):
#     return num < 0

# def report_negative_odds(num_list):

#     result = []
#     for n in num_list:
#         if is_neg(n) and is_odd(n):
#             result.append(n)
#     return result
# print(report_negative_odds([121,-101,36,-19,-6,0,21,-1]))