from modules.graph.graph import Graph

import random        
class AdjacencyListGraph(Graph):
    
    def __init__(self, graph = None):
        
        super().__init__(graph)
        
        self.list_graph = {}
        
        # Poderia utilizar Lista aqui, não sei quanto vantajoso é.
        for vertice in super().getVertices():
            #self.list_graph[vertice] = []
            self.createVertice(vertice)
            
        for edge in super().getEdges():
            self.createEdge(edge)
            
    def show(self):
        print(self.list_graph)
    
    def getGraph(self):
        return self.list_graph
        
    def getEdges(self):
        
        edges = {}
        
        for vertice in self.getVertices():
            for neighborhoodVertice in self.getVerticeNeighborhood(vertice):
                symbolic_edge = self.getSymbolicEdge(vertice, neighborhoodVertice)
                inversed_symbolic_edge = self.getSymbolicEdge(neighborhoodVertice, vertice)
                if symbolic_edge not in edges and inversed_symbolic_edge not in edges:
                    edges[symbolic_edge] = [vertice, neighborhoodVertice]
        
        return edges
    
    def createEdge(self, edge):
        if (self.edgeExists(edge) == False):
            self.list_graph[edge[0]].append(edge[1])
            self.list_graph[edge[1]].append(edge[0])
            
            self.initializeEdge(edge)
            
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
            
            self.initializeVertice(vertice)
            return
        raise Exception('Vertice: {0} is already in Graph!'.format(vertice))
        
    def createVertices(self, vertices):
        for vertice in vertices:
            self.createVertice(vertice)
    
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

    def getGraphInstance(self, copy = False):
        if not copy:
            return AdjacencyListGraph()
        else:
            return AdjacencyListGraph(self.graph)
        