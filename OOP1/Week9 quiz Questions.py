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
        self.new_salary = self.salary * 1.06

        return f"I'm currently making {self.salary}. I'd like new salary of {self.new_salary}"


# job = Employee('Fatah', 'DSP', 31000)

# print(job.request_raise())

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

    def set_name(self, major):
        self.major = major

    def get_GPA(self):
        return self.GPA

    def set_GPA(self, GPA):
        self.GPA = GPA

    def introduction(self):
        return f"Hi, I'm {self.name}. I'm studying {self.major}"
    
    def study_for_exam(self):
        self.current_GPA = self.GPA
        if self.GPA < 4.0: 
            self.new_GPA += 0.2
        else:
            return f"Reached Maxium GPA"
        return f"I'm hitting the books! My GPA increased from old {self.current_GPA} to {self.new_GPA}"

learner = Student("Fatah", "Computer Science", 3.5)

print(learner.study_for_exam())