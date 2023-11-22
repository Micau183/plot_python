from modules.bmp_renderer import Bmp_renderer
from modules.image_object import Image_object
from modules.module_graph.graph import Graph
from modules.module_graph.arete import Arete
from modules.module_graph.sommet import Sommet
import numpy as np
import matplotlib.pyplot as plt
def main():
    # renderer = Bmp_renderer()
    # renderer.test_rendu(300, 150)
    # print("Hello, world!")

    # renderer = Bmp_renderer()
    # img_obj = Image_object()
    # img_obj.image_blanche(300, 1000)
    # img_obj.ligne_hori(100, couleur ='rouge', epaisseur=2)
    # img_obj.plot_fonction(np.cos, end_x=6.3,epaisseur=3, couleur="jaune")
    # img_obj.ligne_vert(800, couleur ='bleu')
    # img_obj.border(couleur='vert')
    # renderer.set_image(img_obj)
    # renderer.assemble_image()
    # renderer.rendu()

##------------------------------------subplot test---------------------
#     renderer = Bmp_renderer()
#     img_obj = Image_object()
#    sub1 = Image_object()
#    sub2 = Image_object()

#    img_obj.image_blanche(1000, 1000)
#    sub1.image_blanche(400, 900)
#    sub2.image_blanche(400, 900)
    
#    sub1.plot_fonction(np.cos, start_x=0, end_x=6.3, couleur="rouge")
#    sub2.plot_fonction(np.sin, start_x=0,end_x=6.3, couleur="bleu")

#    img_obj.add_region(sub1, 50, 50)
#    img_obj.add_region(sub2, 550, 50)

#    img_obj.combine_region()

#    renderer.set_image(img_obj)
#    renderer.assemble_image()
#    renderer.set_name('subplot_test2')
#    renderer.rendu()

    #-----------------------------------------------------------

    # renderer = Bmp_renderer()
    # img_obj = Image_object()
    # img_obj.image_blanche(108, 200)
    # img_obj.text_plot("Hello World ", couleur='bleu')
    # # plt.imshow(img_obj.image)
    # # plt.show()



    # renderer.set_image(img_obj)
    # renderer.assemble_image()
    # renderer.rendu()
    
    ##------------------------------------------------------------------------------------
    # renderer = Bmp_renderer()
    # img_obj = Image_object()
    

    # img_obj.image_blanche(1000, 1000)
    # def f(x):
    #     return x*x
    # img_obj.plot_fonction(f, start_x=0, end_x=10.5, epaisseur= 1, scale ='auto', couleur='bleu')
    # renderer.set_image(img_obj)
    # renderer.assemble_image()
    # renderer.set_name('axe_test2')
    # renderer.rendu()

    # ##----------------------------------scale auto/epaisseur auto-------------------------------------
    # renderer = Bmp_renderer()
    # img_obj = Image_object()

    # img_obj.image_blanche(1000, 1000)
    # img_obj.text_plot("Salut")
    # renderer.set_image(img_obj)
    # renderer.assemble_image()
    # renderer.set_name('scale_testt')
    # renderer.rendu()

#####--------------------------------graphs------------------------------

    # renderer = Bmp_renderer()
    # img_obj = Image_object()
    # img_obj.image_blanche(1000, 1000)



    # # Create Sommet instances
    # sommet1 = Sommet("A")
    # sommet2 = Sommet("B")
    # sommet3 = Sommet("C")
    # sommet4 = Sommet("D")
    # sommet5 = Sommet("E")

    # # Create Arete instances to connect Sommets
    # arete1 = Arete(sommet1, sommet2)
    # arete2 = Arete(sommet2, sommet3)
    # arete3 = Arete(sommet3, sommet4)
    # arete4 = Arete(sommet4, sommet5)
    # arete5 = Arete(sommet5, sommet1)
    # arete6 = Arete(sommet5, sommet3)

    # # Create a Graph and add Sommets and Aretes to it
    # graph = Graph()
    # graph.add_sommets([sommet1, sommet2, sommet3, sommet4, sommet5])
    # graph.add_aretes([arete1, arete2, arete3, arete4, arete5, arete6])


    # img_obj.plot_graph(graph, epaisseur=2)
    # renderer.set_image(img_obj)
    # renderer.assemble_image()
    # renderer.set_name('graph_test')
    # renderer.rendu()


    renderer = Bmp_renderer()
    img_obj = Image_object()
    img_obj.image_blanche(2000, 2000)



    # Create Sommet instances


    # Create Arete instances to connect Sommets
   

        # Create Arete instances to connect Sommets
    # Create 8 Sommet instances
    sommets = [Sommet(str(i)) for i in range(1, 7)]

    # Create 12 Arete instances
    aretes = [
        Arete(sommets[0], sommets[1]),
        Arete(sommets[1], sommets[2]),
        Arete(sommets[2], sommets[0]),

        Arete(sommets[3], sommets[4]),
        Arete(sommets[4], sommets[5]),
        Arete(sommets[5], sommets[3]),

        Arete(sommets[0], sommets[3]),
        Arete(sommets[1], sommets[4]),
        Arete(sommets[2], sommets[5]),

        Arete(sommets[0], sommets[4]),
    ]

    # Create a Graph and add Sommets and Aretes to it
    graph = Graph()
    graph.add_sommets(sommets)
    graph.add_aretes(aretes)

   
    graph.plongement_tutte_triangle()

    img_obj.plot_graph(graph, epaisseur=2)
    renderer.set_image(img_obj)
    renderer.assemble_image()
    renderer.set_name('graph_test_tutte')
    renderer.rendu()

if __name__ == "__main__":
    main()
