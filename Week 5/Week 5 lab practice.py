#2
'''
def is_fever(temp):
    tr
    if user_temp >= 98.5:
        





temp_unit = input("What is the unit of the tempature: ")
user_temp = int(input("What is your tempature: "))
'''


#find Temp F or C 
# enter temp input
#if 98.6 F --> Fever 
#if 37 C -> Fever


# Define your function here 


#1 

'''
def pyramid_volume(base, height):
   
    volume = (base ** 2 * height) / 3
    return volume

print(pyramid_volume(2,2))

'''

#2 

'''
def cone_volume(radius, height):
  
  import math
  volume =  (math.pi * (radius ** 2 * height)) / 3
  return volume

print(cone_volume(1,2))
'''

#3

# def total_score(two_pointers, three_pointers):
    
#     two_pointers *= 2
#     three_pointers *= 3
    
#     score = two_pointers + three_pointers

#     return score

# print(total_score(5,7))

#6 

# def battery_counter(e_dolls, rc_cars, robo_dog):
#     # Electric dolls 2
#     e_dolls *= 2
#     # RC cars 4
#     rc_cars *= 4
#     # robo dog 6
#     robo_dog *= 6

#     total = e_dolls + rc_cars + robo_dog

#     return total 

# print(battery_counter(4,3,2))


# 10

# def access_rights(user_roles):

#     if user_roles == 'user':
#         print('limited')
#     elif user_roles == 'guest':
#         print('view')
#     elif user_roles == 'admin':
#         print('full')
#     return user_roles


# access_rights('admin')


# def access_rights1():
#     user_roles = input("Enter your role: ")
#     if user_roles == 'user':
#         return 'limited'
#     elif user_roles == 'guest':
#         return 'view'
#     elif user_roles == 'admin':
#         return 'full'
#     return user_roles

# print(access_rights1())


# carpet

# width = int(input())
# length = int(input())
# pattern = input()

# for i in range(length):
#     print(pattern*width)



#8


#def pool_time(user_grade, user_time):

    #time_output = "" 

    #if user_grade == "k":
    #   user_grade = 0
    #if int(user_grade) >= 0 and int(user_grade) <= 3:
        #if user_time == "morning":
           #time_output = "9am" 
        #elif user_time == "afternoon":
            #time_output = "1pm"
   # if int(user_grade) >= 4 and int(user_grade) <= 8:
    #    if user_time == "morning":
    #        time_output = "10am"
     #   elif user_time == "afternoon":
      #     time_output = "2pm"
   # if int(user_grade) >= 9 and int(user_grade) <= 12:
    #    if user_time == "morning":
     #       time_output = "11am"
      #  elif user_time == "afternoon":
       #     time_output = "3pm"
   # return time_output

#print(pool_time(3,"afternoon"))







#11 !!!!!!!!!!!!!!

# def convert_kunts(kunts):
#    output = ""
#   # galleon = kunts / 493
#    remaining_kunts = kunts - (galleon * 493)
#     sickles = remaining_kunts // 29
#     remaining_kunts = remaining_kunts - (sickles * 29)
#     if galleon > 0:
#        output = output + f"Galleon: {galleon}"
#    if sickles > 0:
#        output = output + f"sickles {sickles}"
#    if kunts > 0:
#        output = output + f"Kunts {remaining_kunts}"
#    return output


#user_input = input("Enter a number of knuts: ")
    #print(f'for {user_input} knuts I can buy are: {convert_kunts(user_input)}')

#12

# def convert_bronze(bronze):
#     # 20 bronze equals 1 silver
#     # 15 silver equal 1 gold
#     output = ''
#     gold = bronze // 300
#     remaining_bronze = bronze - (gold * 300)
#     remaining_bronze = bronze % 300
#     silver = remaining_bronze // 20
#     remaining_bronze = remaining_bronze % 20
#     remaining_bronze = remaining_bronze - (silver * 20)
#     if gold > 0:
#         output += f'{gold} Gold'
#     if silver > 0:
#         output += f' {silver} Silver'
#     if bronze > 0:
#         output += f' {remaining_bronze} Bronze'
#     return output


# user_input = int(input('Enter amunt of bronze coins: '))
# print(f'{convert_bronze(user_input)}')



# #1 strings

# def reverse_string(word):
#     return word[::-1]

# print(reverse_string('hello'))

# def is_fever(temp):
#     value, unit = float(temp[:-1]), temp[-1]
#     if unit == 'F':
#         return value > 98.6
#     elif unit == 'C':
#         return value > 37
        
    
# print(is_fever("95F"))

#5 isogram

# def is_isogram(word):
#     for i in range(len(word)):
#         for j in range(i +1, len(word)):
#             if word[i] == word[j]:
#                 return False
#         return True
            
# print(is_isogram('Tufah'))

# # 4 hamming distance

# def hamming_distance(word, word2):
#     count = 0
#     for i in range(len(word)):
#             if word[i] != word2[i]:
#                 count += 1
#     if count == 0:
#         return f'{count}, since all {count} words are the same.'
#     elif count == 1:
#         return f'{count}, since there is only 1 character that is different.'
#     elif count > 1:
#         return f'{count}, since all {count} words are the different.'

# print(hamming_distance('abdce','bcdef'))



