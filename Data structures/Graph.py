class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)
        
if __name__ == '__main__':  
    routes = [
        ('abuja', 'lagos'),
        ('abuja', 'jos'),
        ('lagos', 'jos'),
        ('lagos', 'minna'),
        ('jos', 'minna'),
        ('minna', 'kaduna')
    ]
    
    route_graph = Graph(routes)