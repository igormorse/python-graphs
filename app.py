import json

from modules.graph.adjacency_matrix_graph import AdjacencyMatrixGraph

from modules.graph.adjacency_list_graph import AdjacencyListGraph

graph = None

# Read Generated Json Graph File.
with open('./data/graph.json', encoding='utf-8') as json_file:
    graphFile = json.load(json_file)


graph = AdjacencyMatrixGraph()

graph.createVertice('a')
graph.createVertice('b')
graph.createVertice('c')

graph.createEdge(['a','b'])

# Connect Graph
graph.createEdge(['b','c'])

# Add Cicle to Graph
graph.createEdge(['c', 'a'])

print(graph.getForestGeneratorGraph().show())

# ------------ Adjacency List Graph ------------------ #

graph = AdjacencyListGraph()


graph.createVertice('a')
graph.createVertice('b')
graph.createVertice('c')

graph.createEdge(['a','b'])

# Connect Graph
graph.createEdge(['b','c'])

# Add Cicle to Graph
graph.createEdge(['c', 'a'])

# graph.show()

#print("\nArestas: " + str(graph.getEdges()))
#
#print("\nÉ Conexo: " + str(graph.isConnected()))
#
#print("\nPossui Ciclo: " + str(graph.hasCicle()))
#
#print("\nPossui Floresta: " + str(graph.hasForest()))
#
#print("\nÉ Arvore: " + str(graph.isTree()))
#
#print("\nFloresta Geradora: \n\n")
#
print(graph.getForestGeneratorGraph().show())
#
## print("\nÉ Arvore Fast: " + str(graph2.isTreeFast()))


