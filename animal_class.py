class Animal():



    # characteristics
    def __init__(self, name, colour, eyes = 2):
        self.name = name
        self.colour = colour
        self.number_eyes = eyes
        self.alive = True
        self.number_animal_eaten = 0
        self.age = 0

    # Behaviours - Functions that belong to a class

    def eat(self, food):
        return f'NOM NOM NOM {food}'

    def sleep(self):
        return 'ZzzzzZZZZzzz'#

    def hunt(self):
        return 'ATTTTACKKKKK'

    def potty(self):
        return 'anddddddd PUSHHHHHHHHH'

    def play(self):
        return 'HAHA RAWWW HAHAHAH'

# Lets create an object of class animal
    # Initialising an object

# my_animal = Animal() # Created an instance of class Animal
# #
# print(my_animal)
# print(type(my_animal))