from modules.bmp_renderer import Bmp_renderer
from modules.image_object import Image_object

def main():
    renderer = Bmp_renderer()
    renderer.test_rendu(300, 150)
    print("Hello, world!")

    img_obj = Image_object()
    img_obj.image_blanche(20, 30)

if __name__ == "__main__":
    main()
