import numpy as np
class Texte:
    def __init__(self):
        self.string = ""
        self.list = []
        self.taille = 1
        self.alphabet = {
    '0': [[3,1],[4, 1], [2,2], [2,3], [2,4], [2,5], [5,2], [5,3], [5,4], [5,5],[3,6],[4, 6]],
    '1': [[3,1],[2,2],[3,2],[3,3],[3,4],[3,5],[3,6],[2,6],[4,6]],
    '2': [[1,2],[2,1],[3,1],[4,2],[4,3],[3,4],[2,5],[1,6],[1,7],[2,7],[3,7],[4,7]]
        }
    def set_dimension(self):
        self.taille = len(self.string)

    def set_list(self):
        for elt in self.string:
            self.list.append(self.alphabet[elt])
    
    def set_name(self, string):
        self.string = string

    def set(self, string):
        self.set_name(string)
        self.set_dimension()
        self.set_list()


