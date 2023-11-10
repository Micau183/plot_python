
import numpy as np
import matplotlib.pyplot as plt

class TutteAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def draw_planar_graph(self):
        pos = self.tutte_embedding()
        #nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=700)
        plt.show()

    def tutte_embedding(self):
        n = len(self.graph.nodes())
        # Create the matrix for the linear equations
        A = np.zeros((n, n))
        b = np.zeros((n,))

        for i, node in enumerate(self.graph.nodes()):
            A[i][i] = 1
            neighbors = list(self.graph.neighbors(node))
            A[i, neighbors] = -1 / len(neighbors)
            b[i] = 0

        # Solve the linear equations
        x, y = np.linalg.solve(A, b), np.zeros((n,))
        pos = {node: (x[i], y[i]) for i, node in enumerate(self.graph.nodes())}
        return pos

# Example usage:
# G = nx.complete_graph(5)
# tutte_algorithm = TutteAlgorithm(G)
# tutte_algorithm.draw_planar_graph()
