class Edge(object):
        def __init__(self, nodename ):
           self.nodename= nodename
class Vertex(object):
        def __init__(self, vertexname):
            self.name =vertexname
            self.parent = None
all_name =[]
class Graphic(object):
        def __init__(self):
              self.graphdict= {}
        def AddEdge(self, first_vertex, second_vertex, edgecapacity):
              self.graphdict[(first_vertex,second_vertex)] = edgecapacity
        def findmaxflow(self):

            if self.findonepath():
                 return_vertex = self.findonepath()
                 flow_value = 0
                 while (return_vertex.parent!=None):

                     flow_value = max(flow_value, self.graphdict[(return_vertex.parent.name,return_vertex.name)])

                     print(return_vertex.name)
                     return_vertex = return_vertex.parent
                 print(return_vertex.name)
        def findonepath(self):
             initial_vertex = '0'
             end_vertex =  '5'
             visited_edge ={}
             flowpath = {}
             Vertex_list = [Vertex('0'),Vertex('1'),Vertex('2'),Vertex('3'),Vertex('4'),Vertex('5')]
             checking_list = [Vertex_list[0]]
             while (len(checking_list)!=0):
                 starting_vertex = checking_list.pop(0)
                 for vertex in Vertex_list:
                     if (starting_vertex.name,vertex.name) in  self.graphdict and (vertex.name) not in visited_edge:
                         checking_list.append(vertex)
                         visited_edge[vertex.name] =True
                         vertex.parent = starting_vertex
                         if vertex.name == end_vertex:
                           return Vertex_list[-1]
             return False
if __name__ == "__main__":
      g = Graphic()
      g.AddEdge('0', '1', 16)
      g.AddEdge('0', '2', 13)
      g.AddEdge('1', '2', 10)
      g.AddEdge('1', '3', 12)
      g.AddEdge('2', '1', 4)
      g.AddEdge('2', '4', 14)
      g.AddEdge('3', '2', 9)
      g.AddEdge('3', '5', 20)
      g.AddEdge('4', '3', 7)
      g.AddEdge('4', '5', 4)
      g.findmaxflow()

                
            