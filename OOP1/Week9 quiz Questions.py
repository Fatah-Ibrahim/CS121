import math 

#1 
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name      
    
    def get_price(self):
        return self.price 
    
    def get_quantity(self):
        return self.quantity 

    # def set_name(self, name):
    #     self.name = name      
    
    # def set_price(self, price):
    #     self.price = price
    
    # def set_quantity(self, quantity):
    #     self.quantity = quantity 


# item = Product('PlayStation 5', 449.99, 1)

# print(f"Name: {item.get_name()}")
# print(f"Price: ${item.get_price()}")
# print(f"Quantity: {item.get_quantity()}")


#2 

class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_page_count(self):
        return self.page_count
    
    def set_title(self, title):
        self.title = title

    def set_author(self,author):
        self.author = author

    def set_page_count(self, page_count):
        self.page_count = page_count

# book = Book('Lord of the Rings', 'Fatah Ibrahim', 540)

# print(f"Name: {book.get_title()}")
# print(f"Author: {book.get_author()}")
# print(f"Page count: {book.get_page_count()}")

#3
class Movie:
    def __init__(self, title, director, run_time):
        self.title = title
        self.director = director
        self.run_time = run_time

    def get_title(self):
        return self.title
    
    def get_director(self):
        return self.director
    def get_run_time(self):
        return self.run_time
    
    def set_title(self, title):
        self.title = title
    
    def set_artist(self, director):
        self.director = director
        
    
    def set_run_time(self, run_time):
        self.run_time = run_time

# movie = Movie('Weapons', 'Najib', 222)

# print(f'Title: {movie.get_title()}')
# print(f'Director: {movie.get_director()}')
# print(f'Runtime in minutes: {movie.get_run_time()}')
#4
class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds

    def get_title(self):
        return self.title
    
    def get_artist(self):
        return self.artist
    
    def get_duration_seconds(self):
        return self.duration_seconds
    
    def set_title(self, title):
        self.title = title
    
    def set_artist(self, artist):
        self.artist = artist
    
    def set_duration_seconds(self, duration_seconds):
        self.duration_seconds = duration_seconds

# song = Song('Something', 'Nba YoungBoy', 168)

# print(f'Title: {song.get_title()}')
# print(f'Artist: {song.get_artist()}')
# print(f'Duration in seconds: {song.get_duration_seconds()}')

#5 

class Employee:

    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def get_name(self): 
        return self.name      

    def get_title(self):     
        return self.title

    def get_salary(self):
        return self.salary
    
    def set_name(self, name):
        self.name = name

    def set_title(self, title):
        self.title = title

    def set_salary(self,salary):
         self.salary = salary
    
    def greeting(self):
        return f" Hello. My name is {self.name}. I'm the {self.title}"
    
    def request_raise(self):
        new_salary = self.salary * 1.06

        return f"I'm currently making {self.salary}. I'd like new salary of {new_salary}"


# job = Employee('Fatah', 'DSP', 31000)
# print(job.request_raise())

#6

class Student:

    def __init__(self, name, major, GPA):
        self.name = name
        self.major = major
        self.GPA = GPA

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def get_GPA(self):
        return self.GPA

    def set_GPA(self, GPA):
        self.GPA = GPA

    def introduction(self):
        return f"Hi, I'm {self.name}. I'm studying {self.major}"
    
    def study_for_exam(self):
        old_GPA = self.GPA
        if self.GPA < 4.0: 
            self.GPA += 0.2
        else:
            return f"Reached Maxium GPA"
        return f"I'm hitting the books! My GPA increased from old {old_GPA} to {self.GPA}"

# learner = Student("Fatah", "Computer Science", 3.5)
# print(learner.study_for_exam())

#7 

class Vehicle:
    def __init__(self, _make, _model, _year):
        self.make = _make
        self.model = _model
        self.year = _year
        

    def get_make(self):
        return self.make
    
    def set_make(self, _make):
        self.make = _make
    
    def get_model(self):
        return self.model
    
    def set_model(self, _model):
        self.model = _model

    def get_year(self):
        return self.year
    
    def set_year(self, _year):
        self.year = _year

    def print_vehicle_type(self):
        return f'{self.year} {self.make} {self.model}'

