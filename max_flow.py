
class Vertex(object):
        def __init__(self, vertexname):
            self.name =vertexname
            self.parent = None


# please change vertex_listhere, let me see how to adapt vertex_list here to apply for all situations.          
initial_flow_value = 100000

class Graphic(object):
        def __init__(self):
            self.edge_dict_residual= {}
            self.edge_dict_electrical = {}
            self.Vertex_list = []
            self.edge_number = 0 
            self.vertex_number = 0
            self.total_value = 0
            
        def AddEdge(self, first_vertex, second_vertex, edgecapacity):
            self.edge_dict_residual[(first_vertex,second_vertex)] = edgecapacity
            self.edge_dict_electrical[(first_vertex,second_vertex)]  = edgecapacity
            self.edge_number =  self.edge_number  + 1
            if first_vertex not in self.Vertex_list:
                self.Vertex_list.append(first_vertex)
                self.vertex_number = self.vertex_number + 1 
            if second_vertex not in self.Vertex_list:
                self.Vertex_list.append(second_vertex)
                self.vertex_number = self.vertex_number + 1 
                
        
        def findmaxflow(self):
            while self.findonepath():
                 flow_path = self.findonepath()
                 return_vertex = self.findonepath()
                 flow_value = initial_flow_value

                 while (return_vertex.parent!=None):
                     flow_value = min(flow_value, self.edge_dict_residual[(return_vertex.parent,return_vertex)])
                     return_vertex = return_vertex.parent
                 self.update_edge_dict_residual(flow_path,flow_value)
                 self.total_value = self.total_value + flow_value
            print(self.total_value)


        def update_edge_dict_residual(self,flow_path,flow_value):
            while(flow_path.parent != None ):
                 self.edge_dict_residual[(flow_path.parent,flow_path)]  =  self.edge_dict_residual[(flow_path.parent,flow_path)] - flow_value
                 self.edge_dict_residual[(flow_path, flow_path.parent)] =  flow_value
                 flow_path = flow_path.parent


        def findonepath(self):
             end_vertex =  self.Vertex_list[-1].name
             visited_edge ={}
             checking_list = [self.Vertex_list[0]]
             while (len(checking_list)!=0):
                 starting_vertex = checking_list.pop(0)
                 visited_edge[starting_vertex.name] = True
                 for vertex in self.Vertex_list:
                     if (starting_vertex,vertex) in  self.edge_dict_residual and vertex.name not in visited_edge:
                          if self.edge_dict_residual[(starting_vertex,vertex)] > 0:
                            checking_list.append(vertex)
                            visited_edge[vertex.name] =True
                            vertex.parent = starting_vertex
                            if vertex.name == end_vertex:
                              return self.Vertex_list[-1]
             return False

        def find_maxflow_residualversion(self):
            return self.findmaxflow()

        def find_maxflow_electricversion(self, binary_interval):
            while( (binary_interval[1] - binary_interval[0]) > 10*(-1)):
              total_flow = sum(binary_interval)/2
              if self.testify_binary_search(total_flow):
                  binary_interval[0] = total_flow
              else:
                  binary_interval[1] = total_flow
            return binary_interval[0]
        def edge_initial(self):
            edge_weights = []
            self.list_to_graph = [] 
            for key in self.edge_dict_electrical.keys():
                edge_weights.append(1/self.edge_number)
                self.list_to_graph.append(keys)
            return edge_weights
        def testify_binary_search(self, total_flow):
            edge_weights = self.initial()
            while(i < terminal_iteration ):
                resistance_matrix = self.get_resistance(edge_weights)
                current_electrical_flow = self.get_electrical_flow(total_flow,resistance_matrix)
                energy = self.get_flow_energy(current_electrical_flow,resistance_matrix)
                if energy > 1:
                    return False
                edge_weights = self.update_weights(current_electrical_flow, edge_weights)
                 

        def get_resistance(edge_weights):
            resistance_matrix = np.arrar([self.edge_number, self.edge_number])
            inde = 0
            for edge_weight in edge_weights:
                  resistance_matrix[inde,inde] =  edge_weight/ (self.edge_dict_electrical[(self.list_to_graph[inde])]**2)
            return resistance_matrix
        def get_flow_energy(self, electrical_flow,  resistance_matrix):
            energy  = electrical_flow.T * resistance_matrix * electrical_flow
            return energy
        def get_electrical_flow(self, given_total_value,  resistance_matrix):

            lapcian_matrix = B*inv(resistance_matrix) * B.T
            f = given_total_value * inv(resistance_matrix) * B.T * inv(lapcian_matrix)
            return f
        def get_B_matrix(self):
            pass
            



if __name__ == "__main__":
      g = Graphic()
      vertex_0 = Vertex('0')
      vertex_1 = Vertex('1')
      vertex_2 = Vertex('2')
      vertex_3 = Vertex('3')
      vertex_4 = Vertex('4')
      vertex_5 = Vertex('5')
      vertex_111 = Vertex('5')
      print(vertex_5 == vertex_111)
      g.AddEdge(vertex_0, vertex_1, 16)
      g.AddEdge(vertex_0, vertex_2, 13)
      g.AddEdge(vertex_1, vertex_2, 10)
      g.AddEdge(vertex_1, vertex_3, 12)
      g.AddEdge(vertex_2, vertex_1, 4)
      g.AddEdge(vertex_2, vertex_4, 14)
      g.AddEdge(vertex_3, vertex_2, 9)
      g.AddEdge(vertex_3, vertex_5, 20)
      g.AddEdge(vertex_4, vertex_3, 7)
      g.AddEdge(vertex_4, vertex_5, 4)
      g.findmaxflow()


      
                
            