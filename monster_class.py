class Monsters():



    # characteristics
    def __init__(self, name, eyes, alive, fur, list,  cute):
        self.name = name
        self.number_eyes = eyes
        self.alive = alive
        self.fur_type = fur
        self.characteristics = list
        self.cuteness = cute


    # Behaviours - Functions that belong to a class

    def eat(self, food):
        return f'NOM NOM NOM {food}'

    def scare(self):
        return 'RAWRRRRRRRRR'

    def mating_call (self):
        return "OOOO LOOK AT MEEE, YOU WANT SOME OF THIS DON'T YOU"

    def potty(self):
        return 'anddddddd PUSHHHHHHHHH'

    def play(self):
        return 'HAHA RAWWW HAHAHAH'

#Lets create an object of class animal
 #   Initialising an object

# my_monster = Monsters() # Created an instance of class Animal

# print(my_monster)
# print(type(my_monster))