
class Planet:
    def __init__(self, _name):
        self.name = _name

Planet_1 = Planet('x25')


class Dog:
    def __init__(self, _name, _breed, _fur):

        self.name = _name
        self.breed = breed_of_dog()
        self.fur = _fur
        
    
dog1 = Dog('Lab')

 

def breed_of_dog():

    user_input  = input('What breed is your dog: ')
    breed = user_input
    return breed
print(breed_of_dog())