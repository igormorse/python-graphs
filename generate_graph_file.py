import json
import random
import sys


if (len(sys.argv) == 1):
    print("\n\nUsage: python generate_graph_file.py {OUTPUT_GRAPH_SIZE} \n\nExample: python generate_graph_file.py 500 - Generates Graph with 500 Vertices and random relationships between them.\n\n")
    exit()
    
# Edges hash to prevent repeated Vertices
edgesHash = {}

# List of Vertices
vertices = []

# Array of tuples of edges
edges = []

# Generated Vertices in Range [1,2,3, ... , n]
for i in range(1, int(sys.argv[1])):
    vertices.append(i)

# Iterate over all Vertices [1,2,3, ... , n]
for vertice in vertices:

    # Defines vertice "Grau"
    random_neighborhood_size = random.randint(0, len(vertices) - 1)

    # Randomly select N-Vertices
    vertices_neighborhood = random.choices(vertices, k=random_neighborhood_size)

    # Build Vertices Neighborhood Edges
    for neighborhood in vertices_neighborhood:
        # if ([vertice, neighborhood] and [neighborhood, vertice] not in edges and neighborhood != vertice):
        if (neighborhood != vertice and str(vertice) + str(neighborhood) not in edgesHash):
            edges.append([vertice, neighborhood])
            edgesHash[str(vertice) + str(neighborhood)] = None
            edgesHash[str(neighborhood) + str(vertice)] = None

# print(edgesHash)

generated_graph = {}

generated_graph['nome'] = 'GRAFO_COM_N_' + str(sys.argv[1])

generated_graph['vertices'] = vertices

generated_graph['arestas'] = edges

# Save Random Generated Graph into Json File
with open('./data/graph.json', 'w', encoding='utf-8') as json_file:
    json.dump(generated_graph, json_file)
