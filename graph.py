from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search

class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.checked = False
        self.color = None
        
    # def __str__(self):
        


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertex_list.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertex_list associated 
           with the edge.'''
        self.graph = {}
        self.vertices = []
        
        file = open(filename, 'r')
        for line in file:
            self.vertices += line.split()
        file.close()
        
        for v in self.vertices:
            self.add_vertex(v)
            
        for v in range(1, len(self.vertices), 2):
            # print(v)
            right_key = str(self.vertices[v])
            left_key = str(self.vertices[v-1])
            self.add_edge(left_key, right_key)
        
    
        

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if not key in self.graph:
            self.graph[key] = Vertex(key)
            

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        return self.graph[key]
    

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
    
        self.graph[v1].adjacent_to.append(v2)
        self.graph[v2].adjacent_to.append(v1)


    def get_vertex_list(self): #do this with .keys() figure it out 
        '''Returns a list of id's representing the vertex_list in the graph, in ascending order'''
        keys = list(self.graph.keys())
        keys.sort()
        return keys
        # return self.ids.sort()

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertex_list (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        comp_list = []
        stack = Stack(len(self.graph))
        for key in self.graph:
            if not self.graph[key].checked:
                sub_list = []
                stack.push(self.graph[key])
                while not stack.is_empty():
                    s = stack.peek()
                    sub_list.append(stack.pop().id)
                    if not s.checked:
                        s.checked = True
                    adj_list = []
                    for vertex in s.adjacent_to:
                        adj_list.append(vertex)
                    for i in range(len(adj_list)):
                        if not self.graph[adj_list[i]].checked:
                            stack.push(self.graph[adj_list[i]])
                            self.graph[adj_list[i]].checked = True
            sub_list.sort()
            if len(comp_list) == 0 or comp_list[-1] != sub_list:
                comp_list.append(sub_list)
        comp_list.sort(key = lambda x : x[0])
        return comp_list
                
                
                
    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        
        queue = Queue(len(self.graph))
        for k in self.graph:
            
            vertex = self.graph[k]
            queue.enqueue(vertex)
            
            if vertex.color is None:
                vertex.color = True
            while not queue.is_empty():
                vertex = queue.dequeue()
                 # print('START ID: ', self.graph[start].id, 'START COLOR: ', self.graph[start].color)

                for v in vertex.adjacent_to:
                    
                    if self.graph[v].color == vertex.color:
                        return False
                    
                    elif self.graph[v].color is None:
                        if vertex.color == True:
                                    #                 # print('      ADJ ID: ', self.graph[adj].id, 'ADJ COLOR: ', self.graph[adj].color)
                            self.graph[v].color = False
                        else:
                            self.graph[v].color = True
                        queue.enqueue(self.graph[v])
        return True
            
      
        
    def print_graph(self):
        for vertex in self.graph.items():
            print(vertex[0], vertex[1].adjacent_to)
            # for adj in vertex[1].adjacent_to:
            #     print(vertex[0], [adj])
