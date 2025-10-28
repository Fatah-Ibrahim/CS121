
# 1

# def is_isogram(word):
    

#     for i in range(len(word)):
#         for j in range(i + 1, len(word)):
#             if word[i] == word[j]:
#                 return False
#     return True

# print(is_isogram('Algorism'))


#2 

# def find_unique(num_list):

#     find_unique = []
#     for x in num_list:
#         count = 0
#         for y in num_list:
#             if x ==y:
#                 count += 1
#         if count == 1:
#             find_unique.append(x)
#     return find_unique

# print(find_unique([7,9,9,0,7,2,1,4]))

#3

# def find_unique(num_list):

#     find_unique = []
#     for x in num_list:
#         count = 0
#         for y in num_list:
#             if x ==y:
#                 count += 1
#         if count == 1:
#             find_unique.append(x)
#     return find_unique


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

# menu_dict = {'Burgers' : 10, 'Fries': 4, 'Soda': 3}

# def restaurant(menu_dict):
    
#     output = ''
#     for food, price in menu_dict.items():
#         output += f'{food} costs {price}\n'
#     return output
# print(restaurant(menu_dict))

#11

# def count_reps(elements):
    
#     reps_dict = {} 

#     for word in elements:
#         if word in reps_dict:
#             reps_dict[word] += 1
#         else:
#             reps_dict[word] = 1 
#     return reps_dict
    
# print(count_reps(['cat', 'dog', 'cat', 'cow', 'cow', 'cow']))
    
#12

# def items_purchase(store, wallet):
#     #what is the sum of the store items    
#     affordable = {}

#     for item in store:
#         price = store[item]
#         if wallet >= price:
#             affordable[item] = price
#             wallet -= price
#     return affordable
        
        
# print(items_purchase({'Water': 1, 'Bread': 3, 'TV': 1000},300))


#13

# def total_sales(sales):

#     sum = 0 

#     for item_name in sales:
#         sum += sales[item_name]
#     return sum

# print(total_sales({"Shoes": 20, "Hats": 15, "Jackets": 10}))

#14

# def high_earners(employee_salaries, amount):

#     higher_salarie = []

#     for name in employee_salaries:
#         if employee_salaries[name] > amount:
#             higher_salarie.append(name)
#     return higher_salarie

# print(high_earners({'Alice': 50000, 'Bob': 75000, 'Charlie': 1000000},60000))

#15

# def total_donations(donations):

#     sum = 0
#     for donors in donations:
#         sum += donations[donors]
#     return sum

# print(total_donations({'John': 100, 'Sarah': 200, 'Mike': 50}))

#17

# def total_calories(fruits):

#     calories = {'apple': 95, 'banana': 105, 'orange': 62, 'grape': 3, 'pear': 102}
#     sum = 0
#     for fruit in fruits:
#         sum += calories[fruit]
#     return sum
    
# print(total_calories(['apple', 'banana', 'orange']))

#18

# def total_cost(ingredients):
    
#     price = {'flour': 2.50, 'sugar': 1.80, 'eggs': 3.00, 
#              'milk': 2.00, 'butter': 2.75, 'vanilla': 4.50,
#              'chocolate': 5.00}
    
#     sum = 0
#     for ingredient in ingredients:
#         sum += price[ingredient]
#     return sum

# print(total_cost(['flour', 'sugar', 'eggs', 'butter']))
