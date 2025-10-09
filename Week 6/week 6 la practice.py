# 5

# def hailstone_seq(num):

#     saved_values = []

#     while num > 1:
#         if num % 2 == 0:
#             num = num / 2
#         else:
#             num = (num ** 3) + 1


#         saved_values.append(num)
#     return saved_values

#9

# def count(list_of_cards):
#     points = 0 
#     # ['10', 'j', 'q', 'k'] +1
#     # ['2', '3', '4', '5', '6'] -1

#      #Iterate through each of the card
#     for cards in list_of_cards:
#         if str(cards) in ['10', 'j', 'q', 'k']:
#             points +=1
#         elif str(cards) in ['2', '3', '4', '5', '6']:
#             points -=1
#     return points   


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

def add_lists(list1, list2):
    list3 = []

    for i in range(len(list1)):
            list3.append(list1[i]+ list2[i])
    return list3

print(add_lists([1,3,3,1],[4,3,5,1]))




    


