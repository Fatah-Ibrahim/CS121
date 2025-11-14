#1

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name

    def get_major(self):
        return self.major
    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f"Hello I'm {self.name} and my major is {self.major}"
        
    
class Course:
    def __init__(self, course_name, course_number,):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []

    def get_course_number(self):
        return self.course_number
    def set_course_number(self, course_number):
        self.course_number = course_number

    def add_student(self, students):
        self.students.append(students)

    def show_student_enrollment(self):
        for student in self.students:
            print(student)
    
    def __str__(self):
        return f'This is the course number: {self.get_course_number()}.'


# class2 = Course('intro to pythpn', "121")
# student1 = Student("bob", "CIS")
# student2 = Student('Maddie', 'Nursing')
# class2.add_student(student1)
# class2.add_student(student2)
# class2.show_student_enrollment()

#2

class Duck:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

    def speak(self):
        print('Quack')

    def __str__(self):
        return f'{self.name}'

class Pond:
    def __init__(self, name):
        self.name = name
        self.ducks = []

    def add_duck(self, duck):
        self.ducks.append(duck)

    def ducks_quacks(self):
        for duck in self.ducks:
            print(f" {duck} says:")
            duck.speak()

    def __str__(self):
        return f'{self.name} and there are {len(self.ducks)} ducks'
    

# pond1 = Pond("Swamppy")
# duck1 = Duck("Nate", "Yellow")
# duck2 = Duck('Deshaun', 'Green')
# pond1.add_duck(duck1)
# pond1.add_duck(duck2)
# print(pond1)
# pond1.ducks_quacks()
        
#3

class Lion:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
    def roar(self):
        print('Roar!')

    def __str__(self):
        return f'{self.name}'

class Zoo:
    def __init__(self, location):
        self.location = location
        self.lions = []

    def add_lion(self, lions):
        self.lions.append(lions)

    def lions_roar(self):
        for lion in self.lions:
            print(f" {lion} says:")
            lion.roar()

    def count_lions(self):
        m_count = 0
        fm_count = 0 
        for lion in self.lions:
            if lion.gender == 'male':
                m_count += 1
            else:
                fm_count += 1
        print(f'{m_count} male, {fm_count} female')

        
    def __str__(self):
        return f'At {self.location} Zoo there are {len(self.lions)} lions'

lion1 = Lion('rash', 'male')
lion2 = Lion('hida', 'female')
zoo1 = Zoo ('Safari')

# zoo1.add_lion(lion1)
# zoo1.add_lion(lion2)
# print(zoo1)
# zoo1.lions_roar()
# zoo1.count_lions()

#4 

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position
    def set_position(self, position):
        self.position = position
    
    def __str__(self):
        return f' Name: {self.name} Position: {self.position}'
    
class Department:
    def __init__(self, dept_name, budget):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []

    def get_budget(self):
        return self.budget
    def set_budget(self, budget):
        self.budget = budget

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def is_large(self):
        return len(self.employees) >= 10 
    def show_staff_list(self):
        for staff in self.employees:
            print(staff)
    
    def __str__(self):
        return f'Department: {self.dept_name} Budget: {self.budget}'
    
dept1 = Department('MNSU', 1000,)
employee1 = Employee('Fatah', 'Student')
employee2 = Employee('Hoda', 'Student')

# dept1.add_employee(employee1)
# dept1.add_employee(employee2)
# dept1.show_staff_list()

#5

class Droid:
    def __init__(self, designation, series):
        self.designation = designation
        self.series = series

    def get_series(self):
        return self.series
    def set_series(self, series):
        self.series = series

    def communicate(self):
        print('Beep-Bloop-Blop!')

    def __str__(self):
        return f'A Droid say "Beep-Bloop-Blop."'
class Starship:
    def __init__(self, name):
        self.name = name
        self.droids = []

    def add_droid(self, droid):
        self.droids.append(droid)
    
    def droids_communicate(self):
        for droid in self.droids:
            droid.communicate()
    
    def __str__(self):
        return f'Hello {self.name}'
    
ship1 = Starship('Galactico')
driod1 = Droid('DRF', '-90282')
driod2 = Droid('DSF', '-90282')

# ship1.add_droid(driod1)
# ship1.add_droid(driod2)

# ship1.droids_communicate()

#6 

class Post:
    def __init__(self, caption, likes):
        self.caption = caption
        self.likes = likes

    def get_likes(self):
        return self.likes

    def add_like(self):
        self.likes += 1

    def display(self):
        print(self.caption)
    
    def __str__(self):
        return f'Caption: {self.caption} Likes: {self.likes}'
    
class Profile:
    def __init__(self, username):
        self.username = username
        self.post = []

    def add_post(self, post):
        self.post.append(post)

    def display_trending_posts(self):
        for post in self.post:
            if post.likes >= 10000:
                print(post)

    def __str__(self):
        return f'Profile: {self.username} Amount of posts {len(self.post)}'
    
