# plot_python
![Language](https://img.shields.io/badge/Language-Python-f2cb1b)
<br/>

Le projet est de ré-implémenter une partie des bibliothèque matplotlib.pyplot et networkx et également de pouvoir afficher des graphes avec un plongement planaire.

<br/>

<div style="display: flex; align-items: center;">
    <img src="https://i.imgur.com/ao0JzHl.png" style="width: 50%;">
</div>



<br/>


## Explications

Pour pouvoir commencer ce projet, j'ai implémenté un class 'Renderer' qui permet de créer une image au format BitMap créant l'entête en fonction des caractéristiques voulues de l'image.
La classe principale de ce projet est "Image_object" qui permet de modifier une matrice représentant une image en couleur.
A été implémenté :
- Tracé de forme élémentaire : point, ligne (Bresenham algorithm) , cercle (Midle Point Circle algorithm), etc)
- Tracé de fonction sur un intervalle
- Création de "sous-image" (subplot sur matplotlib.pyplot)
- Tracé de texte et chiffres
- Possibilité de choix de taille, d'épaisseur et de couleur pour tous les éléments
- Création d'un "Scale automatique" qui permet de choisir automatiquement la taille du texte en fonction de la taille du contexte
- Tracé de graphes
- Tutte Embedding algorithm pour les plongement planaire de graphes (en cours)

## Le programme
Quelques exemples sont disponibles en commentaire dans le main, et lancer le fichier (sans arguments) :

    python __main__.py 
    
Les fichiers s'enregistrerons dans le dossier 'output' à la fin de l'exécution du programme.

## Infos
Le programme n'étant pas terminé, les bibliothèque matplotlib.pyplot et networkx sont toujours présentes dans le code pour pouvoir débugger plus facilement.
La seule bibliothèque utilisé à terme sera numpy.


