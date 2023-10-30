import numpy as np
import matplotlib.pyplot as plt

class Image_object:
    def __init__(self):
        self.image = []
        self.longueur = 0
        self.hauteur = 0

    def image_blanche(self, hauteur, longueur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.image = np.full((self.hauteur, self.longueur, 3), 255, dtype=np.uint8)

    def ligne_hori(self, indice):
        ligne = np.array([[0, 0, 0] for _ in range(self.longueur)])
        self.image[indice] = ligne

    def ligne_vert(self, indice):
        ligne = np.array([[0, 0, 0] for _ in range(self.hauteur)])
        self.image[:, indice] = ligne

    def plot_fonction(self, f):
        X = np.linspace(0, 10, self.longueur )
        Y = f(X)
        
        # Normalisation des valeurs de Y en fonction de la hauteur
        mini = min(Y)
        maxi = max(Y)
        rangeY = maxi - mini 
        ratio = self.hauteur / (rangeY +1/self.hauteur) #terme correctif du feeling
        Y = (Y-mini) * ratio
        print(X)
        print(Y)
        
        for i in range(self.longueur):

            self.image[int(Y[i]),int(i)] = [0, 0, 0]


def test():
    img = Image_object()
    img.image_blanche(300, 300)
    img.plot_fonction(np.sin)
    plt.imshow(img.image)
    plt.show()
test()
    





        


    
