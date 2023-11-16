from modules.module_graph.arete import Arete
from modules.module_graph.sommet import Sommet
import random as rd
import numpy as np
class Graph:
    def __init__(self, sommets=None, aretes=None):
        self.name = "graph"
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
    
    def clique(self, k):
        self.name = "K"+str(k)
        for i in range(k):
            s = Sommet(str(i), 0.5*(np.cos(2*np.pi *i /k)+1), 0.5*(np.sin(2*np.pi *i /k)+1))
            self.add_sommet(s)
            print (i)
        for i in range(k):
            print(i)
            for j in range(i + 1, k):
                #print(i, j)
                a = Arete(self.sommets[i], self.sommets[j])
                self.add_arete(a)

    

    def plongement_tutte(self):
        face = self.trouver_plus_grand_face()
        nb_sommet = len(face)-1
        for i in range(nb_sommet):
            face[i].fix((0.5 * (np.cos(2 * np.pi * i / nb_sommet) + 1), 0.5 * (np.sin(2 * np.pi * i / nb_sommet) + 1)))
            
        