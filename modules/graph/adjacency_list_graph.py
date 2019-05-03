from modules.graph.graph import Graph
        
class AdjacencyListGraph(Graph):
    
    def __init__(self, graph):
        
        super().__init__(graph)
        
        self.list_graph = {}
        
        # Poderia utilizar Lista aqui, não sei quanto vantajoso é.
        for vertice in super().getVertices():
            self.list_graph[vertice] = []
            
        for edge in super().getEdges():
            self.createEdge(edge)
            
    def show(self):
        print(self.list_graph)
    
    def getGraph(self):
        return self.list_graph
    
    def createEdge(self, edge):
        if (self.edgeExists(edge) == False):
            self.list_graph[edge[0]].append(edge[1])
            self.list_graph[edge[1]].append(edge[0])
            return
        raise Exception('Edge: {0} - {1} is already in Graph!'.format(edge[0],edge[1]))
        
    def edgeExists(self, edge):
        if (self.verticeExists(edge[0]) and self.verticeExists(edge[1])):
            return edge[1] in self.list_graph[edge[0]]
        return False
        
    def removeEdge(self, edge):
        if (self.edgeExists(edge) == True):
            self.list_graph[edge[0]].remove(edge[1])
            self.list_graph[edge[1]].remove(edge[0])
            return
        
        raise Exception('Edge: {0} - {1} is not in Graph!'.format(edge[0],edge[1]))
        
    def getVertices(self):
        return list(self.list_graph.keys())
        
    def verticeExists(self, vertice):
        return vertice in self.list_graph
        
    def createVertice(self, vertice):
        if (self.verticeExists(vertice) == False):
            self.list_graph[vertice] = []
            return
        raise Exception('Vertice: {0} is already in Graph!'.format(vertice))
    
    def removeVertice(self, vertice):
        if (self.verticeExists(vertice)):
            for neighborhood in self.getVerticeNeighborhood(vertice):
                self.list_graph[neighborhood].remove(vertice)
                
            del self.list_graph[vertice]
            return
        raise Exception('Vertice: {0} is not in Graph!'.format(vertice))
    
    def getVerticeNeighborhood(self, vertice):
        if (self.verticeExists(vertice)):
            return self.list_graph[vertice]
        raise Exception('Vertice: {0} is not in Graph!'.format(vertice))
            