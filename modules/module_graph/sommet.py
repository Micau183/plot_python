import random as rd
class Sommet:
    def __init__(self, name, pos_x=None, pos_y=None):
        self.is_fixed = False
        self.name = name
        self.pos_x = pos_x if pos_x is not None else rd.random()
        self.pos_y = pos_y if pos_y is not None else rd.random()
        self.voisins = []
        self.visited = False
        self.parent = None

    def set_name(self, name):
        self.name = name

    def set_pos(self, pos):
        if not self.is_fixed:
            x, y = pos 
            self.pos_x = x
            self.pos_y = y 
        else: 
            print ("Le sommet %s, est fixé", self.name)
    def ajoute_voisin(self, sommet):
        self.voisins.append(sommet)
    
    def fix(self, pos):
        x, y = pos 
        self.pos_x = x
        self.pos_y = y 
        self.is_fixed = True
    def get_pos_x(self):
        return self.pos_x
    
    def get_pos_y(self):
        return self.pos_y

