import math
import numpy as np
from cvxopt  import solvers, matrix 
class Vertex(object):
        def __init__(self, vertexname):
            self.name =vertexname
            self.parent = None

class Graphic(object):
        def __init__(self):
            self.edge_dict_residual= {}
            self.edge_dict_electrical = {}
            self.Vertex_list = []
            self.edge_number = 0 
            self.vertex_number = 0
            self.total_value = 0
            self.epsilon = 0.5
            self.sigma = 0.1
            
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

        def find_maxflow_electricversion(self):
            binary_interval = self.interval_initial()
            binary_interval[1] =100
            while( (binary_interval[1] - binary_interval[0]) > 0.01):
              given_flow = sum(binary_interval)/2
              result = self.testify_binary_search(given_flow)
              if result[0]:
                  binary_interval[0] = given_flow 
                  average_flow = result[1]/self.get_ternimal_condition()

              else:
                  binary_interval[1] = given_flow*(1 - self.epsilon)
            return (binary_interval[0],average_flow)

        def get_ternimal_condition(self):
            iteration_number = 2 * ((1-self.epsilon)/(self.epsilon - self.sigma))**2 * math.log(self.edge_number)*self.edge_number/self.epsilon 
            return iteration_number

        def testify_binary_search(self, given_flow):
            edge_weights = self.edge_initial()
            i =  1
            terminal_iteration = self.get_ternimal_condition()
            sum_flow = np.zeros((self.edge_number,1))
            while(i <= terminal_iteration ):
                resistance_matrix = self.get_resistance(edge_weights)
                current_electrical_flow = self.get_electrical_flow(given_flow, resistance_matrix)

                energy = self.get_flow_energy(current_electrical_flow, resistance_matrix)

                sum_flow = sum_flow + current_electrical_flow
                if energy > 1:
                    return (False, 0)
                edge_weights = self.update_weights(current_electrical_flow, edge_weights)    
                i = i + 1

            return (True, sum_flow)
        
        def update_weights(self,current_electrical_flow, edge_weights):

            for i in range(self.edge_number):
                edge_weights[i] = edge_weights[i] * (1 + abs(current_electrical_flow[i])/self.edge_dict_electrical[self.list_to_graph[i]])

            return np.array(edge_weights)/sum(edge_weights)

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
        def get_electrical_flow_cvx(self,given_total_value, resistance_matrix):
            P = matrix(resistance_matrix)
            q_e = matrix(np.zeros(self.edge_number))
            G = -matrix(self.get_B_matrix())
            h_e = -matrix(given_total_value* self.X_st)
            sol = solvers.qp(P,q_e,G,h_e) 
            return sol['x']

        def get_electrical_flow(self, given_total_value,  resistance_matrix):

            B = self.get_B_matrix()
            lapcian_matrix = np.dot(np.dot(B,np.linalg.inv(resistance_matrix)),B.T )
            additional_constraint = np.zeros(self.vertex_number)
            additional_constraint[0] =1

            A  = np.vstack((lapcian_matrix,additional_constraint))
            b_vertor =  given_total_value * self.X_st
            b_vertor = np.vstack((b_vertor,1))

            A = np.mat(A)
            b_vertor = np.mat(b_vertor)

            #phi = np.linalg.solve(lapcian_matrix, given_total_value * self.X_st) 
            #f = np.dot(np.dot(np.linalg.inv(resistance_matrix) , B.T ), phi)
            f = given_total_value * np.dot(np.dot(np.dot(np.linalg.inv(resistance_matrix) , B.T ), np.linalg.pinv(lapcian_matrix)), self.X_st )
          
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
            self.X_st = np.zeros((self.vertex_number,1))
            self.X_st[0] = 1
            self.X_st[-1] = -1
            edge_weights = []
            self.list_to_graph = [] 
            for key in self.edge_dict_electrical.keys():
                edge_weights.append(1/self.edge_number)
                self.list_to_graph.append(key)
            return edge_weights
        def interval_initial(self):
            binary_interval = np.zeros(2)
            binary_interval[0] = 1
            for key in self.edge_dict_electrical.keys():
                if self.Vertex_list[0] in key:
                    binary_interval[1] = binary_interval[1] + self.edge_dict_electrical[key]
            return binary_interval

        ####################### 我是分割线

        def find_maxflow_residualversion(self):
            return self.findmaxflow()

        def findmaxflow(self):
            while self.findonepath():
                 flow_path = self.findonepath()
                 return_vertex = self.findonepath()
                 flow_value = 100000

                 while (return_vertex.parent!=None):
                     flow_value = min(flow_value, self.edge_dict_residual[(return_vertex.parent,return_vertex)])
                     return_vertex = return_vertex.parent
                 self.update_edge_dict_residual(flow_path,flow_value)
                 self.total_value = self.total_value + flow_value
            return self.total_value


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


            
if __name__ == "__main__":
      g = Graphic()
      vertex_0 = Vertex('0')
      vertex_1 = Vertex('1')
      vertex_2 = Vertex('2')
      vertex_3 = Vertex('3')
      vertex_4 = Vertex('4')
      vertex_5 = Vertex('5')
      g.AddEdge(vertex_0, vertex_1, 11)
      g.AddEdge(vertex_0, vertex_2, 13)
      g.AddEdge(vertex_1, vertex_2, 10)
      g.AddEdge(vertex_1, vertex_3, 12)
      g.AddEdge(vertex_2, vertex_4, 14)
      g.AddEdge(vertex_3, vertex_2, 9)
      g.AddEdge(vertex_3, vertex_5, 10)
      g.AddEdge(vertex_4, vertex_3, 7)
      g.AddEdge(vertex_4, vertex_5, 4)
      print('approximate_solution:',g.find_maxflow_electricversion())
      print('exact_solution:',g.find_maxflow_residualversion())