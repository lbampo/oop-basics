from animal_class import*

class Reptile(Animal): # Inheritance
    # Runs all the same methods as animal because that is all it knows

    def __init__(self, name, colour, number_hearts, camouflage, eyes = 2):
        super().__init__(name,colour,eyes)
        self.number_hearts = number_hearts
        self.camo = camouflage



    def hunting(self,):
        return f'waiiiit forrrrr ittt..... waitttttt forrr itttttt....... POUNCE on the '

    # def seek_heat(self):

