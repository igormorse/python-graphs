from collections import deque
import random

class Graph:
    
    VERTICES_KEY = 'vertices'
    EDGES_KEY = 'arestas'
    GRAPH_NAME_KEY = 'nome'
    
    GRAPH_REPRESENTATION_TYPES = ['adjacency_matrix', 'adjacency_list']
    
    ADJACENCY_MATRIX = 'adjacency_matrix'
    AJACENCY_LIST = 'adjacency_list'
    
    def __init__(self, graph = None, directed = False):
        
        # Search Implementation
        self.visited = {}
        self.explored = {}
        self.discovered = {}
        
        self.directed = directed
        
        self.capacity = {}
        
        self.flow = {}
        
        self.sink = {}
        
        self.reverse_edge = {}
        
        if graph is not None:
            self.graph = graph
        else:
            self.graph = {}
            self.graph[self.VERTICES_KEY] = []
            self.graph[self.EDGES_KEY] = []
            self.graph[self.GRAPH_NAME_KEY] = []
        
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
        
    def createVertices(self, vertices):
        for vertice in vertices:
            self.createVertice(vertice)
            
    def createEdge(self, edge):
        if (self.edgeExists(edge) == False):
            self.graph[self.EDGES_KEY].append(edge)
            return
        
        raise Exception('Edge is already in Graph!')
        
    def removeEdge(self, edge):
        if (self.edgeExists(edge)):
            del self.graph[self.EDGES_KEY][edge]
            return
        
        raise Exception('Edge not Found in Graph!')
        
    def clearEdges(self):
        for edge in list(self.getEdges().values()):
            self.removeEdge(edge)
        
    def getSymbolicEdge(self, firstVertice, secondVertice):
        return str(firstVertice) + str(secondVertice)
        
    def initializeEdge(self, edge):
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
        self.visited[vertice] = False
        
    def exploreEdge(self, firstVertice, secondVertice):
        self.explored[self.getSymbolicEdge(firstVertice, secondVertice)] = True
        
        if (self.directed == False):
            self.explored[self.getSymbolicEdge(secondVertice, firstVertice)] = True
        
    def discoverEdge(self, firstVertice, secondVertice):
        self.discovered[self.getSymbolicEdge(firstVertice, secondVertice)] = True
        
        if (self.directed == False):
            self.discovered[self.getSymbolicEdge(secondVertice, firstVertice)] = True
        
    def createCapacity(self, edge, capacity = 0):
        if self.edgeExists(edge):
            self.capacity[self.getSymbolicEdge(edge[0], edge[1])] = capacity
            return True
            
        return False
        
    def createFlow(self, edge, flow = 0):
        if self.edgeExists(edge):
            self.flow[self.getSymbolicEdge(edge[0], edge[1])] = flow
            return True
            
        return False
        
    def resetState(self):
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
        for vertice in self.getVertices():
            if(self.visited[vertice] == False):
                self.search(vertice)
        
    def search(self, vertice = None):
        
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
        self.search()
        for vertice in self.getVertices():
            if(self.visited[vertice] == False):
                return False
        return True
        
    def hasCicle(self):
        self.fullSearch()
        
        for edge in self.getEdges().keys():
            if not self.discovered[edge]:
                return True
        return False
        
    def hasForest(self):
        return not self.hasCicle() 
    
    def isTree(self, alternative = False):
        
        if not alternative:
            self.search()
            
            for vertice in self.getVertices():
                if(self.visited[vertice] == False):
                    return False
            
            for edge in list(self.getEdges().values()):
                if(self.discovered[edge] == False):
                    return False;
        else:
            return self.isConnected() and not self.hasCicle()

        return True
    
    def getForestGeneratorGraph(self):
        
        newGraph = self.getGraphInstance()
        
        newGraph.createVertices(self.getVertices())
        
        self.fullSearch()
        
        for edge in list(self.getEdges().values()):
            symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
            if self.discovered[symbolic_edge]:
                newGraph.createEdge(edge)
                
        return newGraph
    
    
    def depthSearch(self, vertice, recursive = False):
        
        self.visited[vertice] = True;
        
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
                            self.exploreEdge(vertice, neighborhoodVertice)
                    else:
                        self.exploreEdge(vertice, neighborhoodVertice)
                        self.discoverEdge(vertice, neighborhoodVertice)
                        self.visited[nextNeighborhoodVertice] = True
                        stack.append([nextNeighborhoodVertice, self.getVerticeNeighborhoodAfter(nextNeighborhoodVertice)])
                    
    def getVerticeNeighborhoodAfter(self, vertice, neighborhoodVertice = None):
        
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
        
        self.visited[start_vertice] = True;
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
        self.visited[start_vertice] = True;
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
        
        paths = []
        
        graphs_paths = []
        
        visited = {}

        for vertice in self.getVertices():
            visited[vertice] = False
        
        self.getAllGraphPaths(origin_vertice, destination_vertice, visited, paths, graphs_paths)
        
        return graphs_paths
    
    def getAllGraphPaths(self, origin_vertice, destination_vertice, visited, paths, graphs_paths): 
  
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
                      

        paths.pop()
        
        visited[origin_vertice] = False
    
    def distancesToVertice(self, vertice):
        
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
        
        if (self.directed == False):
            raise Exception('Current Graph is not Directed! Transform it to Directed Graph to use MaxFlow!')
        
        #flow = {}
        
        max_flow_digraph = 0
        
        for edge in list(self.getEdges().values()):
            self.flow[self.getSymbolicEdge(edge[0], edge[1])] = 0
            
        residual_digraph = self.getResidualGraph(source, sink)
        
        self.show()
        
        residual_possible_paths = residual_digraph.breadthStartToEndSearch(source, sink).getGraphPaths(source, sink)
        
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
        raise Exception('getVerticeNeighborhood(vertice) Not Implemented! You need to Implement this method in your class!')
        
    # ToDo
    def getGraphInstance(self, copy = False):
        raise Exception('graphInstance() Not Implemented! You need to Implement in your class simply returning its self new instance')
        
        
    