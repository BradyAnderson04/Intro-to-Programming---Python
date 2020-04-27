class Graph:
    def __init__(self,nodes):
        self.nodes = nodes
        self.edges = {}
        for i in self.nodes:
            self.edges[i] = []
    def add_edge(self, pair):
        # add a node if not in graph and then add val to that node's edge
        start,end = pair
        if(start not in self.nodes or end not in self.edges[start]):
            if(start not in self.nodes):
                self.add_node(start)
                self.edges[start] = []
            self.edges[start].append(end)
            return 1
        else:
            return -1
    def children(self,node):
        return self.edges[node]
    def nodes(self):
        return str(self.nodes)
    def __str__(self):
        return str(self.edges)
    def add_node(self, n):
        if(n in self.nodes):
            return -1
        else:
            self.nodes.append(n)
            return 1
    def del_node(self, n):
        if(n in self.nodes and n in self.edges):
            self.nodes.remove(n)
            del self.edges[n]
            return 1
        else:
            return -1
    def del_edge(self, pair):
        try:
            start, end = pair
            self.edges[start] = [x for x in self.edges[start] if x != end]
            return 1
        except:
            return -1
    def reachable(self, pair):
        start, end = pair
        current = start
        # worshawls algorithm https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
        while(current != end):
            if(current != end and self.edges[start] != [] and bool(self.edges[current])):
                current = self.edges[start].pop()
            elif(current != end and bool(self.edges[current])): 
                current = self.edges[current].pop()
            elif(current != end and not bool(self.edges[current])):
                return False
        return True

        



# Testing Area
g = Graph([1, 2, 3, 4, 5])
g.add_edge((2,3))
g.add_edge((1,2))
g.add_edge((4,5))
print(g.edges)
# print(g.edges[2].pop())
print(g.reachable((1, 5)))