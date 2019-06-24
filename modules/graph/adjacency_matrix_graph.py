from modules.graph.graph import Graph

#
#   Class AdjacencyMatrixGraph
#
#   Parent: Graph
#
#   Implements Adjacency Matrix Graph Data Representation
#   This class itself doesn't contain complex methods but only its data representation, that is a Matrix

class AdjacencyMatrixGraph(Graph):
    
    #   Params:   
    #   graph       Dict    | None        Pattern: {Name: Graph_Name, Vertices: [Array of Vertices], Edges[Array of Edges]}
    #   directed    Boolean | None        Build Graph as Directed or Not            
    #
    #   Default Constructor. If graph is not None initialize the Graph from the structure passed as argument
    #
    def __init__(self, graph = None, directed = False):
        
        super().__init__(graph)
        
        self.matrix_graph = {}
        
        for vertice in super().getVertices():
            #self.matrix_graph[vertice] = {}
            self.createVertice(vertice)
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
    
    def getEdges(self):
        
        edges = {}
        
        for vertice in self.getVertices():
            for neighborhoodVertice in self.getVerticeNeighborhood(vertice):
                symbolic_edge = self.getSymbolicEdge(vertice, neighborhoodVertice)
                
                if (self.directed == False):
                    inversed_symbolic_edge = self.getSymbolicEdge(neighborhoodVertice, vertice)
                    if symbolic_edge not in edges and inversed_symbolic_edge not in edges:
                        edges[symbolic_edge] = [vertice, neighborhoodVertice]
                else:
                    if symbolic_edge not in edges:
                        edges[symbolic_edge] = [vertice, neighborhoodVertice]

        return edges
    
    def createEdge(self, edge):
        if (self.edgeExists(edge) == False and self.verticeExists(edge[0]) and self.verticeExists(edge[1])):
            self.matrix_graph[edge[0]][edge[1]] = 1
            self.matrix_graph[edge[1]][edge[0]] = 1
            
            self.initializeEdge(edge)
            
            return
        raise Exception('Edge: {0} - {1} is already in Graph!' .format(edge[0],edge[1]))
        
    def removeEdge(self, edge):
        if (self.edgeExists(edge) == True):
            self.matrix_graph[edge[0]][edge[1]] = 0
            self.matrix_graph[edge[1]][edge[0]] = 0
            return
        raise Exception('Edge: {0} - {1} is not in Graph!'.format(edge[0],edge[1]))
        
    def verticeExists(self, vertice):
        return vertice in self.matrix_graph
            
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
                
            self.initializeVertice(vertice)
            
            return
        
        raise Exception('Vertice: {0} is already in Graph!'.format(vertice))
        
    def createVertices(self, vertices):
        for vertice in vertices:
            self.createVertice(vertice)
        
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
    
        
    def getGraphInstance(self, copy = False):
        if not copy:
            return AdjacencyMatrixGraph()
        else:
            return AdjacencyMatrixGraph(self.graph)
    