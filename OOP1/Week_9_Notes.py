import math
class Planet:
    def __init__(self, _name, radius, mass, distance):
        self.name = _name
        self.radius = radius
        self.mass = mass
        self.distance = distance
    
    def get_name(self):
        return self.name
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_distance(self):
        return self.distance
    
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume

    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    
    def set_name(self, new_name):
        self.name = new_name
    
    def __str__(self):
        msg = ''
        msg += f'Hello {self.get_name()}. How are you'
        return msg
    



Planet1 = Planet('x25',45,198,1000)
Planet2 = Planet('z37',12,234,2381)

print(Planet1)
print(Planet2)

# print(Planet1.get_name())
# Planet1.set_name('Bama')
# print(Planet1.get_name())



# class Dog:
#     def __init__(self, _name, _breed, _fur):

#         self.name = _name
#         self.breed = breed_of_dog()
#         self.fur = _fur
        
    
# dog1 = Dog('Lab')

 

# def breed_of_dog():

#     user_input  = input('What breed is your dog: ')
#     breed = user_input
#     return breed
# print(breed_of_dog())