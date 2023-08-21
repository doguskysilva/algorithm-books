class Node:

    def __init__(self, value):
        self.value = value
        self.color = "white"
        self.distance = None
        self.next = None

    def __str__(self):
        return f'{self.value} - {self.color} - {self.distance}'


class Graph():

    def __init__(self):
        self.graph = []

    def find_position(self, value):
        for idx, edges in enumerate(self.graph):
            head = edges[0]
            if head.value == value:
                return idx
        return None

    def find_node(self, value):
        for edges in self.graph:
            head = edges[0]
            if value == head.value:
                return head
        return None

    def add_node(self, node):
        self.graph.append([node])
        return len(self.graph) - 1

    def adjacencies(self, node):
        index = self.find_position(node.value)
        return self.graph[index]

    def add_edge(self, src, dest):
        head_dest = self.graph[dest][0]
        src_list = self.graph[src]

        src_list.append(head_dest)


    def add_adj(self, src, dests):
        index_src = self.find_position(src)

        if index_src == None:
            index_src = self.add_node(Node(src))

        for dest in dests:
            index_dest = self.find_position(dest)
            node_dest = None

            if index_dest == None:
                node_dest = Node(dest)
                index_dest = self.add_node(node_dest)
            else:
                node_dest = self.graph[index_dest][0]

            self.add_edge(index_src, index_dest)

    def __str__(self):
        return f'{self.graph}'

    def print(self):
        for edges in self.graph:
            adj = [node.value for node in edges]

            print(" -> ".join(adj))


if __name__ == "__main__":
    graph = Graph()

    graph.add_adj("v", ["r"])
    graph.add_adj("r", ["s", "v"])
    graph.add_adj("s", ["r", "w"])
    graph.add_adj("w", ["s", "t", "x"])
    graph.add_adj("t", ["w", "x", "u"])
    graph.add_adj("x", ["t", "u", "w"])
    graph.add_adj("u", ["x", "y", "t"])
    graph.add_adj("y", ["x", "u"])
    
    graph.print()

    print("\n =============== BSF =============== \n")

    
    ## Start BSF
    start_search = "s"
    
    s = graph.find_node("s")
    
    s.color = "gray"
    s.distance = 0
    s.next = None
    
    Q = []
    Q.append(s)

    while Q:
        u = Q.pop()
        for v in graph.adjacencies(u):
            if v.color == "white":
                v.color = "cinza"
                v.distance = u.distance + 1
                v.next = u
                Q.append(v)

        u.color = "black"

    for edges in graph.graph:
        print(edges[0])


