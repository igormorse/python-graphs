import json
import time

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

# print(graph.getForestGeneratorGraph().show())

# ------------ Adjacency List Graph ------------------ #

graph = AdjacencyListGraph(None, True)

for i in range(1,9):
    graph.createVertice(i)
    
graph.createEdge([1,2])
graph.createCapacity([1,2], 10)

graph.createEdge([1,3])
graph.createCapacity([1,3], 5)
graph.createEdge([1,4])
graph.createCapacity([1,4], 15)

graph.createEdge([2,3])
graph.createCapacity([2,3], 4)

graph.createEdge([2,5])
graph.createCapacity([2,5], 9)

graph.createEdge([2,6])
graph.createCapacity([2,6], 15)

graph.createEdge([3,4])
graph.createCapacity([3,4], 4)

graph.createEdge([3,6])
graph.createCapacity([3,6], 8)

graph.createEdge([4,7])
graph.createCapacity([4,7], 30)

graph.createEdge([5,6])
graph.createCapacity([5,6], 15)

graph.createEdge([5,8])
graph.createCapacity([5,8], 10)

graph.createEdge([6,7])
graph.createCapacity([6,7], 15)

graph.createEdge([6,8])
graph.createCapacity([6,8], 10)

graph.createEdge([7,3])
graph.createCapacity([7,3], 6)

graph.createEdge([7,8])
graph.createCapacity([7,8], 10)


print("\n\nGraph: ")
graph.show()

print("\n\nMax Flow: " + graph.getMaxFlow(1, 8))

# ----------
graph = AdjacencyListGraph(None, True)


graph.createVertice('a')
graph.createVertice('b')
graph.createVertice('c')

graph.createEdge(['a','b'])

# Connect Graph
graph.createEdge(['b','c'])

# Add Cicle to Graph
graph.createEdge(['c', 'a'])


print("Show:\n")
graph.show()

print("\n\nGRAFO CAMINHO: \n")

graph.getMaxFlow('a', 'c')

print("\n\n")

exit()

begin = time.time()
print("\nÉ Conexo: " + str(graph.isConnected()))
end = time.time()

print("Tempo: ", end - begin )

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