profile1 = Profile('Cert')

post1 = Post("soccer", 10010)
post2 = Post("college", 99)

# profile1.add_post(post1)
# profile1.add_post(post2)

# profile1.display_trending_posts()

#7 

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    
    def display_details(self):
        print(f'{self.name} costs ${self.price}')

    def __str__(self):
        return f'{self.name} costs ${self.price}'
    
class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)
    
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        print(f'Total = ${total}')

    def __str__(self):
        return f'here is the amount of items in your shopping cart {len(self.products)}'
    
# cart1 = ShoppingCart('Tufah')

# item1 = Product('Macbook', 1100)
# item2= Product('Ipad', 350)

# cart1.add_product(item1)
# cart1.add_product(item2)
# cart1.calculate_total()

#8

class LLM:
    def __init__(self, name, token_limit):
        self.name = name
        self.token_limit = token_limit
    
    def get_token_limit(self):
        return self.token_limit
    def set_token_limit(self, token_limit):
        self.token_limit = token_limit

    def __str__(self):
        return f'{self.name} your token limit is: {self.token_limit}'
    
class AICompany:
    def __init__(self, company_name, founding_year, headquarters):
        self.company_name =company_name
        self.founding_year = founding_year
        self.headquarters = headquarters
        self.llms = []

    def get_headquarters(self):
        return self.headquarters
    def set_headquarters(self, headquarters):
        self.headquarters = headquarters

    def add_llm(self, llm):
        self.llms.append(llm)

    def display_models(self):
        for llm in self.llms:
            print(llm)

    def __str__(self):
        return f'here is the amount of llms {len(self.llms)}'

ai1 = AICompany('Blink', 2022, 'Minnesota')

llm1 = LLM('bob', 213)
llm2 = LLM('nate', 222)

# ai1.add_llm(llm1)
# ai1.add_llm(llm2)

# ai1.display_models()

#9

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price

    def show_discription(self):
        print(f'{self.name} costs ${self.price}')

    def __str__(self):
        return f'{self.name} costs ${self.price}'

class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)
    
    def lunch_menu(self):
        for item in self.menu_items:
            discounted = item.price - 2
            print(f'{item.name} costs ${discounted}')

    def display_menu_item(self):
        for item in self.menu_items:
            print(item)
    
    def __str__(self):
        return f'Welcome to {self.restaurant_name}! Please enjoy the food!'
    


restaurant1 = Restaurant('Sunny')

item1 = MenuItem('Pasta', 10)
item2 = MenuItem('Rice', 12)
        
restaurant1.add_menu_item(item1)
restaurant1.add_menu_item(item2)

# restaurant1.display_menu_item()
# restaurant1.lunch_menu()

#10

class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author

    def display_info(self):
        print(f'{self.title} by: {self.author}')

    def __str__(self):
        return f'{self.title} by: {self.author}'
    
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def display_catalog(self):
        for book in self.books:
            print(book)
    
    def __str__(self):
        return f'There are this amount of books in this library: {len(self.books)}'
    
lib1 = Library('Beckham Library')

book1 = Book('One Piece', 'Eiichiro Oda')
book2 = Book('Gachiakuta', 'Kei Urana')

# lib1.add_book(book1)
# lib1.add_book(book2)

# lib1.display_catalog()

# 11

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def get_artist(self):
        return self.artist
    def set_artist(self, artist):
        self.artist = artist

    def play(self):
        print(f'{self.title} by {self.artist}')

    def __str__(self):
        return f'{self.title} by {self.artist}'
    
class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def play_all(self):
        for song in self.songs:
            song.play()

    def __str__(self):
        return f'Here are your playlist: {len(self.songs)}'
    
playlist1 = Playlist('Late Night Drive')

song1 = Song('Gravity', 'Nba YoungBoy')
song2 = Song('Letter to Big Dump', 'Nba YoungBoy')

playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.play_all()

#12

class TVShow:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
    
    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre
    
    def preview(self):
        print(f'The title is {self.title} and the genre is {self.genre}')
    
    def __str__(self):
        return f'The title is {self.title} and the genre is {self.genre}'
    
class NetflixDashboard:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.shows = []
    
    def add_show(self, show):
        self.shows.append(show)

    def display_recommendations(self):
        for show in self.shows:
            show.preview()
    
    def __str__(self):
        return f'User: {self.profile_name}'
    
prof1 = NetflixDashboard('Fatah')

show1 = TVShow('One Piece', "Shonen")
show2 = TVShow('The Unwanted Undead Adventurer', 'Isakai')

# prof1.add_show(show1)
# prof1.add_show(show2)

# prof1.display_recommendations()
