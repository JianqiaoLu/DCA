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
            # 对于每一个vertex都能独立的生成一个edge向量用以表示和他的所属关系。。
        def reset(self):
            for vertex in self.vertex_list:
                self.discovered[vertex] = False
                vertex.parent = -1 
                vertex.priority = None
                for adject_vertex in self.vertex_list:
                   self.edge[(vertex, adject_vertex)]  = 'undetermiend'

        def AddEdge(self, first_vertex, second_vertex, edgecapacity):
            self.edge[(first_vertex,second_vertex)] = edgecapacit
def DFS(edge_list):
    layer = [vertex_list[0]]
    while layer:
        current_vertex = layer.pop(-1)
        name = current_vertex.value
        adjencent = edge_list[name]
        for adjencent_vertex in adjencent:
            if not visited[adjencent_vertex]:
                  visited[adjencent_vertex] = True
                  layer.append(adjencent_vertex)
                  adjencent_vertex.parent = current_vertex
                  if adjencent_vertex =  vertex_list[0]
                  return "find a cycle"
    return 'there exists no cycle'
def DFSforclassification(specimemen_list, judgement_list):
    adjent_judgement = [[] for i in range(len(specimemen_list))]
    for speci_single_a in specimemen_list:
        for speci_single_b in specimemen_list:
            if judgement_list(speci_single_a, speci_single_b) or judgement_list(speci_single_a, speci_single_b):
                adjent_judgement[speci_single_a].append((speci_single_b)) 
                adjent_judgement[speci_single_b].append((speci_single_a))
    layer = [specimemen_list[0]]
    layer_total = specimemen_list
    While[layer_total]:
        layer = [layer_total.pop(-1)]
        while layer:
            current_speci = layer.pop(-1)
            adjencent = adjent_judgement(current_speci)
            for adjencent_speci in adjencent:
                if not visited[adjencent_speci]:
                    visited[adjencent_speci] = True
                    if judgement_list((current_speci, adjencent_speci)) or judgement_list((current_speci, adjencent_speci)):
                        adjencent_speci.specyclass = current_speci.specyclass
                    else
                        adjencent_speci.specyclass = not current_speci.specyclass
                    layer.append(adjencent_speci)

                    adjencent_vertex.parent = current_speci
                else
                   if judgement_list((current_speci, adjencent_speci)) or judgement_list((current_speci, adjencent_speci)):
                       if current_speci.specyclass != adjencent_speci.specyclass:
                           return False
                   else:
                        if current_speci.specyclass == adjencent_speci.specyclass:
                            return False

if __name__ == "__main__":
    vertex_list = [[] for i in range(5)]
    print(vertex_list)
    # we firstly define the DFS algorithms:
    