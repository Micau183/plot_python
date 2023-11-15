import random as rd
class Sommet:
    def __init__(self, name, pos_x=None, pos_y=None):
        self.name = name
        self.pos_x = pos_x if pos_x is not None else rd.random()
        self.pos_y = pos_y if pos_y is not None else rd.random()

    def set_name(self, name):
        self.name = name

    def set_pos(self, pos):
        x, y = pos 
        self.pos_x = x
        self.pos_y = y 

    def get_pos_x(self):
        return self.pos_x
    
    def get_pos_y(self):
        return self.pos_y

