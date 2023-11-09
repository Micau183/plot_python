from modules.module_graph.arete import Arete
from modules.module_graph.sommet import Sommet
class Graph:
    def __init__(self):
        self.sommets =  []
        self.aretes = []
    
    def add_sommet(self, sommet):
        self.sommets.append(sommet)

    def add_sommet(self, sommet_list):
        self.sommets += sommet_list
