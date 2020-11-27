import numpy as np
import math
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
            self.epsilon = 0.1
            
            
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

        def find_maxflow_electricversion(self):

            binary_interval = np.zeros(2)
            binary_interval[0] = 1
            binary_interval[1] = sum(self.edge_dict_electrical.values())
            while( (binary_interval[1] - binary_interval[0]) > 0.1):
              total_flow = sum(binary_interval)/2
              if self.testify_binary_search(total_flow):
                  binary_interval[0] = total_flow
              else:
                  binary_interval[1] = total_flow
            return binary_interval[1]
        def get_ternimal_condition(self):

            iteration_number = math.log(self.edge_number)*self.edge_number/self.epsilon * 2 * (self.epsilon/(1-2*self.epsilon))**2
            return iteration_number

        def testify_binary_search(self, total_flow):
            edge_weights = self.edge_initial()
            i =  1
            terminal_iteration = self.get_ternimal_condition()
            while(i < terminal_iteration ):
                resistance_matrix = self.get_resistance(edge_weights)
                current_electrical_flow = self.get_electrical_flow(total_flow,resistance_matrix)
                energy = self.get_flow_energy(current_electrical_flow,resistance_matrix)
 
                if energy > 1:
                    return False
                edge_weights = self.update_weights(current_electrical_flow, edge_weights)    
                i = i + 1
        
        
        def update_weights(self,current_electrical_flow, edge_weights):
            sum = 0
            for i in range(self.edge_number):
                edge_weights[i] = edge_weights[i] * (1 + abs(current_electrical_flow[i])/self.edge_dict_electrical[self.list_to_graph[i]])
                sum = sum + edge_weights[i]
            return edge_weights/sum

        def get_resistance(self,edge_weights):
 
            resistance_matrix = np.zeros((self.edge_number, self.edge_number))
            inde = 0
            for edge_weight in edge_weights:
                  resistance_matrix[inde,inde] =  edge_weight/ (self.edge_dict_electrical[self.list_to_graph[inde]]**2)
                  inde = inde + 1
            return resistance_matrix
        def get_flow_energy(self, electrical_flow,  resistance_matrix):
            energy  = np.dot(np.dot(electrical_flow.T , resistance_matrix), electrical_flow)
            return energy

        def get_electrical_flow(self, given_total_value,  resistance_matrix):
            B = self.get_B_matrix()
            lapcian_matrix = np.dot(np.dot(B,np.linalg.inv(resistance_matrix)),B.T )
            lfside = lapcian_matrix
            rtside = given_total_value * self.X_st
            

            '''
            try:
                np.linalg.inv(lapcian_matrix)
            except:
                f = given_total_value * np.dot(np.dot(np.dot(np.linalg.inv(resistance_matrix) , B.T ), np.linalg.pinv(lapcian_matrix)), self.X_st )
            else:
                f = given_total_value * np.dot(np.dot(np.dot(np.linalg.inv(resistance_matrix) , B.T ), np.linalg.inv(lapcian_matrix)), self.X_st )
            '''
            f = given_total_value * np.dot(np.dot(np.dot(np.linalg.inv(resistance_matrix) , B.T ), np.linalg.pinv(lapcian_matrix)), self.X_st )
            '''
            import pdb
            pdb.set_trace()
            phi = np.linalg.solve(lfside,rtside)
            f = np.dot(np.dot(np.linalg.inv(resistance_matrix) , B.T ), phi)
            '''
            return f
        def get_B_matrix(self):
            B_matrix = np.zeros((self.vertex_number, self.edge_number))
            inde = 0
            for vertex in self.edge_dict_electrical.keys():
                B_matrix[int(vertex[0].name), inde] = 1
                B_matrix[int(vertex[1].name), inde] = - 1
                inde = inde + 1
            return B_matrix
        def edge_initial(self):
            self.X_st = np.zeros(self.vertex_number)
            self.X_st[0] = 1
            self.X_st[1] = -1
            edge_weights = []
            self.list_to_graph = [] 
            for key in self.edge_dict_electrical.keys():
                edge_weights.append(1/self.edge_number)
                self.list_to_graph.append(key)
            return edge_weights
            

if __name__ == "__main__":
      g = Graphic()
      vertex_0 = Vertex('0')
      vertex_1 = Vertex('1')
      vertex_2 = Vertex('2')
      vertex_3 = Vertex('3')
      vertex_4 = Vertex('4')
      vertex_5 = Vertex('5')
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
      # g.find_maxflow_residualversion()
      print(g.find_maxflow_electricversion())


      
                
            