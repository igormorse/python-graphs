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
# graph.createEdge(['b','c'])

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

# print(graph.distancesToVertice(1))

# graphs_paths = graph.getGraphPaths(1, 8)

# for graph in graphs_paths:
    # graph.show()

# print("\n\nGRAFO CAMINHO: \n")
# test = graph.breadthStartToEndSearch(1,8)

# test.getGraphPaths(1, 8, visited, path)

#test.show()

#print(test.distancesToVertice(1))

# exit()
print("\n\nGraph: ")
# graph.show()

for i in range(1):
    
    max_flow = graph.getMaxFlow(1, 8)
    
    print(graph.flow)
    print("\n\nMax Flow: " + str(max_flow))
    
    if (max_flow == 28):
        print("\n\nMax Flow: " + str(max_flow))
        
    graph.resetState()
    
    print(graph.flow)

exit()

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


print("\n\nArestas (getEdges()) ")
begin = time.time()
graph.getEdges()
end = time.time()
print("Tempo: ", end - begin )

print("\n\nÉ Conexo (isConnected()) ")
begin = time.time()
graph.isConnected()
end = time.time()
print("Tempo: ", end - begin )

print("\n\nPossui Ciclo: (hasCicle()) ")
begin = time.time()
graph.hasCicle()
end = time.time()
print("Tempo: ", end - begin )

print("\n\nPossui Floresta (hasForest) ")
begin = time.time()
graph.isConnected()
end = time.time()
print("Tempo: ", end - begin )

print("\n\nÉ Arvore (isTree) ")
begin = time.time()
graph.isTree()
end = time.time()
print("Tempo: ", end - begin )

print("\n\nBrusca profundidade (depthSearch) ")
begin = time.time()
graph.depthSearch(random.choice(graph.getVertices()))
end = time.time()
print("Tempo: ", end - begin )

print("\n\nBrusca profundidade Recursivo (depthSearch) ")
begin = time.time()
graph.depthSearch(random.choice(graph.getVertices()),True)
end = time.time()
print("Tempo: ", end - begin )

print("\n\nBusca Largura (breadthStartSearch) ")
begin = time.time()
graph.breadthStartSearch(random.choice(graph.getVertices()))
end = time.time()
print("Tempo: ", end - begin )

print("\n\nBusca Largura - Com vertice terminal (breadthStartToEndSearch) ")
begin = time.time()
graph.breadthStartToEndSearch(random.choice(graph.getVertices(),random.choice(graph.getVertices())
end = time.time()
print("Tempo: ", end - begin )

print("\n\nFluxo Maximo (getMaxFlow) ")
begin = time.time()
graph.getMaxFlow(random.choice(graph.getVertices(),random.choice(graph.getVertices())
end = time.time()
print("Tempo: ", end - begin )
