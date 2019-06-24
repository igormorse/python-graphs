import json
import time
import random  

from modules.graph.adjacency_matrix_graph import AdjacencyMatrixGraph

from modules.graph.adjacency_list_graph import AdjacencyListGraph

def timeFormat(begin,end):
    return round((end - begin) * 1000, 6)

graph = None

# Read Generated Json Graph File.
with open('./data/graph.json', encoding='utf-8') as json_file:
    graphFile = json.load(json_file)


# Executa o Algorítmo do Fluxo Máximo
MAX_FLOW_EXAMPLE = False

# True - Utiliza Lista de Adjacência | Falso - Utiliza Matriz de Adjacência
USE_ADJACENCY_LIST_GRAPH = True

# ------------ Fluxo Maximo - Adjacency List Graph ------------------ 
if(MAX_FLOW_EXAMPLE == True):
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
    for i in range(1):
        begin = time.time()
        max_flow = graph.getMaxFlow(1, 8)
        end = time.time()
        print("Tempo: ", timeFormat(begin,end) )
        print("Max (1,8): " , max_flow)
        print("\n\nMax FLow (getMaxFlow()) ")
        
        graph.resetState()
        #print(graph.flow)
    exit()


# ---------- Grafo Lista Adjacente -----
if(USE_ADJACENCY_LIST_GRAPH == True):
    graph = AdjacencyListGraph(graphFile)    
else:
    graph = AdjacencyMatrixGraph(graphFile)    

print("Grafo :\n")
graph.show()

print("\n\n")

print("\n\nCriar Vertice (createVertice()) ")
begin = time.time()
graph.createVertice('asda')
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

randomVerticeSearch = random.choice(graph.getVertices())
print("\n\nBuscar Vertice (search()) ")
begin = time.time()
graph.search(randomVerticeSearch)
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

randomVerticeadd = random.choice(graph.getVertices())
randomVerticeadd2 = 'asda'
print("\n\nCriar Arestas (createEdge()) ")
begin = time.time()
graph.createEdge([randomVerticeadd,randomVerticeadd2])
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

print("\n\nObter Arestas (getEdges()) ")
begin = time.time()
result = graph.getEdges()
end = time.time()
print("Tempo: ", timeFormat(begin,end) )
print("Obter Arestas ", result)


print("\n\nRemover Arestas (removeEdge()) ")
begin = time.time()
graph.removeEdge([randomVerticeadd,randomVerticeadd2])
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

graph.resetState()
randomVerticeRemove = random.choice(graph.getVertices())
print("\n\nRemover Vertice (removeVertice()) ")
begin = time.time()
graph.removeVertice(randomVerticeRemove)
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

graph.resetState()
print("\n\nÉ Conexo (isConnected()) ")
begin = time.time()
result = graph.isConnected()
end = time.time()
print("Tempo: ", timeFormat(begin,end) )
print("É Conexo ", result)

graph.resetState()
print("\n\nPossui Ciclo: (hasCicle()) ")
begin = time.time()
result = graph.hasCicle()
end = time.time()
print("Tempo: ", timeFormat(begin,end) )
print("Possui Ciclo ", result)

graph.resetState()
print("\n\nPossui Floresta (hasForest()) ")
begin = time.time()
result = graph.hasForest()
end = time.time()
print("Tempo: ", timeFormat(begin,end) )
print("Possui Floresta ", result)

graph.resetState()
print("\n\nFloresta Geradora (getForestGeneratorGraph()) ")
begin = time.time()
result = graph.getForestGeneratorGraph()
end = time.time()
print("Tempo: ", timeFormat(begin,end) )
print("Floresta Geradora ", result.show())

graph.resetState()
print("\n\nÉ Arvore (isTree()) ")
begin = time.time()
result = graph.isTree()
end = time.time()
print("Tempo: ", timeFormat(begin,end) )
print("É Arvore" ,result)

graph.resetState()
randomVerticeSearch = random.choice(graph.getVertices())
print("\n\nBusca profundidade (depthSearch()) ")
begin = time.time()
graph.depthSearch(randomVerticeSearch)
end = time.time()
print("Tempo: ", timeFormat(begin,end) )


graph.resetState()
randomVerticeSearch = random.choice(graph.getVertices())
print("\n\nBusca profundidade Recursivo (depthSearch()) ")
begin = time.time()
graph.depthSearch(randomVerticeSearch, True)
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

graph.resetState()
randomVerticeSearch = random.choice(graph.getVertices())
print("\n\nBusca Largura (breadthStartSearch()) ")
begin = time.time()
graph.breadthStartSearch(randomVerticeSearch)
end = time.time()
print("Tempo: ", timeFormat(begin,end) )

