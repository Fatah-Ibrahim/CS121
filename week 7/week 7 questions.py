#4 

# def get_names(name_dict):
#     result = []
#     for key in name_dict: 
#         names = name_dict[key]
#         result.append(names)
#     return result

# print(get_names({'01475' : 'steve', '87469': 'alice', '654123' : 'bob'}))

#5 

# def find_oldest(people):
#     oldest = ''
#     largest = 0
#     for key in people:
#         age = people[key]
#         if age > largest:
#             largest = age
#             oldest = key
#     return oldest
    

# print(find_oldest({'Emma': 71, 'Jack': 45, 'Olivia': 82, 'Liam': 39}))

#6 

# def letter_count(word):
#     count_dict = {}
#     for letter in word:
#         if letter in count_dict:
#             count_dict[letter] += 1
#         else:
#             count_dict[letter] = 1
#     return count_dict
# print(letter_count("Hello"))
        
#9

# recipe_dict = {"Side Salad": 6,
#                "Chicken Perm": 12, 
#                 "Cookie": 3 }

# def total_cost(recipe_dict):
#         sum = 0
#         for key in recipe_dict:
#                 sum += recipe_dict[key]
#         return sum
# print(total_cost(recipe_dict))

#10

menu_dict = {'Burgers' : 10, 'Fries': 4, 'Soda': 3}

def restaurant(menu_dict):
    
    output = ''
    for food, price in menu_dict.items():
        output += f'{food} costs {price}\n'
    return output
print(restaurant(menu_dict))
         
    
    


    

    