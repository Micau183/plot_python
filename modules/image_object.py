import numpy as np
import matplotlib.pyplot as plt

class Image_object:
    def __init__(self):
        self.image = []
        self.longueur = 0
        self.hauteur = 0
        self.name = "image"

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

    def ajoute_point(self, x, y, epaisseur=2):
        if epaisseur >= 1:
            self.image[y, x] = [0, 0, 0]

        for r in range(1, epaisseur):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                for i in range(1, r + 1):
                    new_x, new_y = x + i * dx, y + i * dy
                    if 0 <= new_x < self.image.shape[1] and 0 <= new_y < self.image.shape[0]:
                        delta_intensity = [100, 100, 100] if r == 1 else [30, 30, 30]
                        self.image[new_y, new_x] = np.maximum(self.image[new_y, new_x] - delta_intensity, [0, 0, 0])

    def plot_fonction(self, f, start_x=0, end_x=10, epaisseur=2):
        self.name = str(f)

        X = np.linspace(start_x, end_x, self.longueur)
        Y = f(X)
        
        # Coefficient de mise à l'échelle pour la hauteur de l'image
        coeff = 0.9
        
        mini = min(Y)
        maxi = max(Y)
        rangeY = maxi - mini
        
        # Calcule le ratio de mise à l'échelle pour adapter Y à la hauteur de l'image
        ratio = self.hauteur * coeff / rangeY
        
        # Ajuste les valeurs Y en fonction de la hauteur de l'image
        Y = (Y - mini) * ratio
        
        # Calcule l'ajustement pour positionner la courbe verticalement
        ajust = self.hauteur * ((1 - coeff) / 2)
        
        for i in range(self.longueur):
            y_coord = int(Y[i] + ajust)
            x_coord = int(i)
            
            self.ajoute_point(x_coord, y_coord,epaisseur=epaisseur)




def test():
    img = Image_object()
    img.image_blanche(300, 1000)
    img.plot_fonction(np.sin)
    plt.imshow(img.image)
    plt.show()

    





        


    
