from collections import deque
import random

class Graph:
    """
    Generic Class for Graphs. It shares common methods for data representations implementations such as AdjacencyList and AdjacencyMatrix.

    All basic methods to interact with Vertice and Edges needs to be override by the Child Class.

    Returns:
        Graph -- Graph Class
    """

    # Vertice Key of Data Structured passed by argument
    VERTICES_KEY = 'vertices'
    # Edge Key of Data Structured passed by argument
    EDGES_KEY = 'arestas'
    # Graph name Key of Data Structured passed by argument
    GRAPH_NAME_KEY = 'nome'
    
    def __init__(self, graph = None, directed = False):
        """Default Constructor
        
        Keyword Arguments:
            graph {Dictionary}  -- Data Structure to Initialize the Graph with. Example: {Name: Graph_Name, Vertices: [Array of Vertices], Edges[Array of Edges]} (default: {None})
            directed {bool}     -- Graph is directed (oriented) or Not. (default: {False})
        """

        """Create public variables to store searchs and max flow algorithms data
        """
        self.visited = {}
        self.explored = {}
        self.discovered = {}
        
        self.directed = directed
        
        self.capacity = {}
        
        self.flow = {}
        
        self.sink = {}
        
        self.reverse_edge = {}
        
        """Initialize Graph with Data Structure passed by Argument or initialize everything with blank
        """
        if graph is not None:
            self.graph = graph
        else:
            self.graph = {}
            self.graph[self.VERTICES_KEY] = []
            self.graph[self.EDGES_KEY] = []
            self.graph[self.GRAPH_NAME_KEY] = []
        
    def show(self):
        """ Print Current Graph into Console.
        """
        print(self.graph)
        
    def getGraph(self):
        """Return Original Graph Data Structure ( This method is not public as it is overriden by child classes )

        **Overriden Method by Child**
        
        Returns:
            Dictionary -- Return initial Graph Data Structure
        """
        return self.graph
        
    def getVertices(self):
        """ Get Graph's Vertices List

        **Overriden Method by Child**
        
        Returns:
            [List]     -- Vertices List
        """
        return self.graph[self.VERTICES_KEY]
        
    def verticesCount(self):
        """Count Number of Vertices
        
        Returns:
            [Integer]   -- Number of Vertices
        """
        return len(self.getVertices())
        
    def getEdges(self):
        """Get Graph's Edges List

        **Overriden Method by Child**
        
        Returns:
            [List]      -- Edges List
        """
        return self.graph[self.EDGES_KEY]
        
    def edgesCount(self):
        """Count Number of Edges
        
        Returns:
            [Integer]   -- Number of Edges
        """
        return len(self.getEdges())
        
    def getName(self):
        """Get Graph's Name
        
        Returns:
            [String]        -- Graph's Name
        """
        return self.graph[self.GRAPH_NAME_KEY]
        
    def setName(self, name):
        """Define Graph's Name
        
        Arguments:
            name {String}    -- Graph's Name
        """
        self.graph[self.GRAPH_NAME_KEY] = name
        
    def verticeExists(self, vertice):
        """Check if Vertice Exists

        **Overriden Method by Child**
        
        Arguments:
            vertice {String|Integer}  -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Returns:
            [Boolean]         -- Condition to check if vertice exists
        """
        return vertice in self.graph[self.VERTICES_KEY]
        
    def edgeExists(self, edge):
        """Check if Edges Exists

        **Overriden Method by Child**
        
        Arguments:
            edge {List}       -- Edges as List. Example: [vertice1, vertice2]
        
        Returns:
            Boolean           -- Either Edge Exists or Not.
        """
        
        v1 = edge[0]
        v2 = edge[1]
        
        return [v1, v2] in self.graph[self.EDGES_KEY] or [v2, v1] in self.graph[self.EDGES_KEY]
        
    def createVertice(self, vertice):
        """Create Vertice in Graph

        **Overriden Method by Child**
        
        Arguments:
            vertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Vertice Already Exists in Graph
        """
        if (self.verticeExists(vertice) == False):
            self.graph[self.VERTICES_KEY].append(vertice)
            return
        
        raise Exception('Vertice is already in Graph!')
        
    def createVertices(self, vertices):
        """Create Many Vertices in Graph
        
        Arguments:
            vertices {List}         -- List of Vertices to be created.
        """
        for vertice in vertices:
            self.createVertice(vertice)
            
    def createEdge(self, edge):
        """Create Edge in Graph

        **Overriden Method by Child**
        
        Arguments:
            edge {List}             -- Edges as List. Example: [vertice1, vertice2]
        
        Raises:
            Exception: Edge already Exists in Graph
        """
        if (self.edgeExists(edge) == False):
            self.graph[self.EDGES_KEY].append(edge)
            return
        
        raise Exception('Edge is already in Graph!')
        
    def removeEdge(self, edge):
        """Remove Edge from Graph

        **Overriden Method by Child**
        
        Arguments:
            edge {List}         -- Edges as List. Example: [vertice1, vertice2]
        
        Raises:
            Exception: Edge doesn't Exists in Graph
        """
        if (self.edgeExists(edge)):
            del self.graph[self.EDGES_KEY][edge]
            return
        
        raise Exception('Edge not Found in Graph!')

    def removeVertice(self, vertice):
        """Remove Vertice from Graph
        
        Arguments:
            vertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Method not Implemented!
        """
        
        raise Exception('removeVertice(self,vertice) is not Implemented!')
        
    def clearEdges(self):
        """Remove all Edges from Graphs
        """
        for edge in list(self.getEdges().values()):
            self.removeEdge(edge)
        
    def getSymbolicEdge(self, firstVertice, secondVertice):
        """Get Symbolic Edge as String. Example: firstVertice: 0 and secondVertice: 1 turns to '01'
           So it can be used as Dictionary Key
        
        Arguments:
            firstVertice {String|Integer}         -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            secondVertice {String|Integer}        -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Returns:
            [String]                              -- Symbolic Key of Vertices as String. Example: firstVertice: 0 and secondVertice: 1 turns to '01'
        """
        return str(firstVertice) + str(secondVertice)
        
    def initializeEdge(self, edge):
        """Initialize Edge with default Setup such as explored, discovered to default values as they are global
           Similar To: initializeVertice(self, vertice)
        
        Arguments:
            edge {List}                           -- Edges as List. Example: [vertice1, vertice2]
        """
        symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
        
        self.explored[symbolic_edge] = False
        
        self.discovered[symbolic_edge] = False
        
        self.createFlow(edge, 0)
        
        self.createCapacity(edge, 0)
        
        self.sink[symbolic_edge] = False
    
        if (self.directed == False):
            inversed_symbolic_edge = self.getSymbolicEdge(edge[1], edge[0])
            self.explored[inversed_symbolic_edge] = False
            self.discovered[inversed_symbolic_edge] = False
    
    def initializeVertice(self, vertice):
        """Initialize Vertice with default setup such as Visited to default values as they are global
           Similar To: initializeEdge(self, edge)
        
        Arguments:
            vertice {String|Integer}            -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        """
        self.visited[vertice] = False
        
    def exploreEdge(self, firstVertice, secondVertice):
        """Method to Explore Edge
        
        Arguments:
            firstVertice {String|Integer}       -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            secondVertice {String|Integer}      -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        """
        self.explored[self.getSymbolicEdge(firstVertice, secondVertice)] = True
        
        if (self.directed == False):
            self.explored[self.getSymbolicEdge(secondVertice, firstVertice)] = True
        
    def discoverEdge(self, firstVertice, secondVertice):
        """Method to Discover Edge
        
        Arguments:
            firstVertice {String|Integer}       -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            secondVertice {String|Integer}      -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        """
        self.discovered[self.getSymbolicEdge(firstVertice, secondVertice)] = True
        
        if (self.directed == False):
            self.discovered[self.getSymbolicEdge(secondVertice, firstVertice)] = True
        
    def createCapacity(self, edge, capacity = 0):
        """Creates Capacity for Edge
        
        Arguments:
            edge {List}         -- Edges as List. Example: [vertice1, vertice2]
        
        Keyword Arguments:
            capacity {int}      -- Capacity Value for Edge (default: {0})
        
        Returns:
            Boolean             -- Capacity was created or not
        """
        if self.edgeExists(edge):
            self.capacity[self.getSymbolicEdge(edge[0], edge[1])] = capacity
            return True
            
        return False
        
    def createFlow(self, edge, flow = 0):
        """Creates Flow for Edge
        
        Arguments:
            edge {List}         -- Edges as List. Example: [vertice1, vertice2]
        
        Keyword Arguments:
            flow {int}          -- Flow Value for Edge (default: {0})
        
        Returns:
            Boolean             -- Flow was created or not
        """
        if self.edgeExists(edge):
            self.flow[self.getSymbolicEdge(edge[0], edge[1])] = flow
            return True
            
        return False
        
    def resetState(self):
        """Reset State for the Graph. Basically resets global variables to default value

           Values reseted: visited, sink, discovered, expored, reverse_edge, flow, capacity
        """
        for vertice in self.visited:
            self.visited[vertice] = False
            
        for sink in self.sink:
            self.sink[sink] = False
            
        for discovered in self.discovered:
            self.discovered[discovered] = False
            
        for explored in self.explored:
            self.explored[explored] = False
            
        for reverse in self.reverse_edge:
            self.reverse_edge[reverse] = 0
            
        for flow in self.flow:
            self.flow[flow] = 0
            
        for capacity in self.capacity:
            self.capacity[capacity] = 0
    
    def fullSearch(self):
        """Full Search Method for Graph, performs search in every Vertice in Graph.
           Visiting, Exploring and Discovering Every Vertice and Edge in Graph.
           Complexity: θ(n+m)
        """
        for vertice in self.getVertices():
            if(self.visited[vertice] == False):
                self.search(vertice)
        
    def search(self, vertice = None):
        """Search Method for Graph, performs Search initializing from a random or choosen vertice.
           Visiting, Exploring and Discovering Every Vertice and Edge in Graph.
           Complexity: O(n+m)
        
        Keyword Arguments:
            vertice {String|Integer}        -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive. (default: {None})
        """
        if vertice is None:
            # Choosing Randomly Doesn't Work so instead choose the first one
            # root_vertice = random.choices(list(self.list_graph.keys()), k=1)
            root_vertice = list(self.getVertices())
            self.visited[root_vertice[0]] = True
        else:
            self.visited[vertice] = True
            
        for edge in list(self.getEdges().values()):
            symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
            if (self.visited[edge[0]] and not self.explored[symbolic_edge]):
                self.explored[symbolic_edge] = True
                
                if not self.visited[edge[1]]:
                    self.visited[edge[1]], self.discovered[symbolic_edge] = True, True
        
    def isConnected(self):
        """Check if Graph is Connected or Not
           Complexity: O(n+m)
        
        Returns:
            Boolean         -- Graph is Connected or Not
        """
        self.search()
        for vertice in self.getVertices():
            if(self.visited[vertice] == False):
                return False
        return True
        
    def hasCicle(self):
        """Check if Graph has Cicle or Not
           Complexity: O(n+m)
        Returns:
            Boolean         -- Graph has Cicle or Not
        """
        self.fullSearch()
        
        for edge in self.getEdges().keys():
            if not self.discovered[edge]:
                return True
        return False
        
    def hasForest(self):
        """Check if Graph has Forest or Not
           Complexity: O(n+m)
        
        Returns:
            Boolean         -- Graph has a Forest or Not
        """
        return not self.hasCicle() 
    
    def isTree(self, alternative = False):
        """Check if Graph is a Tree or Not
           Complexity: O(n+m) 

        Keyword Arguments:
            alternative {bool}  -- Use Alternative Method to Verify if Is Tree. First uses Search and Second Uses isConnected() and not HasCicle()  (default: {False})
        
        Returns:
            Boolean             -- Graph is a Tree or Not
        """
        
        if not alternative:
            self.search()
            
            for vertice in self.getVertices():
                if(self.visited[vertice] == False):
                    return False
            
            for edge in list(self.getEdges().values()):
                symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
                if(self.discovered[symbolic_edge] == False):
                    return False
        else:
            return self.isConnected() and not self.hasCicle()

        return True
    
    def getForestGeneratorGraph(self):
        """Get Forest Generator Graph
           Complexity: O(n+m) 
        
        Returns:
            Graph       -- Returns Forest Generator Graph for the current Graph itself
        """
        
        newGraph = self.getGraphInstance(directed = self.directed)
        
        newGraph.createVertices(self.getVertices())

        self.fullSearch()
        
        for edge in list(self.getEdges().values()):
            symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
            if self.discovered[symbolic_edge]:
                newGraph.createEdge(edge)
                
        return newGraph
    
    
    def depthSearch(self, vertice, recursive = False):
        """Peforms Depth Search in Graph either on Recursive or Iterative Mode
        
        Arguments:
            vertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Keyword Arguments:
            recursive {bool}            -- Execute using recursive method or iterative (default: {False})
        """

        self.visited[vertice] = True
        
        if(recursive):
            for neighborhoodVertice in self.getVerticeNeighborhood(vertice):
                if(self.visited[neighborhoodVertice]):
                    if not self.explored[self.getSymbolicEdge(vertice, neighborhoodVertice)]:
                        self.exploreEdge(vertice, neighborhoodVertice)
                else:
                    self.exploreEdge(vertice, neighborhoodVertice)
                    self.discoverEdge(vertice, neighborhoodVertice)
                    self.depthSearch(neighborhoodVertice, True)
        else:
            stack = []
            stack.append([vertice, self.getVerticeNeighborhoodAfter(vertice)])

            while(stack):
                topStack = stack.pop()
                vertice = topStack[0]
                nextNeighborhoodVertice = topStack[1]

                if(nextNeighborhoodVertice > 0):
                    stack.append([vertice,self.getVerticeNeighborhoodAfter(vertice,nextNeighborhoodVertice)])
                   
                    if(self.visited[nextNeighborhoodVertice]):
                        if(not self.explored[self.getSymbolicEdge(vertice, nextNeighborhoodVertice)]):
                            self.exploreEdge(vertice, nextNeighborhoodVertice)
                    else:
                        self.exploreEdge(vertice, nextNeighborhoodVertice)
                        self.discoverEdge(vertice, nextNeighborhoodVertice)
                        self.visited[nextNeighborhoodVertice] = True
                        stack.append([nextNeighborhoodVertice, self.getVerticeNeighborhoodAfter(nextNeighborhoodVertice)])
                    
    def getVerticeNeighborhoodAfter(self, vertice, neighborhoodVertice = None):
        """Get Vertices Neighborhood of a Vertice after some Vertice Neighborhood.
           Example: Vertices neighborhood for v1 is [v2,v3,v4]
                    neighborhoodVertice value is v3 then result will be v4. 
        
        Arguments:
            vertice {String|Integer}                -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Keyword Arguments:
            neighborhoodVertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive. (default: {None})
        
        Returns:
            List        -- List of Vertices Neighborhood after a given vertice inside the neighborhood
        """
        
        verticeNeighborhoodList = self.getVerticeNeighborhood(vertice)
        
        if not verticeNeighborhoodList:
            return 0
        else:
            if(neighborhoodVertice is None):
                return verticeNeighborhoodList[0]
        
        indexAfter = verticeNeighborhoodList.index(neighborhoodVertice)+1
        try:
            if(verticeNeighborhoodList[indexAfter]):
                return verticeNeighborhoodList[indexAfter]
        except IndexError:  
            return 0

    def breadthStartSearch(self, start_vertice):
        """Performs Breadth Search in Graph
        
        Arguments:
            start_vertice {String|Integer}      -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        """
        
        self.visited[start_vertice] = True
        queue = deque([])
        queue.append(start_vertice)

        while(queue):
            vertice = queue.popleft()
            for neighborhoodVertice in self.getVerticeNeighborhood(vertice):
                if(self.visited[neighborhoodVertice]):
                    if(not self.explored[self.getSymbolicEdge(vertice, neighborhoodVertice)]):
                        self.exploreEdge(vertice, neighborhoodVertice)
                else:
                    self.exploreEdge(vertice, neighborhoodVertice)
                    self.discoverEdge(vertice, neighborhoodVertice)
                    self.visited[neighborhoodVertice] = True
                    queue.append(neighborhoodVertice)
                    
    def breadthStartToEndSearch(self, start_vertice, end_vertice):
        """Performs Breadth Search from a Start Vertice to an Destination Veretice
           From Vertice A to B it will return a Graph with at least one path between those two points.
        
        Arguments:
            start_vertice {String|Integer}  -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            end_vertice {String|Integer}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Returns:
            Graph   -- Graph with at least one Path that exists from origin vertice to destination vertice
        """

        self.visited[start_vertice] = True
        queue = deque([])
        queue.append(start_vertice)
        
        graph = self.getGraphInstance(directed = self.directed)

        graph.createVertice(start_vertice)
   
        while(queue):
            vertice = queue.popleft()
            for neighborhoodVertice in self.getVerticeNeighborhood(vertice):
                
                if(self.visited[neighborhoodVertice]):
                    if not self.explored[self.getSymbolicEdge(vertice, neighborhoodVertice)]:
                        self.exploreEdge(vertice, neighborhoodVertice)
                        graph.createEdge([vertice, neighborhoodVertice])
                else:
                    self.exploreEdge(vertice, neighborhoodVertice)
                    self.discoverEdge(vertice, neighborhoodVertice)
                    self.visited[neighborhoodVertice] = True
                    queue.append(neighborhoodVertice)
                    graph.createVertice(neighborhoodVertice)
                    graph.createEdge([vertice, neighborhoodVertice])
                    
                if (neighborhoodVertice == end_vertice):
                    return graph
            
        return None
    
    def getGraphPaths(self, origin_vertice, destination_vertice):
        """Get All Paths from one Origin Vertice to a Destination Vertice
           From Vertice A to B returns a List of Graphs containing all Paths between those two Vertices
           
           Related To: getAllGraphPaths()
        
        Arguments:
            origin_vertice {String|Integer}             -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            destination_vertice {String|Integer}        -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Returns:
            [List]      -- List of Graph's Paths
        """

        paths = []
        
        graphs_paths = []
        
        visited = {}

        for vertice in self.getVertices():
            visited[vertice] = False
        
        self.getAllGraphPaths(origin_vertice, destination_vertice, visited, paths, graphs_paths)
        
        return graphs_paths
    
    def getAllGraphPaths(self, origin_vertice, destination_vertice, visited, paths, graphs_paths):
        """Get All Paths from one Origin Vertice to a Destination Vertice
           From Vertice A to B returns a List of Graphs containing all Paths between those two Vertices
        
        Arguments:
            origin_vertice {String|Integer}                 -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            destination_vertice {String|Integer}            -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            visited {List}                                  -- Visited List of Vertices ( Passed by Reference )
            paths {List}                                    -- List of Paths ( Passed by Reference )
            graphs_paths {List}                             -- List of Graph's Paths ( Passed by Reference )
        """
  
        # Mark the current node as visited and store in path 
        visited[origin_vertice] = True
        paths.append(origin_vertice) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if (origin_vertice == destination_vertice):
            
            graph = self.getGraphInstance(directed = self.directed)
            
            index = 0
            
            for i in range(len(paths)):
                
                vertice = paths[i]
                
                if not graph.verticeExists(vertice):
                    graph.createVertice(vertice)
                
                if (i < len(paths) - 1):
                    
                    next_vertice = paths[i + 1]
                    
                    if not graph.verticeExists(next_vertice):
                        graph.createVertice(next_vertice)
                    
                    graph.createEdge([vertice, next_vertice])
                    
            graphs_paths.append(graph)
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for neighborhoodVertice in self.getVerticeNeighborhood(origin_vertice): 
                if (visited[neighborhoodVertice] == False): 
                    self.getAllGraphPaths(neighborhoodVertice, destination_vertice, visited, paths, graphs_paths) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        paths.pop()
        
        visited[origin_vertice] = False
    
    def distancesToVertice(self, vertice):
        """Get All Vertice Distances to One Specified Vertice
           Example: distancesToVertice(1) -> Returns a List of All Vertices and their distances to Vertice 1
        
        Arguments:
            vertice {String|Integer}        -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Returns:
            [List]      -- List of Vertices containing their Distances
        """
        
        distances = {}
        
        for _vertice in self.getVertices():
            distances[_vertice] = None
        
        queue = deque([])
        
        self.visited[vertice] = True
        
        queue.append([vertice, 1])
        
        while(len(queue) > 0):
            popedEdge = queue.popleft()
            
            for neighborhoodVertice in self.getVerticeNeighborhood(popedEdge[0]):
                if self.visited[neighborhoodVertice]:
                    if not self.explored[self.getSymbolicEdge(popedEdge[0], neighborhoodVertice)]:
                        self.exploreEdge(popedEdge[0], neighborhoodVertice)
                else:
                    self.exploreEdge(popedEdge[0], neighborhoodVertice)
                    self.discoverEdge(popedEdge[0], neighborhoodVertice)
                    
                    self.visited[neighborhoodVertice] = True
                    
                    distances[neighborhoodVertice] = popedEdge[1]
    
                    queue.append([neighborhoodVertice, popedEdge[1] + 1])
                    
        return distances
        
    def getMaxFlow(self, source, sink):
        """Get Max Flow from a Directed Graph
           Related To: getResidualGraph()
        
        Arguments:
            source {String|Integer}         -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            sink {String|Integer}           -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Graph is not Directed!
        
        Returns:
            Integer         -- Value of Max Flow
        """
        
        if (self.directed == False):
            raise Exception('Current Graph is not Directed! Transform it to Directed Graph to use MaxFlow!')
        
        #flow = {}
        
        max_flow_digraph = 0
        
        for edge in list(self.getEdges().values()):
            self.flow[self.getSymbolicEdge(edge[0], edge[1])] = 0
            
        residual_digraph = self.getResidualGraph(source, sink)
        
        try:
            residual_possible_paths = residual_digraph.breadthStartToEndSearch(source, sink).getGraphPaths(source, sink)
        except AttributeError:  
            return 0
        
        # residual_possible_paths = residual_digraph.getGraphPaths(source, sink)
        
        digraph_path = random.choice(residual_possible_paths)
        
        residual_capacity = 0
        
        while (digraph_path != None):
            
            residual_capacity = min(list(self.reverse_edge.values()))
            
            max_flow_digraph += residual_capacity
            
            for edge in list(digraph_path.getEdges().values()):
                
                symbolic_edge = digraph_path.getSymbolicEdge(edge[0], edge[1])
                
                inverse_symbolic_edge = digraph_path.getSymbolicEdge(edge[1], edge[0])
                
                if (self.sink[symbolic_edge]):
                    self.flow[symbolic_edge] += residual_capacity
                else:
                    self.flow[inverse_symbolic_edge] -= residual_capacity
                    
            residual_digraph = self.getResidualGraph(source, sink)
            
            # possible_digraph_paths = residual_digraph.getGraphPaths(source, sink)
            possible_paths = residual_digraph.breadthStartToEndSearch(source, sink)
            
            if possible_paths is not None:
                digraph_path = random.choice(possible_paths.getGraphPaths(source, sink))
            else:
                digraph_path = None
            
            # if possible_digraph_paths:
            #    digraph_path = random.choice(possible_digraph_paths)
            #else:
            #    digraph_path = None
            
        return max_flow_digraph
    
    def getResidualGraph(self, source, sink):
        """Get Residual Graph for MaxFlow usage
           Related To: MaxFlow()
        
        Arguments:
            source {String|Integer}         -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
            sink {String|Integer}           -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Graph is not Directed!
        
        Returns:
            Graph       -- Residual Generated Graph
        """
        
        if (self.directed == False):
            raise Exception('Current Graph is not Directed! Transform it to Directed Graph to use ResidualGraph!')
        
        residual_digraph = self.getGraphInstance(deep_copy = True)
        
        residual_digraph.clearEdges()
        
        for edge in list(self.getEdges().values()):
            
            symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
            
            reverse_symbolic_edge = self.getSymbolicEdge(edge[1], edge[0])
            
            if (self.capacity[symbolic_edge] - self.flow[symbolic_edge]) > 0:
                residual_digraph.createEdge(edge)
                self.reverse_edge[symbolic_edge] = self.capacity[symbolic_edge] - self.flow[symbolic_edge]
                self.sink[symbolic_edge] = True
            elif (self.flow[symbolic_edge] > 0):
                residual_digraph.createEdge([edge[1], edge[0]])
                self.reverse_edge[reverse_symbolic_edge] = self.flow[symbolic_edge]
                self.sink[reverse_symbolic_edge] = False
                
        return residual_digraph
                
    
    def getVerticeNeighborhood(self, vertice):
        """Get All Vertices in a Vertice(V1) Neighborhood
           Example: v1 has [v2,v3,v4] as adjacency vertices, this methods returns those vertices
        
        Arguments:
            vertice {String|Vertice}    -- Vertice Key Name. Example: Vertice 'a' or Vertice 2. Name doesn't matter as long it is a primitive.
        
        Raises:
            Exception: Method Not Implemented in Child Class!
        """
        raise Exception('getVerticeNeighborhood(vertice) Not Implemented! You need to Implement this method in your class!')
        
    def getGraphInstance(self, deep_copy = False, directed = False):
        """Get Self Graph Instance as a Copy or New One

           **Method Overriden by Child Class**
        
        Keyword Arguments:
            deep_copy {bool}    -- Generate a new copy of itself or a new one (default: {False})
            directed {bool}     -- If New Graph should be Directed or Not (default: {False})
        
        Raises:
            Exception: Method not Implemented
        """
        raise Exception('graphInstance() Not Implemented! You need to Implement in your class simply returning its self new instance')
        
        
    