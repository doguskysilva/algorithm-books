class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.value}'


class Graph():

    def __init__(self):
        self.graph = []

    def find_position(self, value):
        for idx, edges in enumerate(self.graph):
            head = edges[0]
            if head.value == value:
                return idx
        return None

    def add_node(self, node):
        self.graph.append([node])
        return len(self.graph) - 1

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

   # graph.add_node(Node("v"))
   # graph.add_node(Node("r"))
   # graph.add_node(Node("s"))
   # graph.add_node(Node("w"))
   # graph.add_node(Node("t"))
   # graph.add_node(Node("x"))
   # graph.add_node(Node("u"))
   # graph.add_node(Node("y"))

   # graph.add_edge(0, 1)
   # graph.add_edge(1, 0)
   # graph.add_edge(1, 2)

    graph.add_adj("v", ["r"])
    graph.add_adj("r", ["s", "v"])
    graph.add_adj("s", ["r", "w"])
    graph.add_adj("w", ["s", "t", "x"])
    graph.add_adj("t", ["w", "x", "u"])
    graph.add_adj("x", ["t", "u", "w"])
    graph.add_adj("u", ["x", "y", "t"])
    graph.add_adj("y", ["x", "u"])
    
    graph.print()
    

