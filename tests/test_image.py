with open('sample.bmp', 'rb') as fichier:
    donneees = fichier.read()
    #print(donnees)
entete_bmp = donneees[:54]

# Extraire des informations de l'en-tête BMP
largeur = int.from_bytes(entete_bmp[18:22], byteorder='little', signed=False)
hauteur = int.from_bytes(entete_bmp[22:26], byteorder='little', signed=False)
profondeur_couleurs = int.from_bytes(entete_bmp[28:30], byteorder='little', signed=False)
# ... d'autres informations de l'en-tête BMP

# Afficher les informations
print("Largeur de l'image:", largeur)
print("Hauteur de l'image:", hauteur)
print("Profondeur des couleurs:", profondeur_couleurs)
for octet in entete_bmp:
    binaire = bin(octet)[2:].zfill(8)  # Convertir en binaire et remplir avec des zéros à gauche
    #print(binaire)


import random

# Dimensions de l'image
largeur = 100
hauteur = 100

# Créer une liste vide pour stocker les octets de l'image
donnees = []

# En-tête de fichier BMP
taille_fichier = 54 + (largeur * hauteur * 3)  # Taille du fichier BMP en octets (24 bits par pixel)
donnees.extend([66, 77])

# Taille du fichier (4 octets little-endian)
donnees.append(taille_fichier & 0xFF)
donnees.append((taille_fichier >> 8) & 0xFF)
donnees.append((taille_fichier >> 16) & 0xFF)
donnees.append((taille_fichier >> 24) & 0xFF)

# Champs réservés
donnees.extend([0, 0, 0, 0])

# Offset des données d'image (4 octets little-endian)
donnees.extend([54, 0, 0, 0])

# Taille de l'en-tête de l'image (4 octets)
donnees.extend([40, 0, 0, 0])

# Largeur de l'image (4 octets)
donnees.extend([largeur, 0, 0, 0])

# Hauteur de l'image (4 octets)
donnees.extend([hauteur, 0, 0, 0])

# Planes (2 octets)
donnees.extend([1, 0])

# Profondeur des couleurs (2 octets) - 24 bits par pixel
donnees.extend([24, 0])

# Type de compression (4 octets)
donnees.extend([0, 0, 0, 0])

# Taille des données d'image (4 octets)
donnees.extend([0, 0, 0, 0])

# Résolution horizontale (4 octets)
donnees.extend([0, 0, 0, 0])

# Résolution verticale (4 octets)
donnees.extend([0, 0, 0, 0])

# Nombre de couleurs dans la palette (4 octets)
donnees.extend([0, 0, 0, 0])

# Nombre de couleurs importantes (4 octets)
donnees.extend([0, 0, 0, 0])

# Données d'image (10x10 pixels en couleur RVB aléatoire)
for _ in range(hauteur):
    for _ in range(largeur):
        r = random.randint(0, 255)  # Canal rouge
        g = random.randint(0, 255)  # Canal vert
        b = random.randint(0, 255)  # Canal bleu
        donnees.extend([255,255,255])  # Ajouter en ordre BGR (Bleu, Vert, Rouge)

# Créer un fichier BMP en écrivant les octets
with open('image.bmp', 'wb') as fichier:
    fichier.write(bytearray(donnees))

print("Image BMP en couleur générée avec succès.")
