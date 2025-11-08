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
    

pond1 = Pond("Swamppy")
duck1 = Duck("Nate", "Yellow")
duck2 = Duck('Deshaun', 'Green')
pond1.add_duck(duck1)
pond1.add_duck(duck2)
print(pond1)
pond1.ducks_quacks()
        
            

    
            
    