class Node:
    def __init__(self, d):
        self.Data, self.Left, self.Right = d, None, None

class Tree:
    def __init__(self, d=None):
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):   # if no node left insert here
                if (n.Left == None):
                    n.Left = Node(d)
                else:          # or try left child
                    __insertHere__(n.Left, d)
            elif (n.Data < d): # if no node right insert here
                if (n.Right == None):
                    n.Right = Node(d)
                else:          # or try right child
                    __insertHere__(n.Right, d)
        if (self.Root == None): # it was an empty tree
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):          # try left child
                if (self.Root.Left == None):  # if empty insert here
                    self.Root.Left = Node(d)
                else:                         # try left subtree
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):        # try right child
                if (self.Root.Right == None): # if empty insert here
                    self.Root.Right = Node(d)
                else:                         # try right subtree
                    __insertHere__(self.Root.Right, d)
    def check(self, d):
        def __check__(n, d):
            if (n == None):
                return False
            elif (n.Data == d):
                return True
            elif (n.Data > d):
                return __check__(n.Left, d)
            elif (n.Data < d):
                return __check__(n.Right, d)
        return __check__(self.Root, d)
    
    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---"*h, n.Data)
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")

    def num_nodes(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.num_nodes(node.Left) + self.num_nodes(node.Right)
    
    def get_graph(self):
        def traverse(node, matrix, graph_dict):
            if node is None:
                return
            if node.Data not in graph_dict:
                graph_dict[node.Data] = len(graph_dict)
            node_index = graph_dict[node.Data]
            if node.Left is not None:
                if node.Left.Data in graph_dict:
                    left_index = graph_dict[node.Left.Data]
                    matrix[node_index][left_index] = abs(node.Data - node.Left.Data)
                traverse(node.Left, matrix, graph_dict)
            if node.Right is not None:
                if node.Right.Data in graph_dict:
                    right_index = graph_dict[node.Right.Data]
                    matrix[node_index][right_index] = abs(node.Data - node.Right.Data)
                traverse(node.Right, matrix, graph_dict)

        graph_dict = {}
        traverse(self.Root, [], graph_dict)
        num_nodes = len(graph_dict)
        graph = [[0] * num_nodes for i in range(num_nodes)]
        traverse(self.Root, graph, graph_dict)
        return graph 

def main():
    myTree = Tree()
    infile = open("numbers.txt", "r")
    file_numbers = []
    for data in infile:
        my_list = data.strip()
        if my_list:
            file_numbers.append(int(my_list))
    infile.close()
    for data in file_numbers:
        myTree.insert(data)
    
    myTree.printPreorder()
    adj_matrix = myTree.get_graph()
    for row in adj_matrix:
        print(row)
 

main()


# graph = [[0, 22, 0, 0, 21]
#          [0,  0, 4, 1,  0]
#          [0,  0, 0, 0,  0]
#          [0,  0, 0, 0,  0]
#          [0,  0, 0, 0,  0]]

# Preoder: 34
#          12
#          8
#          13
#          55

# [[0, 7, 5, 0, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 15],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0]]
13
18
6
33
5