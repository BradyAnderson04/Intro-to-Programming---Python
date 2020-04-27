# import graph class as module 
import bestgraph as bg

# establish a queue class
class Queue:
    def __init__(self):
        self.q = []
    def dequeue(self):
        return self.q.pop(0)
    def enqueue(self,x):
        self.q.append(x)
    def empty(self):
        return (len(self.q) > 0)
    def __str__(self):
        return "{0}".format(self.q)

# g = graph, node = start
def bfsfull(g,node):
    # establish queue
    visited = []
    q = Queue()
    q.enqueue(node)
    while q.empty():
        n = q.dequeue()
        if (n not in visited):
            print('Visiting:' ,n)
            visited.append(n)
            edges = g.edges[n]
            for e in edges:
                if e not in visited:
                    q.enqueue(e)
            if(edges == []):
                q.enqueue(g.nodes[0])
                # start at first node not in visited
    return visited

if __name__=="__main__":
    my_graph = bg.Graph([1,2,3,4,5,6,7,8])
    elst = [(1,2),(1,3),(2,8),(3,5),(3,4),(5,6),(6,4),(6,7)]
    for i in elst:
        my_graph.add_edge(i)
    bfsfull(my_graph,5)