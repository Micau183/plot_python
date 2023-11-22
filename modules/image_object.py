import numpy as np
from modules.algorithm.bresenham import Bresenham
from modules.algorithm.midpointcircle import MidpointCircle
from modules.texte import Texte
from modules.module_graph.graph import Graph as g
from modules.module_graph.sommet import Sommet as s
from modules.module_graph.arete import Arete as a
import matplotlib.pyplot as plt
import time 
class Image_object:
    def __init__(self):
        self.image = []
        self.longueur = 0
        self.hauteur = 0
        self.name = "image"
        self.img_obj_liste = []
        self.x = 0
        self.y = 0
        self.epaisseur = 1
        self.scale =1


    def image_blanche(self, hauteur, longueur, scale=1, epaisseur=1):
        # On créée une image blanche et on set up les dimensions et l'autoscale

        self.longueur = longueur
        self.hauteur = hauteur
        self.image = np.full((self.hauteur, self.longueur, 3), 255, dtype=np.uint8)
        self.set_scale(scale)

        #gestion de l'epaisseur automatique (pas très propre j'avoue)
        if epaisseur is None or epaisseur =='auto':
            self.set_epaisseur()
        else:
            self.epaisseur = epaisseur
    

    def set_scale(self, scale):
        #gestion du scale auto
        if scale =='auto':
            self.scale = self.autoscale()
        else:
            self.scale = scale
        if self.scale == 0:
            self.scale = 1 

    def set_epaisseur(self):
        #ça casse dans text_plot si je laisse le if, c'est pour ça que je le fais en deux temps
        # if self.epaisseur =='auto':
        self.epaisseur = int(np.log2(self.scale+1))
        if self.epaisseur >3:
            self.epaisseur = 3
        if self.epaisseur<=0:
            self.epaisseur = 1
    
    def ligne_hori(self, x, epaisseur=1, couleur='noir'):
        #droite horizontale à la hauteur x

        for indice in range(self.longueur):
            self.ajoute_point(indice, x, epaisseur, couleur)

    def ligne_vert(self, indice, epaisseur=1, couleur='noir'):
        #droite verticale à au pixel de longueur 'indice

        for y in range(self.hauteur):
            self.ajoute_point(indice, y, epaisseur, couleur)

    def segment_vert(self, indice, start, end, epaisseur=1, couleur='noir'):
        #segment verticale à la hauteur 'indice qui va de 'start' à 'end'

        for y in range(end-start):
            self.ajoute_point(indice, y+ start, epaisseur, couleur)
    
    def segment_hori(self, indice, start, end, epaisseur=1, couleur='noir'):
        #segment horizontale à la hauteur 'indice qui va de 'start' à 'end'

        for x in range(end-start):
            self.ajoute_point(x+start, indice, epaisseur, couleur)

    def border(self, epaisseur=1, couleur='noir'):
        #Créer des bordures à l'aide de quatres droites autour d'une image

        self.ligne_hori(0, epaisseur=epaisseur, couleur=couleur)
        self.ligne_hori(self.hauteur -1, epaisseur=epaisseur, couleur=couleur)
        self.ligne_vert(0, epaisseur=epaisseur, couleur=couleur)
        self.ligne_vert(self.longueur -1, epaisseur=epaisseur, couleur=couleur)

    def ajoute_point(self, x, y, epaisseur=1, couleur='noir'):

        #ajoute un point à l'indice (x, y)

        #on regarde la couleur, en fonction de si l'argument est un tuple ou un string
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

        if 0 <= x < self.image.shape[1] and 0 <= y < self.image.shape[0]:
            self.image[y,x] = color

       # Boucle extérieure pour l'épaisseur du flou
        for r in range(epaisseur):
            # Boucle pour parcourir les colonnes du carré autour du pixel (x, y)
            for dx in range(-r, r + 1):
                # Boucle pour parcourir les lignes du carré autour du pixel (x, y)
                for dy in range(-r, r + 1):
                    # Calcul des nouvelles coordonnées (new_x, new_y) du pixel à modifier
                    new_x, new_y = x + dx, y + dy

                    # Vérification que les nouvelles coordonnées sont à l'intérieur des limites de l'image
                    if 0 <= new_x < self.image.shape[1] and 0 <= new_y < self.image.shape[0]:
                        # Définition de l'intensité de modification des couleurs
                        # Si r == 0 (au centre du carré), une augmentation importante de l'intensité est appliquée (100, 100, 100)
                        # Sinon, une augmentation moins importante est appliquée (30, 30, 30)
                        delta_intensity = [100, 100, 100] if r == 0 else [30, 30, 30]

                        # Calcul du nouveau pixel en soustrayant delta_intensity à l'image d'origine
                        # et en prenant la valeur maximale entre la nouvelle valeur et la couleur d'origine
                        nouveau_pixel = np.maximum(self.image[new_y, new_x] - delta_intensity, color)

                        # Affectation du nouveau pixel à la position (new_x, new_y) dans l'image
                        self.image[new_y, new_x] = nouveau_pixel


    def plot_fonction(self, f, start_x=0, end_x=10, epaisseur='auto', couleur='bleu', scale ='auto'):
        #On sépare le plot en 4 parties, le titre, l'axe des ordonnées, l'axe des abscisse et le plot
        # de la fonction
        
        #J'ai modifié le code pour le scale et epaisseur auto donc c'est un peu dégeu
        titre = Image_object()
        titre.image_blanche(int(self.hauteur/10), self.longueur, epaisseur=epaisseur, scale = scale)
        titre.text_plot("Fonction : " +str(f),scale = titre.autoscale()+1, epaisseur = epaisseur)

        
        fonction = Image_object()
        fonction.image_blanche(int(self.hauteur*8/10), int(self.longueur*8/10), epaisseur=epaisseur, scale = scale)
        fonction.border()

        abscisse = Image_object()
        abscisse.image_blanche(int(self.hauteur/10),int(self.longueur*8/10), epaisseur=epaisseur, scale = scale)
        #abscisse.border(couleur='bleu', epaisseur=1)

        ordonee = Image_object()
        ordonee.image_blanche(int(self.hauteur*8/10), int(self.longueur/10), epaisseur=epaisseur, scale = scale)
        #ordonee.border(couleur='rouge', epaisseur=1)
        

        self.name = str(f)


        X = np.linspace(start_x, end_x, fonction.longueur)

        abscisse.plot_abscisse(10, start_x, end_x, scale=scale, epaisseur=epaisseur)
        
        Y = f(X)


        
        # Coefficient de mise à l'échelle pour la hauteur de l'image
        coeff = 0.9
        
        mini = min(Y)
        maxi = max(Y)
        
        rangeY = maxi - mini
        
        
        # Calcule le ratio de mise à l'échelle pour adapter Y à la hauteur de l'image
        ratio = fonction.hauteur * coeff / rangeY
        
        # Ajuste les valeurs Y en fonction de la hauteur de l'image
        Y = (Y - mini) * ratio
        
        # Calcule l'ajustement pour positionner la courbe verticalement
        ajust = fonction.hauteur * ((1 - coeff) / 2)
        
        #Alors ça, c'est dégeu et ça marche pas il faut "juste" mettre les valeurs min et max en 
        #ordonné de la fonction
        new_range = rangeY/coeff
        ordonee.plot_ordonee(10, mini-(1-coeff)*new_range*0.5, maxi+(1-coeff)*new_range, scale=scale, epaisseur=epaisseur)

        #plot de la fonction   
        for i in range(fonction.longueur):
            y_coord = int(Y[i] + ajust)
            x_coord = int(i)
            
            #le -1 c'est un terme correctif au feeling
            fonction.ajoute_point(x_coord, y_coord,epaisseur=fonction.epaisseur-1, couleur = couleur)

        #On ajoute les 4 régions à l'image initiale
        self.add_region(fonction, int(self.hauteur/10), int(self.longueur/10))
        self.add_region(abscisse, 0, int(self.longueur/10))
        self.add_region(ordonee, int(self.hauteur/10), 0)
        self.add_region(titre, int(self.hauteur*9/10), 0)

        self.combine_region()

    def combine_region(self):
        #On combine les régions qui sont dans la liste
        for img in self.img_obj_liste:
            for i in range(img.hauteur):
                for j in range(img.longueur):
                    #Test pour savoir si les "sous-images" dépassent pas, on plot pas ce qui dépasse
                    if 0 <= img.x + i < self.hauteur and 0 <= img.y + j < self.longueur:
                        self.image[img.x + i][img.y + j] = img.image[i][j]


    def add_region(self, img_obj, x, y):
        #Ajout d'une région à la liste des régions et aux coordonnées voulues
        img_obj.x = x
        img_obj.y = y
        self.img_obj_liste.append(img_obj)

    def autoscale(self):
        #La valeur 51 est du pur feeling mais ça passe plutôt bien
        mini = min(self.hauteur, self.longueur)
        a = int(mini/51)
        return int(mini/51)
    

    def text_plot(self, string, epaisseur=None, couleur ='noir', pos='center', scale='auto'):
        self.set_scale(scale)
        #print(self.scale)

       #On crée un objet Text et on met .upper parce que j'ai pas encore mis les minuscules
        self.name = string
        textplot = Texte()
        textplot.set(string.upper(), self.scale)
        
        #On crée un image_object de la taille du mot (la taille d'une lettre est 8*6)
        img_obj = Image_object()
        img_obj.image_blanche(8*self.scale, 6* textplot.taille*self.scale)
        
        
        #gestion de l'epaisseur auto
        if epaisseur is None or epaisseur =='auto':
                self.set_epaisseur()
                #print(self.epaisseur)
        else:
            self.epaisseur = epaisseur

        ep = self.epaisseur

        #Pour chaque lettre du mot on crée un nouvel Image_object() et on les ajoute au grand
        #c'est surement pas opti, on pourrait surement tout rajouter directement sur le Image_object du mot

        for i in range(textplot.taille):
            subplot = Image_object()
            subplot.image_blanche(8*self.scale, 6*self.scale)
            

            liste_point = textplot.list[i]
            for j in range(len(liste_point)):
                subplot.ajoute_point(liste_point[j][0], liste_point[j][1], ep, couleur=couleur)

            # plt.imshow(subplot.image)
            # plt.show()
            img_obj.add_region(subplot, 0, 6*i*self.scale)
        img_obj.combine_region()
        
        #On regarde où on veut positionner le mot dans le plot initial
        if isinstance(pos, list):
            x_center, y_center = pos
        elif  pos =='corner':
            x_center = 0
            y_center = 0
        elif pos =='center':
            x_center = int(self.hauteur/2)
            y_center = int((self.longueur-img_obj.longueur)/2)

        self.add_region(img_obj,x_center, y_center)
        self.combine_region()

    def plot_abscisse(self, nb_points, start_x, end_x, scale = 1, epaisseur = 1):
        #On fait des ptits traits de la taille de 1/4 de hauteur du plot
        liste = np.linspace(0, self.longueur, nb_points)
        pas = (end_x - start_x)/nb_points
        for i in range(nb_points-1):
            
            self.segment_vert(int(liste[i]), int(self.hauteur*3/4), int(self.hauteur))
            #print(str(start_x + pas*i))
            self.text_plot(str(start_x + pas*i)[:5], pos =[int(self.hauteur*2/4), int(liste[i])], scale = scale, epaisseur = epaisseur)

    def plot_ordonee(self, nb_points, start_y, end_y, scale=1, epaisseur = 1):
        #On fait des ptits traits de la taille de 1/4 de longueur du plot

        liste = np.linspace(0, self.hauteur, nb_points)
        pas = (end_y - start_y)/nb_points
        for i in range(nb_points-1):
            
            self.segment_hori(int(liste[i]), int(self.longueur*3/4), int(self.longueur))
            #print(str(start_y + pas*i))
            self.text_plot(str(round(start_y + pas*i, 1)), pos =[int(liste[i]), int(self.longueur*2/4)], scale = scale, epaisseur = epaisseur)
        
    def circle(self, rayon, x, y, epaisseur = 1, couleur='noir', fill_color =None):
        midpoint_circle = MidpointCircle(rayon)
        circle_points = midpoint_circle.get_circle()
        #print(circle_points)
        if fill_color != None:
            print("ici")
            liste_lignes = midpoint_circle.fill_circle(circle_points)

            for ligne in liste_lignes:
                print(ligne)
                self.line(ligne[0,0]+x, ligne[0,1]+y, ligne[1,0]+x, ligne[1,1]+y, epaisseur=1, couleur=fill_color)

        for i in range(len(circle_points)):
            self.ajoute_point(circle_points[i][0]+x, circle_points[i][1]+y, epaisseur, couleur=couleur)

        
    def line(self, x0, y0, x1, y1, epaisseur=1, couleur='noir'):
        bresenham_line = Bresenham(x0, y0, x1, y1)
        line_points = bresenham_line.get_line()
        #print(line_points)
        for i in range(len(line_points)):
            #print(line_points[i][0])
            
            self.ajoute_point(line_points[i][0], line_points[i][1], epaisseur, couleur=couleur)
    
    def plot_graph(self, graph, rayon = 20, epaisseur = 2, fill_color =None):
        self.name = graph.name

        adapt_hauteur = self.hauteur *0.9
        adapt_longueur = self.longueur *0.9
        
        for i in range(graph.get_nb_aretes()):
            #print(i)

            arete = graph.get_arete(i)

            debut = arete.get_debut()
            fin = arete.get_fin()

            

            x0 = int(debut.get_pos_x() * adapt_longueur + rayon)
            y0 = int(debut.get_pos_y() * adapt_hauteur + rayon)

            x1 = int(fin.get_pos_x() * adapt_longueur + rayon)
            y1 = int(fin.get_pos_y() * adapt_hauteur + rayon)

            self.line(x0, y0, x1, y1, epaisseur = epaisseur)
            

        for i in range(graph.get_nb_sommets()):
            #print(i)
            sommet = graph.get_sommet(i)

            x = int(sommet.get_pos_x()* adapt_longueur)
            y = int(sommet.get_pos_y()* adapt_hauteur)

            if sommet.couleur != None:
                fill_color = sommet.couleur

            self.circle(rayon, x, y, epaisseur = epaisseur, fill_color =fill_color)


def test():
    img = Image_object()
    img.image_blanche(300, 1000)
    img.plot_fonction(np.sin)
    #plt.imshow(img.image)
    #plt.show()

    





        


    
