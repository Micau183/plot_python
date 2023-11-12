import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


# Create an empty undirected graph
G = nx.Graph()

K6 = nx.complete_graph(6)

# Print basic information about the graph
print("Nodes:", K6.nodes())
print("Edges:", K6.edges())

# Draw and visualize the graph
pos = nx.random_layout(K6)  # Position nodes using a spring layout
nx.draw(K6, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_color='black', font_weight='bold', edge_color='gray', width=2)

# You can save the graph as an image or display it
plt.savefig("K6_graph.png", format="PNG")
plt.show()

# You can save the graph as an image or display it
plt.show()

