def find_largest_face(vertex_list, edge_list):
    # Création de la liste d'adjacence pour représenter le graphe
    adjacency_list = {vertex: [] for vertex in vertex_list}
    for edge in edge_list:
        v1, v2 = edge
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)

    largest_face = []

    # Fonction pour trouver les cycles dans le graphe
    def find_cycles(start, current, path):
        nonlocal largest_face
        for neighbor in adjacency_list[current]:
            if neighbor == start and len(path) > 2:
                path.append(start)
                if len(path) > len(largest_face):
                    largest_face = path.copy()
            elif neighbor not in path:
                find_cycles(start, neighbor, path + [neighbor])

    # Parcourir chaque sommet pour trouver les cycles et la plus grande face
    for vertex in vertex_list:
        find_cycles(vertex, vertex, [vertex])

    return largest_face

# Exemple de représentation d'un graphe
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('B', 'E'), ('E', 'C')]

# Trouver la plus grande face du graphe
largest_face = find_largest_face(vertices, edges)
print("La plus grande face du graphe est :", largest_face)

import numpy as np

def tutte_embedding(vertex_list, edge_list, fixed_vertices=None):
    num_vertices = len(vertex_list)
    num_edges = len(edge_list)

    # Create the adjacency matrix
    adjacency_matrix = np.zeros((num_vertices, num_vertices))
    for edge in edge_list:
        start, end = edge
        start_index = vertex_list.index(start)
        end_index = vertex_list.index(end)
        adjacency_matrix[start_index][end_index] = 1
        adjacency_matrix[end_index][start_index] = 1

    # Create the degree matrix
    degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))

    # Laplacian matrix
    laplacian_matrix = degree_matrix - adjacency_matrix

    # Initialize positions for unfixed vertices
    unfixed_vertices = [v for v in vertex_list if v not in fixed_vertices]
    num_unfixed = len(unfixed_vertices)
    initial_positions = np.random.rand(num_unfixed, 2)

    # Create a mapping from vertex names to indices
    vertex_indices = {vertex: i for i, vertex in enumerate(vertex_list)}

    # Update initial positions with fixed vertices
    for vertex, position in fixed_vertices.items():
        vertex_index = vertex_indices[vertex]
        initial_positions = np.insert(initial_positions, vertex_index, position, axis=0)

    # Solve for the positions of unfixed vertices
    x = np.linalg.pinv(degree_matrix) @ laplacian_matrix @ initial_positions[:, 0]
    y = np.linalg.pinv(degree_matrix) @ laplacian_matrix @ initial_positions[:, 1]

    # Rescale x and y to fit between 0 and 1
    x = (x - np.min(x)) / (np.max(x) - np.min(x))
    y = (y - np.min(y)) / (np.max(y) - np.min(y))

    # Create a dictionary to store vertex positions
    vertex_positions = {vertex_list[i]: (x[i], y[i]) for i in range(num_vertices)}

    return vertex_positions

# Example graph representation
import math
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
largest_face = find_largest_face(vertices, edges)
def def_pos(cycle):
    num_vertices = len(cycle) 
    positions = {}
    for i, vertex in enumerate(cycle):
        angle = 2 * math.pi * i / num_vertices
        x = 0.5 + 0.4 * math.cos(angle)
        y = 0.5 + 0.4 * math.sin(angle)
        positions[vertex] = (x, y)
    return positions
fixed_positions = {'A': (0.2, 0.2), 'D': (0.8, 0.8)}

# Obtain the Tutte embedding
embedding = tutte_embedding(vertices, edges, fixed_positions)
print("Vertex positions after Tutte embedding:")
print(embedding)
import matplotlib.pyplot as plt
import networkx as nx
def plot_graph(embedding, edge_list):
    G = nx.Graph()
    
    for edge in edge_list:
        start, end = edge
        G.add_edge(start, end)

    pos = embedding
    nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightblue')
    plt.show()

# Exemple de graphe
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('B', 'E'), ('E', 'C')]

cycle = find_largest_face(vertices, edges)
fixed_positions = def_pos(cycle[:-1])

# Obtenir l'incorporation Tutte
embedding = tutte_embedding(vertices, edges, fixed_positions)
print("Positions des sommets après l'incorporation Tutte:")
print(embedding)

# Tracer le graphe
plot_graph(embedding, edges)