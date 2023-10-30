import numpy as np
import os

class Bmp_renderer:
    def __init__(self):
        self.largeur = 10
        self.hauteur = 10
        self.donnees = []
        self.taille_fichier = 354
        self.image = np.zeros((10, 10, 3), dtype=np.uint8)
        self.entete = []
    
    def creation_image(self, largeur, hauteur):
        self.set_dimension(largeur, hauteur)
        self.set_taille_fichier()
        self.set_image()

    def set_dimension(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        
    
    def set_taille_fichier(self):
        self.taille_fichier = 54 + (self.largeur * self.hauteur * 3)
    
    def set_image(self):
        self.image = np.full((self.largeur, self.hauteur, 3), 255, dtype=np.uint8)


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
    
            # Largeur de l'image (4 octets)
        self.entete.extend([
        (self.largeur & 0xFF),             
        (self.largeur >> 8) & 0xFF,        
        (self.largeur >> 16) & 0xFF,       
        (self.largeur >> 24) & 0xFF       
        ])

        # Hauteur de l'image (4 octets)
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
        if not os.path.exists('output'):
            os.makedirs('output')

        name = f'output/image{self.largeur}_{self.hauteur}.bmp'
        with open(name, 'wb') as fichier:
            fichier.write(bytearray(self.donnees))
    
    def test_rendu(self, largeur, hauteur):
        self.creation_image(largeur, hauteur)
        self.assemble_image()
        self.rendu()

