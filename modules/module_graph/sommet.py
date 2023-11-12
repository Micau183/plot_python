import random as rd
class Sommet:
    def __init__(self, name):
        self.name = name
        self.pos_x = rd.random()
        self.pos_y = rd.random()

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

