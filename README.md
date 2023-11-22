# plot_python
![Langage](https://img.shields.io/badge/Langage-Python-f2cb1b)
<br/>

Le projet consiste à réimplémenter une partie des bibliothèques matplotlib.pyplot et networkx, ainsi qu'à pouvoir afficher des graphes avec un plongement planaire.
Exemple d'une image contenant deux "sous-images" représentant deux fonctions :
<br/>

<div style="display: flex; align-items: center;">
    <img src="https://i.imgur.com/ao0JzHl.png" style="width: 80%;">
</div>
<br/>
<br/>


Exemple d'une image contenant un plongement planaire d'un graphe :
<div style="display: flex; align-items: center;">
    <img src="https://i.imgur.com/A5yH7e0.png" style="width: 60%;">
</div>

<br/>


## Explications

Pour commencer ce projet, j'ai implémenté une classe 'Renderer' qui permet de créer une image au format Bitmap en créant l'en-tête en fonction des caractéristiques souhaitées de l'image.
La classe principale de ce projet est "Image_object" qui permet de modifier une matrice représentant une image en couleur.
Les fonctionnalités suivantes ont été implémentées :
- Tracé de formes élémentaires : point, ligne (algorithme de Bresenham), cercle (algorithme du cercle du point médian), etc.
- Tracé de fonctions sur un intervalle.
- Création de "sous-images" (sous-graphiques, similaire à matplotlib.pyplot).
- Tracé de texte et de chiffres.
- Possibilité de choisir la taille, l'épaisseur et la couleur pour tous les éléments.
- Création d'un "Scale automatique" qui permet de choisir automatiquement la taille du texte en fonction de la taille du contexte.
- Tracé de graphes.
- Algorithme de tracé de cercle (MidPoint circle algorithm) et de remplissage de cercle.
- Algorithme d'incorporation Tutte pour les plongements planaires de graphes.

## Le programme
Quelques exemples sont disponibles en commentaire dans le fichier principal, et pour lancer le programme (sans arguments), exécutez :

    python __main__.py 
    
Les fichiers seront enregistrés dans le dossier 'output' à la fin de l'exécution du programme.

## Infos
Le programme étant un projet les bibliothèques matplotlib.pyplot et networkx sont  présentes dans le code pour faciliter le débogage.
La seule bibliothèque utilisée dans les programmes est numpy.
