import numpy as np
from modules.alphabet import Alphabet
class Texte:
    def __init__(self):
        self.string = ""
        self.list = []
        self.taille = 1
        self.alphabet = {}
        self.scale = 1


    def set_dimension(self):
        self.taille = len(self.string)

    def set_scale(self, scale):
        self.scale = scale

    def set_list(self):
        for elt in self.string:
            self.list.append(self.alphabet[elt])
    
    def set_name(self, string):
        self.string = string

    def set_alphabet(self):
        alp= Alphabet()
        alp.extraire_points(self.scale)
        self.alphabet = alp.dic_points


    def set(self, string, scale):
        #set applique tout les autres set et on appelle que lui
        self.set_scale(scale)
        self.set_alphabet()
        self.set_name(string)
        self.set_dimension()
        self.set_list()



