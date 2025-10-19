# def EDE(user_num):
#     count = 0
#     for n in range(1, user_num +1):
#         count += n ** 3
#     return count

# print(EDE(3))

#1

# def skip_letter(word):
#     result = []
#     for i in range(0, len(word), 2):
#         if word[i] != ' ':
#             result += word[i]
#     return result
    
# word = 'counter attack'
# print(skip_letter(word))

#2 

# def second_skip_letter(word):
#     result = []
#     for i in range(1, len(word), 2):
#         if word[i] != ' ':
#             result += word[i]
#     return result
    
# word = 'counterattack'
# print(second_skip_letter(word))

#3 

# def output_even():
#     smaller_num = int(input('Enter a number: '))
#     larger_num = int(input('Enter a number bigger than the last: '))

#     result = []
#     for n in range(smaller_num, larger_num + 1):
#         if n % 2 == 0:
#             result.append(n)
#     return result 

# print(output_even())

#4 

# def output_odd():
#     smaller_num = int(input('Enter a number: '))
#     larger_num = int(input('Enter a number bigger than the last: '))

#     result = []
#     for n in range(smaller_num, larger_num + 1):
#         if n % 2 != 0:
#             result.append(n)
#     return result 

# print(output_odd())

#5

# def hailstone_seq(num):
#     saved_values = [num]

#     while num > 1:
#         if num % 2 == 0:
#             num = num // 2
#         else:
#             num = (num * 3) + 1
#         saved_values.append(num)
    
#     return saved_values

# print(hailstone_seq(25))     
             
#6

# def find_factors(num):
    
#     factors = []
    
#     for n in range(1,num + 1):
#         if num % n == 0:
#             factors.append(n)
#     return factors

# print(find_factors(12))

#7

# def ascending_order(num1, num2,num3):
#     if num1 > num2:
#         num1, num2 = num2, num1
#     if num2 > num3:
#         num2, num3 = num3, num2
#     if num1 > num2:
#         num1, num2 = num2, num1
#     return num1, num2, num3

# print(ascending_order(45, 6, 2))

#8

# def descending_order(num1, num2, num3):
#     if num1 < num2:
#         num1, num2 = num2, num1
#     if num2 < num3:
#         num2, num3 = num3, num2
#     if num1 < num2:
#         num1, num2 = num2, num1
#     return num1, num2, num3
    
# print(descending_order(2,3,1))

#9

# def count(list_of_cards):
#     count = 0


#     for card in list_of_cards:
#         if str(card) in ['2','3','4','5','6']:
#             count += 1
#         elif str(card) in ['10','j','q','k','a']:
#             count -= 1 
#     return count

# print(count([5,9,10,3,'j','a',4,8,5]))

#10

# def war_of_numbers(numbers):
#     even_sum = 0
#     odd_sum = 0
#     for n in numbers:
#         if n % 2 == 0:
#             even_sum += n
#         else:
#             odd_sum += n

#     if even_sum > odd_sum:
#         return 'evens is larger'
#     elif odd_sum > even_sum:
#         return 'odds is larger'
#     else:
#         return 'evens and odds are equal'
    
# print(war_of_numbers([2,8,7,5]))

#11

# def add_lists(list1, list2):
#     list3 = []

#     for i in range(len(list1)):
#             list3.append(list1[i]+ list2[i])
#     return list3

# print(add_lists([1,3,3,1],[4,3,6,1]))

#12

# def largest_even(numbers):
    
#      largest = -1
#      for n in numbers:
#          if n % 2 == 0 and n > largest:
#              largest = n
#      return largest

# print(largest_even([7,1,0,9,13]))

#13

# def largest_odd(numbers):
    
#     largest = -1
#     for n in numbers:
#         if n % 2 != 0 and n > largest:
#             largest = n
#     return largest

# print(largest_odd([2,4,1111111,6]))

#14

# def progress_days(numbers):
#     count = 0

#     for i in range(1, len(numbers)):
#         if numbers[i] > numbers[i - 1]:
#             count += 1
#         elif numbers[i] == numbers[i - 1]:
#             count = 0
#     return count

# print(progress_days([1,1]))

# 15


# def lag_days(numbers):
#     count = 0

#     for i in range(1, len(numbers)):
#         if numbers[i] < numbers[i - 1]:
#             count += 1
#         elif numbers[i] == numbers[i - 1]:
#             count = 0

#     return count

# print(lag_days([9,9]))


#16

def like_or_dislike(input):
    if input == "dislike":
        return 'dislike'
    elif input == "like":
        return 'like'
    else:
        return 'nothing'
    
print(like_or_dislike(["dislike","like", 'dislike']))
#17

# def get_indices(lyst, target):

#     indicies = []

#     for i in range(1, len(lyst)):
#         if lyst[i] == target:
#             indicies.append(i)
#     return indicies

# print(get_indices([1,5,5,2,7],7))

#18

# def list_of_multiples(num1, length):

#     multiples = []
#     for n in range(1, length + 1):
#         multiples.append(num1 * n)
#     return multiples

# print(list_of_multiples(7,5))

#19

# def is_acronym(s, words):

#     acronyms = ''

#     for word in words:
#         acronyms += (word[0])
#     if acronyms == s:
#         return True
#     else:
#         return False



# print(is_acronym('abc', ['alice', 'bob', 'charlie']))






