import json

from modules.graph.adjacency_matrix_graph import AdjacencyMatrixGraph

from modules.graph.adjacency_list_graph import AdjacencyListGraph

graph = None

# Read Generated Json Graph File.
with open('./data/graph.json', encoding='utf-8') as json_file:
    graphFile = json.load(json_file)


graph = AdjacencyMatrixGraph(graphFile)
# print(graph.verticeExists(0))
graph.createVertice('a')
graph.breadthSearch(1)
#graph.show()
#print('getaresta')
#print(graph.getEdges())

#graph.show()

#print("\n\nAdicionando o Vertice: a\n\n")

#graph.createVertice('a')

#graph.show()

#graph.createEdge([1,3])
#graph.removeEdge([2,1])

#graph.getEdges()

#graph.show()
#graph.show()
# graph.removeVertice('a')

# graph.show()

# for i in range(1,7):
    #graph.removeVertice(i)
    
# graph.show()

exit()
# print(graph.getVerticeNeighborhood(7))

# ------------ Adjacency List Graph ------------------ #

# graph = AdjacencyListGraph(graphFile)

# print(graph2.verticeExists(1))

#graph2.show()

# print(graph2.getVerticeNeighborhood(2))


graph.createVertice('a')
graph.createVertice('b')
graph.createVertice('c')

graph.createEdge(['a','b'])

# Connect Graph
graph.createEdge(['b','c'])

# Add Cicle to Graph
graph.createEdge(['c', 'a'])

graph.show()

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
#print(graph.getForestGeneratorGraph().show())
#
## print("\nÉ Arvore Fast: " + str(graph2.isTreeFast()))

# print("\nDelete o Vertice: a\n")

#print(graph2.getVerticeNeighborhood('a'))

#graph2.removeVertice('a')

#graph2.show()

# for i in range(1,7):
# graph2.removeVertice(1)
# graph2.removeVertice(2)
# graph2.removeVertice(3)
    
# print(graph2.getVerticeNeighborhood('a'))

# Tamanho da Vizinhança
# for vertice in graph2.getVertices():
    # print("Vertice: " + str(vertice))
    # print(len(graph2.getVerticeNeighborhood(vertice)))
    # print("\n")
