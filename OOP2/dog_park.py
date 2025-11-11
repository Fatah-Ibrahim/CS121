
# class Dog:
#     def __init__(self, name, size, breed = 'Unknown'):
#         self.name = name
#         self.breed = breed
#         self.size = size

    
#     def get_name(self):
#         return self.name
    
#     def set_name(self, name):
#         self.name = name

#     def get_breed(self):
#         return self.breed
    
#     def set_breed(self, breed):
#         self.breed = breed

#     def get_size(self):
#         return self.size
    
#     def set_size(self, size):
#         self.size = size

#     def set_new_name(self,new_name):
#         self.name = new_name

#     def speak(self):

#         if self.size == 1:
#             print('yip')
#         elif self.size == 2:
#             print('bark')
#         elif self.size == 3:
#             print('bow wow')
        
    
# class DogPark:
#     def __init__(self, name):
#         self.name = name
#         self.dogs = []

#     def add_dog(self, dog):
#         self.dogs.append(dog)

#     def show_dogs(self):
#         for dog in self.dogs:
#             print(dog.get_name())
    
#     def change_dog_name(self, old_name, new_name):
#         for dog in self.dogs:
#             if dog.get_name() == old_name:
#                 dog.set_name(new_name)
    
#     def find_dog(self, dog_name):
#         for dog in self.dogs:
#             if dog.get_name() == dog_name:
#                 dog.speak()

#     def call_dog(self, dog_name):
#         for dog in self.dogs:
#             if dog.get_name() == dog_name:
#                 self.dogs.remove(dog)



# park1 = DogPark('BarkZone')


# park1.add_dog(Dog('Spoot', 2, 'lab'))
# park1.add_dog(Dog('Rover', 3, 'Mastiff'))
# park1.add_dog(Dog('Fluffy', 1))

# #park1.show_dogs()
# park1.change_dog_name('Spoot', 'Spot')
# #park1.show_dogs()

# park1.show_dogs()
# park1.call_dog('Rover')
# park1.show_dogs()



class BankAccount:
    rate = 0.02
    def __init__(self, _name, inital_balance=0):
        self.owner = _name
        self.balance = inital_balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if value > self.balance:
            print('insufficant funds')
        else:
            print(f'Here is your ${value}')
            self.balance -= value
    def get_balance(self):
        return self.balance
    
    def set_balance(self, new_balance):
        self.balance = new_balance
    
    def get_owner(self):
        return self.owner
    
    def set_owner(self, new_owner):
        self.owner = new_owner

    def __str__(self):
        return f'owner: {self.get_owner()}, balance: {self.get_balance()}'

    def __add__(self, other):
        new_owner = f'{self.get_owner()} & {other.get_owner()}'
        new_balance = self.get_balance() + other.get_balance()
        new_account = BankAccount(new_owner,new_balance)
        return new_account
    
    def __eq__(self, other):
        return self.get_owner() == other.get_owner()
    
    def give_intrest(self):
        self.balance = self.balance + self.balance * self.rate





matt_acc = BankAccount('matt')
matt_acc.deposit(100)
matt_acc.deposit(50)
# matt_acc.withdraw(215)
# print(matt_acc.get_balance())

ashley_acc = BankAccount('Ashley', 500)
ashley_acc.deposit(250)
print(ashley_acc)
ashley_acc.give_intrest()
print(ashley_acc)

'''# print(matt_acc == ashley_acc)
# other_acc = BankAccount('???', 100)
# print(ashley_acc.get_balance())

# joint_acc = matt_acc + ashley_acc
# print(joint_acc)
# new_acc = joint_acc + other_acc

# print(new_acc)'''





print(matt_acc)
matt_acc.give_intrest()
print(matt_acc)
print(matt_acc.rate)
print(ashley_acc.rate)
