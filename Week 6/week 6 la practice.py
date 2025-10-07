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

