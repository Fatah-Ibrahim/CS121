
import math 

#1 

class Vector:
    def __init__(self, _x_component, _y_component):
        self.a = _x_component
        self.b = _y_component

    def __eq__(self, other_vector):
        return self.a == other_vector.a and self.b == other_vector.b
    
    def __str__(self):
        return f'{self.a}x + {self.b}y'
    
# vect1 = Vector(2,3)
# vect2 = Vector(2,3)
# print(vect1)
# print(vect1 == vect2)

#2

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y
    
    def distance(self, other):

        eq1 = math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2)
        distance = math.sqrt(eq1) 
        return distance
    
    def __str__(self):
        return f'x = {self.x}, y = {self.y}\n   ({self.x},{self.y})'

p1 = Point(3,4)
p2 = Point(0,0) 

# print(p1.__eq__(p2))
# print(p1.distance(p2))
# print(p1)    

#3

class LinearEquation:
    def __init__(self, slope, y_intercept):
        self.m = slope
        self.b = y_intercept

    def __add__(self, other):
        new_slope = self.m + other.m
        new_y_intercept = self.b + other.b
        return LinearEquation(new_slope, new_y_intercept)

    def __str__(self):
        return f' m(slope) = {self.m}, y-intercept = {self.b}\n y = {self.m}x + {self.b} '
    
y1 = LinearEquation(2, 3)
y2 = LinearEquation(-1, 5)

# print(y1.__add__(y2))
# print(y2)

#4 

class Time:
    def __init__(self, hours = 0, minutes = 0):
        self.hours = hours
        self.minutes = minutes
    
    def __add__(self, other : Time):

        '''# t3 = Time(self.hours, self.minutes)
        
        # t3.hours += other.hours
        # t3.minutes += other.minutes

        # if t3.minutes > 60:
        #     t3.hours += 1
        #     t3.minutes = t3.minutes - 60'''

        hours_to_minutes = self.hours * 60
        new_hour = self.hours + other.hours 
        new_mins = self.minutes + other.minutes

        while new_mins >= 60:
            remaining_minutes = new_mins - 60
            new_hour += 1
            new_mins = remaining_minutes
        return Time(new_hour, new_mins)
    
    def __str__(self):
        return f'{self.hours}h {self.minutes}m'
    
t1 = Time(1, 10)
t2 = Time(0, 40)
t3 = t1.__add__(t2)

# print(t3)

#5

class RBGColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __add__(self, other):

        combine_color = (self.red + other.red) / 2, (self.green + other.green) / 2, (self.blue + other.blue) / 2
        return combine_color
    
    def __str__(self):
        return f'({self.red}, {self.green}, {self.blue})'



c1 = RBGColor(170, 150, 200)
c2 = RBGColor(30, 100, 60)

c3 = c1 + c2

# print(c3)

#6 

class RationalNumbers:
    def __init__(self, numerator, denominator):
        self.a = numerator
        self.b = denominator

    def __add__(self, other):

        if self.b != other.b:
            new_b = self.b * other.b
            new_n = (self.a * other.b) + (self.b * other.a)
            return RationalNumbers(new_n, new_b)
        
        if self.b == other.b:
            new_n = self.a + other.a
            return RationalNumbers(new_n, self.b)
    def __str__(self):
        return f' {self.a} / {self.b}'

f1 = RationalNumbers(2,5)
f2 = RationalNumbers(1,5)

f3 = f1 + f2

# print(f3)

#7

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a 
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        if self.b == 0:
            return f'{self.a}'
        elif self.b > 0:
            return f'{self.a} + {self.b}i'
        else:
            return f'{self.a} - {abs(self.b)}i'
        

z1 = ComplexNumber(3, 2)
z2 = ComplexNumber(-1, 4)
z3 = ComplexNumber(2,0)

# print(z3)

#8 

class Playlist:
    def __init__(self, name = "New Playlist", songs = []):
        self.name = name
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def __add__(self, other):
        combine_name = self.name + other.name
        combine_songs = self.songs + other.songs
        return Playlist(combine_name, combine_songs)

    def __str__(self):
        return f'{self.name}, {self.songs}' 
    
p1 = Playlist("A", ['Song A', 'Song B'])
p2 = Playlist("C", ['Song C'])

p3 = p1 + p2

# print(p3)

#9

class ShoppingCart:
    def __init__(self, items = {}):
        self.items = items

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
           self.items[item] = 1
    
    def __add__(self, other):
        combined = ShoppingCart()
        for item, qty in self.items.items():
            combined.items[item] = qty

        for item, qty in other.items.items():
            if item in combined.items:
                combined.items[item] += qty
            else: 
                combined.items[item] = qty
        
        return combined



    def __str__(self):
        return f'{self.items}'
    

p1 = ShoppingCart({'tea': 1, 'energy drink': 2})
p1.add_item('clock')
# print(p1)
p2 = ShoppingCart({'energy drink': 3, 'hat': 1})

combined = p1.__add__(p2)

# print(combined)

#10 

class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area(self):
        return self.w * self.h
    
    def __mul__(self, integer):
        new_witdh = self.w * integer
        new_height = self.h * integer
        return f'Width: {new_witdh} Height: {new_height}'
    
    def __str__(self):
        return f'Width: {self.w} Height: {self.h}'
    
r1 = Rectangle(4,5)
r2 = Rectangle(3,2)

# print(r1.__mul__(3))

        


