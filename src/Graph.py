
import queue
class Graph(object):

    def __init__(self, vertices):
        self.graph = {}
        for vertex in range(vertices):
            self.graph[vertex] = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex]

    def add_neighbour(self, source, dest,weight):
        if dest in self.graph:
            self.graph[source].__setitem__(dest,weight)
        else:
            return None

    def __str__(self):
        for source, neighbours in self.graph.items():
            print('{0} -> {1}'.format(source, neighbours))

    def bfs(self,first):
        visited = [False] * len(self.graph)
        q = queue.Queue()
        q.put(first)
        visited[first] = True
        while(not q.empty()):
            w = q.get()
            print(w)
            for neighbour in self.graph.get(w):
                if not visited[neighbour]:
                    q.put(neighbour)
                    visited[neighbour] = True


if __name__ == '__main__':
    graph = Graph(4)
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_neighbour(0, 1, 2.3)
    graph.add_neighbour(1, 0, 2.6)
    graph.add_neighbour(1, 2, 4.12)
    graph.add_neighbour(2, 0, 4.59)
    graph.add_neighbour(2, 3, 13.06)
    graph.add_neighbour(3,1,1.2)
    graph.__str__()
    graph.bfs(0)


