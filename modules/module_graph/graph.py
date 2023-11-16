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
        self.cycles = []
        self.adjancy = []

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
    
    def set_voisins(self):
        for sommet in self.sommets:
            for arete in self.aretes:
                if arete.debut == sommet:
                    sommet.ajoute_voisin(arete.fin)
                elif arete.fin == sommet:
                    sommet.ajoute_voisin(arete.debut)
    


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


    def remonte_parent(self, cycle, sommet, dernier):
        cycle.append(sommet)
        if sommet.parent is None:
            #print(cycle)
            return cycle
        elif sommet.parent == dernier:
            cycle.append(sommet.parent)
            return cycle
        else:
            return self.remonte_parent(cycle, sommet.parent, dernier)


    def dfs(self, sommet, pile, cycles):
        sommet.visited = True
        
        pile.append(sommet)
        while pile != []:
            s = pile.pop()
            #print("Je commence à "+s.name)

            
            #print(s.voisins)
            for voisin in s.voisins:
                #print("Je visite "+voisin.name)
                if voisin.visited:
                    #print(voisin.name+" a déjà été visité")
                    
                    cyc = self.remonte_parent([], s, dernier=voisin)
                    #print(cyc)
                    self.ajoute_cycle(cyc)

                else:
                    #print(voisin.name+" n'a jamais été visité")
                    voisin.parent = s
                    voisin.visited = True
                    pile.append(voisin)
                    self.dfs(voisin, pile, cycles)
    
    def ajoute_cycle(self, cycle):
        if len(cycle) > 2 and not(cycle in self.cycles):
            self.cycles.append(cycle)

    def cycles_fermes(self, sommet):
        self.set_voisins()
        self.dfs(sommet, [], [])
    
    def plus_grand_cycle(self):
        self.cycles_fermes(self.sommets[0])
        return max(self.cycles, key=len)


        
    def adjacency_matrix(self):
        # Nombre de sommets dans le graphe
        n = len(self.sommets)

        # Initialisation de la matrice d'adjacence avec des zéros
        adj_matrix = np.zeros((n, n), dtype=int)

        # Remplissage de la matrice d'adjacence en fonction des arêtes
        for arete in self.aretes:
            i, j = arete  # arete est une paire (i, j)
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1  # Si le graphe est non orienté

        self.adjancy = adj_matrix
                
    def degree_matrix(self):

        degree_vector = np.sum(self.adjacency, axis=1)
        degree_matrix = np.diag(degree_vector)

        return degree_matrix

                


    def plongement_tutte(self):
        face = self.plus_grand_cycle()
        nb_sommet = len(face)
        for i in range(nb_sommet):
            face[i].fix((0.5 * (np.cos(2 * np.pi * i / nb_sommet) + 1), 0.5 * (np.sin(2 * np.pi * i / nb_sommet) + 1)))
            
        inner = [i for i in range(self.get_nb_sommets)]