from modules.bmp_renderer import Bmp_renderer
from modules.image_object import Image_object
import numpy as np
def main():
    # renderer = Bmp_renderer()
    # renderer.test_rendu(300, 150)
    # print("Hello, world!")

    renderer = Bmp_renderer()
    img_obj = Image_object()
    img_obj.image_blanche(300, 1000)
    img_obj.ligne_hori(100, couleur ='rouge', epaisseur=2)
    img_obj.plot_fonction(np.cos, end_x=6.3,epaisseur=3, couleur=[30,170, 20])
    img_obj.ligne_vert(800, couleur ='bleu')
    
    renderer.set_image(img_obj)
    renderer.assemble_image()
    renderer.rendu()



if __name__ == "__main__":
    main()
