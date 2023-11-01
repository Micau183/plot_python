import numpy as np
from modules.alphabet import Alphabet
class Texte:
    def __init__(self):
        self.string = ""
        self.list = []
        self.taille = 1
        self.alphabet = {}
    def set_dimension(self):
        self.taille = len(self.string)

    def set_list(self):
        for elt in self.string:
            self.list.append(self.alphabet[elt])
    
    def set_name(self, string):
        self.string = string

    def set_alphabet(self):
        alp= Alphabet()
        alp.extraire_points()
        self.alphabet = alp.dic_points
    def set(self, string):
        self.set_alphabet()
        self.set_name(string)
        self.set_dimension()
        self.set_list()


