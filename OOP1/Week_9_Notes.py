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

# print(Planet1)
# print(Planet2)


class Star:
    
    
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def __str__(self):
        msg = ''
        msg += f'Hello {self.get_name()}. How are you'
        return msg
    
              
        
# star1 = Star('Orian')

# print(star1.get_name())
# print(star1)
        


'''Create a planetary system clss that takes a star as an arguement, has the ability to add 
planets to the system, can print all the planets the system. 
'''

class PlanetarySystem: 
    def __init__(self, _star):
        self.star = _star
        self.planets= []

    def add_planet(self, _planet):
        self.planets.append(_planet)

    def show_planets(self):
        for planet in self.planets:
            print(Planet.get_name(planet))

