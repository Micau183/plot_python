from modules.bmp_renderer import Bmp_renderer


def main():
    renderer = Bmp_renderer()
    renderer.test_rendu(300, 150)
    print("Hello, world!")

if __name__ == "__main__":
    main()
