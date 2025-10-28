#7 

# def ascending_order(num1, num2 = 5, num3 = 25):



#     if num1 > num2:
#         num1, num2 = num2 , num1
#     elif num1 > num3:
#         num1, num3 = num3, num1
#     elif num3 > num2:
#         num3, num2 = num3, num3
#     return [num1, num2, num3]

# print(ascending_order(50))

#9

# def get_indices(indice_list , vaule = 0):

#     result = []
#     for i in range(len(indice_list)):
#         if indice_list[i] == vaule:
#             result.append(i)
#     return result

# print(get_indices([1, 0, 5, 0, 7]))




#14

# def is_two_digit_nums(num):
    
#     return num >= 10 and num <= 99
    
# def report_two_digit_nums(nums_list):
    
#     result = []
    
#     for num in nums_list:
#         if is_two_digit_nums(num):
#             result.append(num)
#     return result
# print(report_two_digit_nums([100,22,12,11,3333,3,3]))



     

#15

# def is_negative(nums):
#      if nums < 0:
#         return True
#      else:
#          return False
        
# def is_odd(nums):

#     if nums % 2 != 0:
#         return True
#     else:
#         return False
    
# def report_negative_odds(nums_list):
#     result = []

#     for num in nums_list:
#         if is_negative(num) and is_odd(num):
#             result.append(num)
#     return result

# print(report_negative_odds([100,-57, 12, 1, -36, -15]))

