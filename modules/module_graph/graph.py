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
    

    def get_index(self, sommet):
        for i in range(len(self.sommets)):
            if self.sommets[i] == sommet:
                return i
          
   
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

        return a[0]

        
    def adjacency_matrix(self):
        # Nombre de sommets dans le graphe
        n = len(self.sommets)

        # Initialisation de la matrice d'adjacence avec des zéros
        adj_matrix = np.zeros((n, n), dtype=int)

        # Remplissage de la matrice d'adjacence en fonction des arêtes
        for arete in self.aretes:
            sommet1, sommet2 = arete.debut, arete.fin # arete est une paire (i, j)
            i = self.get_index(sommet1)
            j = self.get_index(sommet2)
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1  # Si le graphe est non orienté

        self.adjancy = adj_matrix
                

    def degree_matrix(self):
        num_nodes = len(self.adjancy)
        degree_matrix = np.zeros((num_nodes, num_nodes))

        for i in range(num_nodes):
            degree_matrix[i, i] = np.sum(self.adjancy[i, :])

        return degree_matrix





    def trouve_triangle(self):
        triangles = []

        # Create an adjacency list for quick neighbor lookup
        adjacency_list = {sommet.name: set() for sommet in self.sommets}
        for arete in self.aretes:
            adjacency_list[arete.debut.name].add(arete.fin.name)
            adjacency_list[arete.fin.name].add(arete.debut.name)

        # Iterate through all triples of vertices
        for i in range(len(self.sommets)):
            for j in range(i + 1, len(self.sommets)):
                for k in range(j + 1, len(self.sommets)):
                    sommet1, sommet2, sommet3 = self.sommets[i], self.sommets[j], self.sommets[k]

                    # Check if there is an edge between every pair of vertices in the triple
                    if sommet2.name in adjacency_list[sommet1.name] and sommet3.name in adjacency_list[sommet1.name] \
                            and sommet3.name in adjacency_list[sommet2.name]:
                        triangle = (sommet1, sommet2, sommet3)
                        triangles.append(triangle)

        return triangles

    def sum_sommet(self, liste):
        somme = 0
        for i in range(len(liste)):
            somme += liste[i].get_nb_voisins()
        return somme
    
    def plus_de_voisins(self, triangles):
        max_triangle = triangles[0]
        max = self.sum_sommet(triangles[0])
        for i in range(len(triangles)):
            somme = self.sum_sommet(triangles[i]) 
            if somme > max:
                max = somme
                max_triangle = triangles[i]

        return max_triangle
    
    def to_indice(self, triangle):
        liste_indice = []
        for sommet in triangle:
            for i in range(len(self.sommets)):
                if self.sommets[i] == sommet:
                    liste_indice.append(i)
        return liste_indice


    def plongement_tutte_triangle(self):
        self.name = "tutte_triangle" + str(self.get_nb_sommets()) + "_" + str(self.get_nb_aretes())

        #On prends la liste de tous les triangles et on prend celui dont la somme des sommets est la 
        #plus élevé 
        triangles = self.trouve_triangle()
        triangle = self.plus_de_voisins(triangles)

        #On travaille avec des indices pour simplifier le code

        outerface = np.array(self.to_indice(triangle))
        n = self.get_nb_sommets()
        #liste des indices des sommets qui ne sont pas sur la face extérieure
        inner = np.array([i for i in range(n) if i not in outerface])

        self.adjacency_matrix()
        #on crée la matrice laplacienne et on fait le calcul théorique pour trouver les positions
        #chercher théorème de tutte sur google 
        L = np.array(self.degree_matrix() - self.adjancy)
        L1 = L[inner][:,inner]
        Q = L[inner][:, outerface]
        print(L1)
        L1_inverse = np.linalg.inv(L1)

        P = np.zeros((n,2))


        circle = self.circle_points(3)
        for i,v in enumerate(outerface):
            P[v] = circle[i]
        P[inner] = -L1_inverse @ Q @ P[outerface]

        for i in range(n):
            self.sommets[i].set_pos((P[i,0], P[i,1]))


    def circle_points(self, entier):
        liste = []
        for i in range(entier):
            pos_x = 0.5 * (np.cos(2 * np.pi * i / entier) + 1)
            pos_y = 0.5 * (np.sin(2 * np.pi * i / entier) + 1)
            
            # Assuming face[i].fix() updates the position of the vertex in the graph
            liste.append([pos_x, pos_y])
        return np.array(liste)
