from modules.module_graph.sommet import Sommet
class Arete:
    def __init__(self, sommet1, sommet2):
        self.debut = sommet1
        self.fin = sommet2


    def arete(self, debut, fin):
        self.debut = debut
        self.fin = fin
    
    def get_debut(self):
        return self.debut
    
    def get_fin(self):
        return self.fin