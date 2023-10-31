import numpy as np
import matplotlib.pyplot as plt

class Image_object:
    def __init__(self):
        self.image = []
        self.longueur = 0
        self.hauteur = 0
        self.name = "image"
        self.img_obj_liste = []
        self.x = 0
        self.y = 0


    def image_blanche(self, hauteur, longueur):
        self.longueur = longueur
        self.hauteur = hauteur
        self.image = np.full((self.hauteur, self.longueur, 3), 255, dtype=np.uint8)

    def ligne_hori(self, x, epaisseur=1, couleur='noir'):
        for indice in range(self.longueur):
            self.ajoute_point(indice, x, epaisseur, couleur)

    def ligne_vert(self, indice, epaisseur=1, couleur='noir'):
        for y in range(self.hauteur):
            self.ajoute_point(indice, y, epaisseur, couleur)

    def border(self, epaisseur=1, couleur='noir'):
        self.ligne_hori(0, epaisseur=epaisseur, couleur=couleur)
        self.ligne_hori(self.hauteur -1, epaisseur=epaisseur, couleur=couleur)
        self.ligne_vert(0, epaisseur=epaisseur, couleur=couleur)
        self.ligne_vert(self.longueur -1, epaisseur=epaisseur, couleur=couleur)

    def ajoute_point(self, x, y, epaisseur=2, couleur='noir'):
        if isinstance(couleur, str):
            if couleur == 'noir':
                color = [0, 0, 0]
            elif couleur == 'rouge':
                color = [0, 0, 255]
            elif couleur == 'vert':
                color = [0, 255, 0]
            elif couleur == 'bleu':
                color = [255, 0, 0]
            elif couleur == 'jaune':
                color = [0, 255, 255]
            else:
                raise ValueError("Couleur non prise en charge")
        elif isinstance(couleur, (list, tuple)) and len(couleur) == 3:
            color = list(couleur)
        else:
            raise ValueError("Couleur invalide")

        self.image[y, x] = color

        for r in range(epaisseur):
            for dx in range(-r, r + 1):
                for dy in range(-r, r + 1):
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < self.image.shape[1] and 0 <= new_y < self.image.shape[0]:
                        delta_intensity = [100, 100, 100] if r == 0 else [30, 30, 30]
                        self.image[new_y, new_x] = np.maximum(self.image[new_y, new_x] - delta_intensity, color)

    def plot_fonction(self, f, start_x=0, end_x=10, epaisseur=2, couleur='bleu'):
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
            
            self.ajoute_point(x_coord, y_coord,epaisseur=epaisseur, couleur = couleur)

    def combine_region(self):
        for img in self.img_obj_liste:
            for i in range(img.hauteur):
                for j in range(img.longueur):
                    self.image[img.x + i][img.y + j] = img.image[i][j]

    def add_region(self, img_obj, x, y):
        img_obj.x = x
        img_obj.y = y
        self.img_obj_liste.append(img_obj)
        



def test():
    img = Image_object()
    img.image_blanche(300, 1000)
    img.plot_fonction(np.sin)
    plt.imshow(img.image)
    plt.show()

    





        


    
