from modules.bmp_renderer import Bmp_renderer
from modules.image_object import Image_object
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
    renderer = Bmp_renderer()
    img_obj = Image_object()
    sub1 = Image_object()
    sub2 = Image_object()

    img_obj.image_blanche(1000, 1000)
    sub1.image_blanche(400, 900)
    sub2.image_blanche(400, 900)
    
    sub1.plot_fonction(np.cos, start_x=0, end_x=6.3, couleur="rouge")
    sub2.plot_fonction(np.sin, start_x=0,end_x=6.3, couleur="bleu")

    img_obj.add_region(sub1, 50, 50)
    img_obj.add_region(sub2, 550, 50)

    img_obj.combine_region()

    renderer.set_image(img_obj)
    renderer.assemble_image()
    renderer.set_name('subplot_test2')
    renderer.rendu()

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

if __name__ == "__main__":
    main()
