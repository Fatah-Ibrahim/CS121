import math

# Question 1. Area of a trapezoid A= (b1 + b2 / 2) * h
'''
a = float(input(" What is base 1? : "))
b = float(input(" What is base 2? : "))
h = float(input(" What is height? : "))

A = (a + b) / 2 * h

print(f' The area of the trapezoid is {A} ')
'''
# Question 2. Volume of a cylinder = pi * r ** 2 * h
''' 
pi = 3.14
r = float(input(" What is the radius? : "))
h = float(input(" What is the height? : "))

V = pi * r ** 2 * h
print(f' The volume of the cylinder is {V} ')
'''

# Question 3. Volume of a sphere = 4/3 * pi * r ** 3
''' 
pi = 3.14
r = float(input(" What is the radius? : "))

V = 4/3 * pi * r ** 3
print(f' The volume of the sphere is {V} ')
'''

#Challenge question. my age in dog years 
''' 

Human_age = float(input("What is your age?: "))
dog_age = Human_age * 7
dog_years = int(dog_age)
dog_months = (dog_age - dog_years) * 12
months = int(dog_months)
dog_days = (dog_months - months) * 30
days = int(dog_days)

cat_age = Human_age / 9
cat_years = int(cat_age)
cat_months = (cat_age - cat_years) * 12
months = int(cat_months)
cat_days = (cat_months - months) * 30
days = int(cat_days)


# Simpler : horse_age = 3 * (((Human_age ** 2)- 47) / 7 + 12)

horse_age = Human_age ** 2
horse_age = horse_age - 47
horse_age = horse_age / 7 + 12
horse_age = horse_age * 3

horse_years = int(horse_age)
horse_months = (horse_age - horse_years) * 12
months = int(horse_months)
horse_days = (horse_months - months) * 30
days = int(horse_days)

print(f'In dog years you are {dog_years} years, {months} months, and {days} days old.')
print(f'In cat years you are {cat_years} years, {months} months, and {days} days old.')
print(f'In horse years you are {horse_years} years, {months} months, and {days} days old.')
'''


'''
# area of a cylinder


h = float(input("What is the height?: "))
r = float(input("What is the radius?: "))
v = ((math.pi) * math.pow(r,3)) * h

print(v)
'''

#Question 2 volume of a sphere 
'''
radius_of_a_sphere = float(input("What is the radius of the sphere?: "))

volume_of_a_sphere= ((4/3) * math.pi) * math.pow(r,3)

print(volume_of_a_sphere)
'''

#Question 8 how many total legs are on the farm
'''
chickens = float(input("How many chickens are on your farm?: "))
cows = float(input("How many cows are on your farm?: "))
pigs = float(input("How many pigs are on your farm?: "))

total_animal_legs = (chickens * 2) + (cows * 4) + (pigs * 4)

print(total_animal_legs) 

'''

'''
x = 10
x = x + 3
x = x / 2
print(x)
'''