class Graph:
    
    VERTICES_KEY = 'vertices'
    EDGES_KEY = 'arestas'
    GRAPH_NAME_KEY = 'nome'
    
    GRAPH_REPRESENTATION_TYPES = ['adjacency_matrix', 'adjacency_list']
    
    ADJACENCY_MATRIX = 'adjacency_matrix'
    AJACENCY_LIST = 'adjacency_list'
    
    def __init__(self, graph):
        self.graph = graph
        
    def show(self):
        print(self.graph)
        
    def getGraph(self):
        return self.graph
        
    def getVertices(self):
        return self.graph[self.VERTICES_KEY]
        
    def verticesCount(self):
        return len(self.getVertices())
        
    def getEdges(self):
        return self.graph[self.EDGES_KEY]
        
    def edgesCount(self):
        return len(self.getEdges())
        
    def getName(self):
        return self.graph[self.GRAPH_NAME_KEY]
        
    def setName(self, name):
        self.graph[self.GRAPH_NAME_KEY] = name
        
    def verticeExists(self, vertice):
        return vertice in self.graph[self.VERTICES_KEY]
        
    def edgeExists(self, edge):
        
        v1 = edge[0]
        v2 = edge[1]
        
        return [v1, v2] in self.graph[self.EDGES_KEY] or [v2, v1] in self.graph[self.EDGES_KEY]
        
    def createVertice(self, vertice):
        if (self.verticeExists(vertice) == False):
            self.graph[self.VERTICES_KEY].append(vertice)
            return
        
        raise Exception('Vertice is already in Graph!')
            
    def createEdge(self, edge):
        if (self.edgeExists(edge) == False):
            self.graph[self.EDGES_KEY].append(edge)
            return
        
        raise Exception('Edge is already in Graph!')
        
    