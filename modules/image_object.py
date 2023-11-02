import numpy as np
from modules.texte import Texte
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
                        nouveau_pixel = np.maximum(self.image[new_y, new_x] - delta_intensity, color)
                        #print(nouveau_pixel)
                        self.image[new_y, new_x] = nouveau_pixel

    def plot_fonction(self, f, start_x=0, end_x=10, epaisseur=2, couleur='bleu', coeff=0.9):

        legende= Image_object()
        legende.image_blanche(int(self.hauteur/10), self.longueur)

        abscisse =Image_object()
        abscisse.image_blanche(int(self.hauteur/10), self.longueur)

        ordonee = Image_object()
        ordonee.image_blanche(self.hauteur, int(self.longueur/10))
        
        fonction = Image_object()
        fonction.image_blanche(int(self.hauteur*8/10), int(self.longueur*8/10))
        
        fonction.border()
        
        self.name = str(f)

        X = np.linspace(start_x, end_x, fonction.longueur)

        Y = f(X)

        
            
        # Coefficient de mise à l'échelle pour la hauteur de l'image
        
        
        mini = min(Y)
        maxi = max(Y)
        rangeY = maxi - mini
        
        # Calcule le ratio de mise à l'échelle pour adapter Y à la hauteur de l'image
        ratio = fonction.hauteur * coeff / rangeY
        
        # Ajuste les valeurs Y en fonction de la hauteur de l'image
        Y = (Y - mini) * ratio
        
        # Calcule l'ajustement pour positionner la courbe verticalement
        ajust = fonction.hauteur * ((1 - coeff) / 2)
        
        for i in range(fonction.longueur):
            y_coord = int(Y[i] + ajust)
            x_coord = int(i)
            
            fonction.ajoute_point(x_coord, y_coord,epaisseur=epaisseur, couleur = couleur)
        
        

    def combine_region(self):

        for img in self.img_obj_liste:
                
            # plt.imshow(img.image)
            # plt.show()
            for i in range(img.hauteur):
                for j in range(img.longueur):
                    if not np.array_equal(img.image[i][j], [255, 255, 255]):
                        self.image[img.x + i][img.y + j] = img.image[i][j]
                    #print(img.image[i][j])

    def add_region(self, img_obj, x, y):
        img_obj.x = x
        img_obj.y = y
        self.img_obj_liste.append(img_obj)

    def text_plot(self, string, epaisseur=1, couleur ='noir'):
        self.name = string
        textplot = Texte()
        textplot.set(string.upper())
        
        
        self.image_blanche(8, 6* textplot.taille)
        print(self.hauteur)
        print(self.longueur)
        for i in range(textplot.taille):
            subplot = Image_object()
            subplot.image_blanche(8, 6)
            liste_point = textplot.list[i]
            for j in range(len(liste_point)):
                subplot.ajoute_point(liste_point[j][0], liste_point[j][1], epaisseur=epaisseur, couleur=couleur)

            # plt.imshow(subplot.image)
            # plt.show()
            self.add_region(subplot, 0, 6*i)
        self.combine_region()

    
        




        



def test():
    img = Image_object()
    img.image_blanche(300, 1000)
    img.plot_fonction(np.sin)
    #plt.imshow(img.image)
    #plt.show()

    





        


    
