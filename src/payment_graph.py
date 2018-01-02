#class for payment graph
class payment_graph:
    def __init__(self):
        self.adj_list = {}
        self.degree_dict = {}

    def insert_edge(self,payment):
        target = payment['target']
        actor = payment['actor']
        
        self.__add_undirected_edge(target,actor)

    def remove_edge(self,payment):
        target = payment['target']
        actor = payment['actor']

        self.__remove_undirected_edge(target,actor)

    def get_median_degree(self):
        degree = self.degree_dict.values()
        degree.sort()
        n = len(degree)
        return float(degree[n/2]) if n%2==1 else 0.5*(degree[n/2]+degree[n/2-1])

    def __add_undirected_edge(self,v1,v2):
        if v1 in self.adj_list:
            if v2 not in self.adj_list[v1]:
                self.adj_list[v1].append(v2)
        else:
            self.adj_list[v1] = [v2]

        if v2 in self.adj_list:
            if v1 not in self.adj_list[v2]:
                self.adj_list[v2].append(v1)
        else:
            self.adj_list[v2] = [v1]

        self.__gen_degree_dict()

    def __remove_undirected_edge(self,v1,v2):
        if v1 in self.adj_list:
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)

        if v2 in self.adj_list:
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)

        self.__gen_degree_dict()

    def __gen_degree_dict(self):
        self.degree_dict = {v:len(self.adj_list[v]) for v in self.adj_list}

