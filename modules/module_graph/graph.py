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

    def trouver_plus_grand_face(self):
        # Créer une liste d'adjacence pour représenter le graphe
        liste_adjacence = {sommet: [] for sommet in self.sommets}
        for arete in self.aretes:
            v1, v2 = arete.debut, arete.fin
            liste_adjacence[v1].append(v2)
            liste_adjacence[v2].append(v1)

        plus_grand_face = []

        # Fonction pour trouver les cycles dans le graphe
        def trouver_cycles(depart, actuel, chemin):
            nonlocal plus_grand_face
            for voisin in liste_adjacence[actuel]:
                if voisin == depart and len(chemin) > 2:
                    chemin.append(depart)
                    if len(chemin) > len(plus_grand_face):
                        plus_grand_face = chemin.copy()
                elif voisin not in chemin:
                    trouver_cycles(depart, voisin, chemin + [voisin])

        # Parcourir chaque sommet pour trouver les cycles et la plus grande face
        for sommet in self.sommets:
            trouver_cycles(sommet, sommet, [sommet])

        for sommet in plus_grand_face:
            print(sommet.name)
        return plus_grand_face

    def plongement_tutte(self, sommets_fixes=None):
        nombre_sommets = len(self.sommets)
        nombre_aretes = len(self.aretes)

        # Créer la matrice d'adjacence
        matrice_adjacence = np.zeros((nombre_sommets, nombre_sommets))
        for arete in self.aretes:
            debut, fin = arete.debut, arete.fin
            indice_debut = self.sommets.index(debut)
            indice_fin = self.sommets.index(fin)
            matrice_adjacence[indice_debut][indice_fin] = 1
            matrice_adjacence[indice_fin][indice_debut] = 1

        # Créer la matrice des degrés
        matrice_degres = np.diag(np.sum(matrice_adjacence, axis=1))

        # Matrice laplacienne
        matrice_laplacienne = matrice_degres - matrice_adjacence

        # Initialiser les positions pour les sommets non fixes
        sommets_non_fixes = []
        for sommet in self.sommets:
            if sommet not in (sommets_fixes or []):
                sommets_non_fixes.append(sommet)

# Ou en utilisant une liste en compréhension pour une syntaxe plus concise :
# sommets_non_fixes = [sommet for sommet in self.sommets if sommet not in (sommets_fixes or [])]

        nombre_non_fixes = len(sommets_non_fixes)
        positions_initiales = np.random.rand(nombre_non_fixes, 2)

        # Créer une correspondance des noms de sommets aux indices
        indices_sommets = {sommet: i for i, sommet in enumerate(self.sommets)}

        # Mettre à jour les positions initiales avec les sommets fixes
        for sommet, position in sommets_fixes.items():
            indice_sommet = indices_sommets[sommet]
            positions_initiales = np.insert(positions_initiales, indice_sommet, position, axis=0)

        # Résoudre pour les positions des sommets non fixes
        x = np.linalg.pinv(matrice_degres) @ matrice_laplacienne @ positions_initiales[:, 0]
        y = np.linalg.pinv(matrice_degres) @ matrice_laplacienne @ positions_initiales[:, 1]

        # Mettre à l'échelle x et y pour les ajuster entre 0 et 1
        x = (x - np.min(x)) / (np.max(x) - np.min(x))
        y = (y - np.min(y)) / (np.max(y) - np.min(y))

        # Créer un dictionnaire pour stocker les positions des sommets
        for i in range(nombre_sommets):
            self.sommets[i].set_pos(x[i], y[i])
      
