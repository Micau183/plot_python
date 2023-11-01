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
    # renderer = Bmp_renderer()
    # img_obj = Image_object()
    # sub1 = Image_object()
    # sub2 = Image_object()

    # img_obj.image_blanche(1024, 1024)
    # sub1.image_blanche(400, 900)
    # sub2.image_blanche(400, 900)

    # sub1.border(epaisseur=2)
    # sub2.border(epaisseur=2)

    
    # sub1.plot_fonction(np.cos, end_x=6.3,epaisseur=2, couleur="rouge")
    # sub2.plot_fonction(np.sin, end_x=6.3,epaisseur=2, couleur="bleu")

    # img_obj.add_region(sub1, 50, 50)
    # img_obj.add_region(sub2, 550, 50)

    # img_obj.combine_region()

    # renderer.set_image(img_obj)
    # renderer.assemble_image()
    # renderer.set_name('subplot_test')
    # renderer.rendu()

    renderer = Bmp_renderer()
    img_obj = Image_object()
    img_obj.text_plot("Hello World ", couleur='bleu', epaisseur=2)
    # plt.imshow(img_obj.image)
    # plt.show()



    renderer.set_image(img_obj)
    renderer.assemble_image()
    renderer.rendu()
    



if __name__ == "__main__":
    main()
