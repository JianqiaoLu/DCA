class Vertex(object):
        def __init__(self, vertexname):
            self.name =vertexname
            self.parent = None
            self.priority = None
            self.status = 'Undiscovered'

class Graph(object):
        def __init__(self):
            self.vertex_list = []
            self.total_value = 0 
            self.discovered = {}
            self.edge = {}
            # maybe i need to install a incidence matrix instead of adjacency matrix (adjacency will cause more redundancy)
        def reset(self):
            for vertex in self.vertex_list:
                self.discovered[vertex] = False
                vertex.parent = -1 
                vertex.priority = None
                for adject_vertex in self.vertex_list:
                   self.edge[(vertex, adject_vertex)]  = 'undetermiend'

        def AddEdge(self, first_vertex, second_vertex, edgecapacity):
            self.edge[(first_vertex,second_vertex)] = edgecapacit