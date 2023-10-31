import numpy as np
import os
from modules.image_object import Image_object


class Bmp_renderer:
    def __init__(self):
        self.hauteur = 10
        self.longueur = 10
        self.donnees = []
        self.taille_fichier = 354
        self.image = np.zeros((10, 10, 3), dtype=np.uint8)
        self.entete = []
    
    def creation_image(self, hauteur, longueur):
        self.set_dimension(hauteur, longueur)
        self.set_taille_fichier()
        self.set_image_default()
    

    def set_dimension(self, hauteur, longueur):
        self.hauteur = hauteur
        self.longueur = longueur

    def set_name(self, name):
        self.name = name
        
    
    def set_taille_fichier(self):
        self.taille_fichier = 54 + (self.hauteur * self.longueur * 3)
    
    def set_image_default(self):
        #à changer et appeller l'image voulu à la place du carré blanc
        self.image = np.full((self.hauteur, self.longueur, 3), 255, dtype=np.uint8)

    def set_image(self, img_obj):
        self.set_dimension(img_obj.hauteur, img_obj.longueur)
        self.set_taille_fichier()
        self.image = img_obj.image
        self.name = img_obj.name

    def assemble_image(self):
        self.set_entete()
        self.set_donnees()

    def set_donnees(self):
        self.donnees = self.entete + self.image.flatten().tolist()
    
    def set_entete(self):
        # En-tête de fichier BMP
        self.entete.extend([66, 77])
    
        # Taille du fichier (4 octets little-endian)
        self.entete.append(self.taille_fichier & 0xFF)
        self.entete.append((self.taille_fichier >> 8) & 0xFF)
        self.entete.append((self.taille_fichier >> 16) & 0xFF)
        self.entete.append((self.taille_fichier >> 24) & 0xFF)
    
        # Champs réservés
        self.entete.extend([0, 0, 0, 0])
    
        # Offset des données d'image (4 octets little-endian)
        self.entete.extend([54, 0, 0, 0])
    
        # Taille de l'en-tête de l'image (4 octets)
        self.entete.extend([40, 0, 0, 0])
    
        # longueur de l'image (4 octets)
        self.entete.extend([
        (self.longueur & 0xFF),            
        (self.longueur >> 8) & 0xFF,        
        (self.longueur >> 16) & 0xFF,       
        (self.longueur >> 24) & 0xFF        
        ])
            # hauteur de l'image (4 octets)
        self.entete.extend([
        (self.hauteur & 0xFF),             
        (self.hauteur >> 8) & 0xFF,        
        (self.hauteur >> 16) & 0xFF,       
        (self.hauteur >> 24) & 0xFF       
        ])

        

        # Plans (2 octets)
        self.entete.extend([1, 0])
    
        # Profondeur des couleurs (2 octets) - 24 bits par pixel
        self.entete.extend([24, 0])
    
        # Type de compression (4 octets)
        self.entete.extend([0, 0, 0, 0])
    
        # Taille des données d'image (4 octets)
        self.entete.extend([0, 0, 0, 0])
    
        # Résolution horizontale (4 octets)
        self.entete.extend([0, 0, 0, 0])
    
        # Résolution verticale (4 octets)
        self.entete.extend([0, 0, 0, 0])
    
        # Nombre de couleurs dans la palette (4 octets)
        self.entete.extend([0, 0, 0, 0])
    
        # Nombre de couleurs importantes (4 octets)
        self.entete.extend([0, 0, 0, 0])
    
    def rendu(self):
        if not os.path.exists('plot_python/output'):
            os.makedirs('plot_python/output')

        name = f'plot_python/output/{self.name}_{self.hauteur}_{self.longueur}.bmp'
        with open(name, 'wb') as fichier:
            fichier.write(bytearray(self.donnees))
    
    def test_rendu(self, hauteur, longueur):
        self.creation_image(hauteur, longueur)
        self.assemble_image()
        self.rendu()

