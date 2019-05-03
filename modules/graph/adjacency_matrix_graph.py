from modules.graph.graph import Graph

class AdjacencyMatrixGraph(Graph):
    
    def __init__(self, graph):
        
        super().__init__(graph)
        
        self.matrix_graph = {}
        
        for vertice in super().getVertices():
            self.matrix_graph[vertice] = {}
            for neighborhood in super().getVertices():
                self.matrix_graph[vertice][neighborhood] = 0
        
        for edge in super().getEdges():
            self.createEdge(edge)
  
        
    def show(self):
        print(self.matrix_graph)
            
    def getGraph(self):
        return self.matrix_graph
        
    def getVertices(self):
        return list(self.matrix_graph.keys())
    
    # ToDo
    def getEdges(self):
        pass
        
    def createEdge(self, edge):
        if (self.edgeExists(edge) == False and self.verticeExists(edge[0]) and self.verticeExists(edge[1])):
            self.matrix_graph[edge[0]][edge[1]] = 1
            self.matrix_graph[edge[1]][edge[0]] = 1
            return
        raise Exception('Edge: {0} - {1} is already in Graph!' .format(edge[0],edge[1]))
        
    # ToDo
    def removeEdge(self, edge):
        if (self.edgeExists(edge) == True):
            self.matrix_graph[edge[0]][edge[1]] = 0
            self.matrix_graph[edge[1]][edge[0]] = 0
            return
        raise Exception('Edge: {0} - {1} is not in Graph!'.format(edge[0],edge[1]))
        
    def verticeExists(self, vertice):
        return vertice in self.matrix_graph
        
    # ToDo
    def edgeExists(self, edge):
        if (self.verticeExists(edge[0]) and self.verticeExists(edge[1])):
            return self.matrix_graph[edge[0]][edge[1]]
            
        return False
            
    def createVertice(self, vertice):
        if (self.verticeExists(vertice) == False):
            
            for graph_vertice in self.getVertices():
                self.matrix_graph[graph_vertice][vertice] = 0
            
            self.matrix_graph[vertice] = {}
            for neighborhood in self.getVertices():
                self.matrix_graph[vertice][neighborhood] = 0
            
            return
        
        raise Exception('Vertice: {0} is already in Graph!'.format(vertice))
        
    def removeVertice(self, vertice):
        if (self.verticeExists(vertice)):
            
            for neighborhood in self.getVertices():
                del self.matrix_graph[neighborhood][vertice]
            
            del self.matrix_graph[vertice]
            
            return
            
        raise Exception('Vertice: {0} is not in Graph!'.format(vertice))
            
    def getVerticeNeighborhood(self, vertice):
        if (self.verticeExists(vertice)):
            
            neighborhood = []
            
            for key, value in self.matrix_graph[vertice].items():
                if value == 1:
                    neighborhood.append(key)
                        
            return neighborhood
            
        raise Exception('Vertice: {0} is not in Graph!'.format(vertice))
            
        
                
        
            
            
            
        
        
    