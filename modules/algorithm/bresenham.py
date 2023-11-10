class Bresenham:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def get_line(self):
        points = []
        dx = abs(self.x1 - self.x0)
        dy = abs(self.y1 - self.y0)
        x, y = self.x0, self.y0
        sx = 1 if self.x0 < self.x1 else -1
        sy = 1 if self.y0 < self.y1 else -1

        if dx > dy:
            err = dx / 2.0
            while x != self.x1:
                points.append((x, y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != self.y1:
                points.append((x, y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy

        points.append((x, y))
        return points

# Example usage:
x0, y0 = 1, 1
x1, y1 = 8, 4

bresenham_line = Bresenham(x0, y0, x1, y1)
line_points = bresenham_line.get_line()

for point in line_points:
    print(point)
