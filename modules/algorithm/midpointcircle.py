import numpy as np
import matplotlib.pyplot as plt
class MidpointCircle:
    def __init__(self, radius):
        self.radius = radius

    def get_circle(self):
        points = []
        x = self.radius
        y = 0
        p = 1 - self.radius

        self._plot_points(points, x, y)

        while x > y:
            y += 1

            if p <= 0:
                p = p + 2 * y + 1
            else:
                x -= 1
                p = p + 2 * (y - x) + 1

            self._plot_points(points, x, y)

        return points

    def _plot_points(self, all_points, x, y):
        all_points.extend([
            [x+self.radius, y+self.radius],
            [-x+self.radius, y+self.radius],
            [x+self.radius, -y+self.radius],
            [-x+self.radius, -y+self.radius],
            [y+self.radius, x+self.radius],
            [-y+self.radius, x+self.radius],
            [y+self.radius, -x+self.radius],
            [-y+self.radius, -x+self.radius],
        ])

# Example usage:
def test():
    radius = 100

    midpoint_circle = MidpointCircle(radius)
    circle_points = midpoint_circle.get_circle()

    for point in circle_points:
        print(point)

    image = np.zeros((radius*3, radius*3))
    for point in circle_points:
        image[point[0],point[1]] = 1

    plt.imshow(image, cmap='gray')
    plt.show()