# car = Vehicle('Toyota', 'Camry', '2021')
# print(car.print_vehicle_type())

#8 

class Course:
    def __init__(self, corse_code, course_name, instructor):
        self.course_code = corse_code
        self.course_name = course_name
        self.instructor = instructor

    def get_corse_code(self):
        return self.course_code
    def set_course_code(self, course_code):
        self.course_code = course_code
    
    def get_corse_name(self):
        return self.course_name
    def set_course_code(self, course_name):
        self.course_name = course_name
    
    def get_instructor(self):
        return self.instructor
    def set_instructor(self, instructor):
        self.instructor = instructor

    def print_info(self):
        return f'{self.course_code}: {self.course_name} taught by {self.instructor}'
    
# class1 = Course('CIS121', 'Introduction to programming', 'Matt')
# print(class1.print_info())

#9

class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_x_coordinate(self):
        return self.x_coordinate
    def set_x_coordinate(self, x_coordinate):
        self.x_coordinate = x_coordinate

    def get_y_coordinate(self):
        return self.x_coordinate
    def set_y_coordinate(self, y_coordinate):
        self.y_coordinate = y_coordinate

    def print_info(self):
        return f'(x,y) = ({self.x_coordinate},{self.y_coordinate})'
    
# xy = Point(4,5)
# print(xy.print_info())

#10
class Vector:
    def __init__(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction

    def get_x_direction(self):
        return self.x_direction
    def set_x_direction(self, x_direction):
        self.x_direction = x_direction

    def get_y_direction(self):
        return self.y_direction
    def set_y_direction(self, y_direction):
        self.y_direction = y_direction

    def get_magnitude(self):
        x = self.x_direction ** 2 + self.y_direction ** 2
        return math.sqrt(x)


# xy = Vector(9,12)
# print(xy.get_magnitude())


#11

class ColorRGB:
    def __init__(self, _red, _green, _blue):
        self.red = _red
        self.green = _green
        self.blue = _blue

    def get_red(self):
        return self.red
    def set_red(self, _red):
        self.red = _red

    def get_green(self):
        return self.green
    def set_red(self, _green):
        self.green = _green

    def get_blue(self):
        return self.blue
    def set_red(self, _blue):
        self.blue = _blue

    def to_greyscale(self):
        greyscale = (0.3 * self.red) + (0.59 * self.green) + (0.11 * self.blue)
        return greyscale
    
# color = ColorRGB(255, 215, 0)
# print(color.to_greyscale())

    
#12

class TemperatureInCelsius:
    def __init__(self, temp_value):
        self.temp_value = temp_value

    def get_temp_value(self):
        return self.temp_value
    def set_temp_value(self, temp_value):
        self.temp_value = temp_value

    def to_fahrenheit(self):
        return (self.temp_value * 9/5) + 32
    
# temp = TemperatureInCelsius(40)
# print(temp.to_fahrenheit())

#13 

class Rectangle:
    def __init__(self, _width, _length):
        self.width = _width
        self.length = _length

    def get_width(self):
        return self.width
    def set_width(self, _width):
        self.width = _width
    
    def get_length(self):
        return self._length
    def set_length(self, _length):
        self.length = _length

    def calculate_area(self):
        return self.width * self.length
    
# rect = Rectangle(2,2)
# print(rect.calculate_area())

# 14

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
# circle = Circle(45)
# print(circle.calculate_circumference())

#15

class Recipe:
    def __init__(self, name, cooking_time):
        self.name = name
        self.cooking_time = cooking_time
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def get_cooking_time(self):
        return self.cooking_time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def is_quick_meal(self):
        return self.cooking_time < 30
        
# meal = Recipe('Ramen', 33)
# print(meal.is_quick_meal())
