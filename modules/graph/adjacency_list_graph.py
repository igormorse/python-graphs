from modules.graph.graph import Graph
import copy

import random        
class AdjacencyListGraph(Graph):
    """
    Implements Adjacency List Graph Data Representation
    This class itself doesn't contain complex methods but only its data representation, that is a List

    Parent: Graph

    Returns:
        AdjacencyListGraph    -- Adjacency List Graph Data Representation
    """
    
    def __init__(self, graph = None, directed = False):
        """Default Constructor
        
        Keyword Arguments:
            graph {Dictionary}  -- Data Structure to Initialize the Graph with. Example: {Name: Graph_Name, Vertices: [Array of Vertices], Edges[Array of Edges]} (default: {None})
            directed {bool}     -- Graph is directed (oriented) or Not. (default: {False})
        """
        
        super().__init__(graph, directed)
        
        """List Graph Representation
        """
        self.list_graph = {}
        
        for vertice in super().getVertices():
            #self.list_graph[vertice] = []
            self.createVertice(vertice)
            
        for edge in super().getEdges():
            self.createEdge(edge)
            
    def show(self):
        """ Print Current Graph into Console.
        """
        print(self.list_graph)
    
    def getGraph(self):
        """Return Original Graph Data Structure ( This method is not public as it is overriden by child classes )

        **Overriden Method by Child**
        
        Returns:
            Dictionary -- Return initial Graph Data Structure
        """
        return self.list_graph
        
    def getEdges(self):
        """Get Graph's Edges List

        **Overriden Method by Child**
        
        Returns:
            [List]      -- Edges List
        """
        
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
        """Create Vertice in Graph

        **Overriden Method by Child**
        
        Arguments:
            vertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Vertice Already Exists in Graph
        """
        if (self.verticeExists(edge[0]) and self.verticeExists(edge[1])):
            if (self.edgeExists(edge) == False):
                self.list_graph[edge[0]].append(edge[1])
                
                if (self.directed == False):
                    self.list_graph[edge[1]].append(edge[0])
                
                self.initializeEdge(edge)
                
                return
            raise Exception('Edge: {0} - {1} is already in Graph!'.format(edge[0],edge[1]))
        raise Exception('Some Vertice: {0} - {1} are not in Graph!'.format(edge[0], edge[1]))
        
    def edgeExists(self, edge):
        """Check if Edges Exists

        **Overriden Method by Child**
        
        Arguments:
            edge {List}       -- Edges as List. Example: [vertice1, vertice2]
        
        Returns:
            Boolean           -- Either Edge Exists or Not.
        """
        if (self.verticeExists(edge[0]) and self.verticeExists(edge[1])):
            return edge[1] in self.list_graph[edge[0]]
            
        return False
        
    def removeEdge(self, edge):
        """Remove Edge from Graph

        **Overriden Method by Child**
        
        Arguments:
            edge {List}         -- Edges as List. Example: [vertice1, vertice2]
        
        Raises:
            Exception: Edge doesn't Exists in Graph
        """
        if (self.edgeExists(edge) == True):
            self.list_graph[edge[0]].remove(edge[1])
            
            if (self.directed == False):
                self.list_graph[edge[1]].remove(edge[0])
                
            return
        
        raise Exception('Edge: {0} - {1} is not in Graph!'.format(edge[0],edge[1]))
        
    def getVertices(self):
        """ Get Graph's Vertices List

        **Overriden Method by Child**
        
        Returns:
            [List]     -- Vertices List
        """
        return list(self.list_graph.keys())
        
    def verticeExists(self, vertice):
        """Check if Vertice Exists

        **Overriden Method by Child**
        
        Arguments:
            vertice {String|Integer}  -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Returns:
            [Boolean]         -- Condition to check if vertice exists
        """
        return vertice in self.list_graph
        
    def createVertice(self, vertice):
        """Create Many Vertices in Graph
        
        Arguments:
            vertices {List}         -- List of Vertices to be created.
        """
        if (self.verticeExists(vertice) == False):
            self.list_graph[vertice] = []
            
            self.initializeVertice(vertice)
            return
        raise Exception('Vertice: {0} is already in Graph!'.format(vertice))
    
    def removeVertice(self, vertice):
        """Remove Vertice from Graph
        
        Arguments:
            vertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Vertice not in Graph!
        """
        if (self.verticeExists(vertice)):
            for neighborhood in self.getVerticeNeighborhood(vertice):
                self.list_graph[neighborhood].remove(vertice)
                
            del self.list_graph[vertice]
            return
        raise Exception('Vertice: {0} is not in Graph!'.format(vertice))
    
    def getVerticeNeighborhood(self, vertice):
        """Get All Vertices in a Vertice(V1) Neighborhood
           Example: v1 has [v2,v3,v4] as adjacency vertices, this methods returns those vertices
        
        Arguments:
            vertice {String|Vertice}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Vertice not in Graph!
        """
        if (self.verticeExists(vertice)):
            return self.list_graph[vertice]
        raise Exception('Vertice: {0} is not in Graph!'.format(vertice))

    def getGraphInstance(self, deep_copy = False, directed = False):
        """Get Self Graph Instance as a Copy or New One

           **Method Overriden by Child Class**
        
        Keyword Arguments:
            deep_copy {bool}    -- Generate a new copy of itself or a new one (default: {False})
        
        """
        if not deep_copy:
            return AdjacencyListGraph(directed = directed)
        else:
            return copy.deepcopy(self)
    