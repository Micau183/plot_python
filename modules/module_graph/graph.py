from modules.module_graph.arete import Arete
from modules.module_graph.sommet import Sommet
import random as rd
class Graph:
    def __init__(self, sommets=None, aretes=None):
        if sommets is None:
            sommets = []
        if aretes is None:
            aretes = []

        self.sommets = sommets
        self.aretes = aretes

    def add_sommet(self, sommet):
        self.sommets.append(sommet)

    def add_sommets(self, sommet_list):
        for i in range(len(sommet_list)):
            self.sommets.append(sommet_list[i])


    def add_arete(self, arete):
        self.aretes.append(arete)

    def add_aretes(self, arete_list):
        for i in range(len(arete_list)):
            self.aretes.append(arete_list[i])


    def get_nb_aretes(self):
        return len(self.aretes)

    def get_nb_sommets(self):
        return len(self.sommets)
    
    
    def get_aretes(self):
        return self.aretes
    
    def get_arete(self, i):
        return self.aretes[i]
    

    def get_sommets(self):
        return self.sommets
    
    def get_sommet(self, i):
        return self.sommets[i]
    