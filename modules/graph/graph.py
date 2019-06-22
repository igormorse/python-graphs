from collections import deque
class Graph:
    
    VERTICES_KEY = 'vertices'
    EDGES_KEY = 'arestas'
    GRAPH_NAME_KEY = 'nome'
    
    GRAPH_REPRESENTATION_TYPES = ['adjacency_matrix', 'adjacency_list']
    
    ADJACENCY_MATRIX = 'adjacency_matrix'
    AJACENCY_LIST = 'adjacency_list'
    
    def __init__(self, graph = None):
        
        # Search Implementation
        self.visited = {}
        self.explored = {}
        self.discovered = {}
        
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
        for edge in self.getEdges():
            self.removeEdge(edge)
        
    def getSymbolicEdge(self, firstVertice, secondVertice):
        return str(firstVertice) + str(secondVertice)
        
    def initializeEdge(self, edge):
        symbolic_edge = self.getSymbolicEdge(edge[0], edge[1])
            
        inversed_symbolic_edge = self.getSymbolicEdge(edge[1], edge[0])
        
        self.explored[symbolic_edge], self.explored[inversed_symbolic_edge] = False, False
        self.discovered[symbolic_edge], self.discovered[inversed_symbolic_edge] = False, False
    
    def initializeVertice(self, vertice):
        self.visited[vertice] = False
        
    def exploreEdge(self, firstVertice, secondVertice):
        self.explored[self.getSymbolicEdge(firstVertice, secondVertice)] = True
        self.explored[self.getSymbolicEdge(secondVertice, firstVertice)] = True
        
    def discoverEdge(self, firstVertice, secondVertice):
        self.discovered[self.getSymbolicEdge(firstVertice, secondVertice)] = True
        self.discovered[self.getSymbolicEdge(secondVertice, firstVertice)] = True
        
        
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
            
            for edge in self.getEdges():
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

    def breadthSearch(self, vertice):
        
        self.visited[vertice] = True;
        queue = deque([])
        queue.append(vertice)

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
    
    def distancesToVertice(self, vertice):
        
        distances = {}
        
        for vertice in self.getVertices():
            distances[vertice] = None
        
        queue = deque([])
        
        self.visited[vertice] = True
        
        queue.append([vertice, 1])
        
        while(queue):
            popedEdge = queue.popleft()
            
            for neighborhoodVertice in self.getVerticeNeighborhood(vertice):
                if self.visited[neighborhoodVertice]:
                    if not self.explored[self.getSymbolicEdge(vertice, neighborhoodVertice)]:
                        self.exploreEdge(vertice, neighborhoodVertice)
                else:
                    self.exploreEdge(vertice, neighborhoodVertice)
                    self.discoverEdge(vertice, neighborhoodVertice)
                    
                    self.visited[neighborhoodVertice] = True
                    
                    distances[neighborhoodVertice] = popedEdge[1]
    
                    queue.append([neighborhoodVertice, popedEdge[1] + 1])
                    
        return distances
        
    @staticmethod
    def getMaxFlow(digraph, source, sink):
        
        # if self.digraph = False:
            # Exception Grafo não é Digrafo
        
        flow = {}
        
        max_flow_digraph = 0
        
        for edge in digraph.getEdges():
            flow[digraph.getSymbolicEdge(edge[0], edge[1])] = 0
            
        residual_digraph = getResidualGraph(digraph, source, sink)
        
        digraph_path = BuscaCaminhoAumentante(residual_digraph, source, sink) # Verificar também como implementar essa função.
        
        residual_capacity = 0
        
        while digraph_path != None:
            residual_capacity = digraph_path.map {|uv| }.min() # Implementação em Ruby, tem que ver como faz em Python
            
            max_flow_digraph += residual_capacity
            
            for edge in digraph_path.getEdges():
                
                symbolic_edge = digraph_path.getSymbolicEdge(edge[0], edge[1])
                
                if (sink[symbolic_edge]):
                    flow[symbolic_edge] += residual_capacity
                else
                    flow[symbolic_edge] -= residual_capacity
                    
            residual_digraph = getResidualGraph(digraph, source, sink)
            digraph_path = BuscaCaminhoAumentante(residual_digraph, source, sink) # Verificar também como implementar essa função.
            
        return max_flow_digraph
    
    @staticmethod
    def getResidualGraph(digraph, source, sink):
        
        # if self.digraph = False:
            # Exception Grafo não é Digrafo
        
        residual_digraph = digraph.getGraphInstance(True)
        
        residual_digraph.clearEdges()
        
        capacity, flow, reverse_edge = {}, {}, {}
        
        for edge in digraph.getEdges():
            
            symbolic_edge = digraph.getSymbolicEdge(edge[0], edge[1])
            
            reverse_symbolic_edge = digraph.getSymbolicEdge(edge[1], edge[0])
            
            if (capacity[symbolic_edge] - flow[symbolic_edge]) > 0:
                residual_digraph.createEdge(edge)
                reverse_edge[symbolic_edge] = capacity[symbolic_edge] - flow[symbolic_edge]
                sink[symbolic_edge] = True
            elif (flow[symbolic_edge] > 0):
                residual_digraph.createEdge([edge[1], edge[0]])
                reverse_edge[reverse_symbolic_edge] = flow[symbolic_edge]
                sink[reverse_symbolic_edge] = False
                
        return residual_digraph
                
    
    def getVerticeNeighborhood(self, vertice):
        raise Exception('getVerticeNeighborhood(vertice) Not Implemented! You need to Implement this method in your class!')
        
    # ToDo
    def getGraphInstance(self, copy = False):
        raise Exception('graphInstance() Not Implemented! You need to Implement in your class simply returning its self new instance')
        
        
    