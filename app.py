import json

from modules.graph.adjacency_matrix_graph import AdjacencyMatrixGraph

from modules.graph.adjacency_list_graph import AdjacencyListGraph

graph = None

with open('./data/graph.json', encoding='utf-8') as json_file:
    graphFile = json.load(json_file)

# MODO 1

#graph = AdjacencyMatrixGraph(graphFile)

#print(graph.verticeExists(0))

#print(graph.getGraph())

#print("\n\nAdicionando o Vertice: a\n\n")

#graph.createVertice('a')

#graph.show()

#graph.createEdge([1,3])
#graph.removeEdge([2,1])

#graph.show()
# graph.removeVertice('a')

# graph.show()

# for i in range(1,7):
    # graph.removeVertice(i)
    
# graph.show()

#exit()
# print(graph.getVerticeNeighborhood(7))

graph2 = AdjacencyListGraph(graphFile)

# print(graph2.verticeExists(1))

# graph2.show()

# print(graph2.getVerticeNeighborhood(2))


print("\nAdicionando o Vertice: a\n")

graph2.createVertice('a')
graph2.createEdge(['a',3])
graph2.createEdge([1,'a'])
graph2.createEdge([2,'a'])
graph2.removeEdge([2,1])
# graph2.show()

print("\nDelete o Vertice: a\n")

#print(graph2.getVerticeNeighborhood('a'))

#graph2.removeVertice('a')

#graph2.show()

# for i in range(1,7):
graph2.removeVertice(1)
graph2.removeVertice(2)
graph2.removeVertice(3)
    
print(graph2.getVerticeNeighborhood('a'))

for vertice in graph2.getVertices():
    print("Vertice: " + str(vertice))
    print(len(graph2.getVerticeNeighborhood(vertice)))
    print("\n")


# MODO 2
# AdjancecyList/Matrix Classes secundárias
# graph = Graph(graph, Graph.ADJANCECY_REPRESENTATION)
