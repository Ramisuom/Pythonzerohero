class Dog():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name):

        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name


    #OPERATIONS/ACTIONS ---> Methods
    def bark(self,number):
        print('WOOF! My name is {} and the number is {}'.format(self.name,number))

my_dog = Dog('lab','Frankie')

print(type(my_dog))
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark(number=3))

class Circle():
    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):

        self.radius = radius
        self.area = radius*radius*Circle.pi

    #Method
    def get_circumfrence(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumfrence())
print(my_circle.area)

class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am an eating')

class Dog(Animal):

    def __init__(self):
        def __init__(self):
            Animal.__init__(self)
            print('Dog created')

    def bark(self):
        print('WOOF!')

    def who_am_i(self):
        print('I am a dog!')

my_dog = Dog()

my_dog.eat()
myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()
my_dog.who_am_i()
my_dog.bark()