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
        """
        Creates num_nodes method

        Recursively checks the number of nodes in a subtree.
        """
        if node == None:
            return 0
        else:
            return 1 + self.num_nodes(node.Left) + self.num_nodes(node.Right)
    
    def get_graph(self):
        """
        Creates get_graph method

        Creates an adjacency matrix of the binary tree.
        """
        def traverse(node, matrix, graph_dict):
            """
            Creates transverse method

            Recursively transverses the tree using preorder transversal.
            """
            if node is None:
                return
            # Stores node values in a dictionary
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
        # Creates the empty dictionary
        graph_dict = {}
        traverse(self.Root, [], graph_dict)
        num_nodes = len(graph_dict)
        # Creates the graph per the number of nodes
        graph = [[0] * num_nodes for i in range(num_nodes)]
        traverse(self.Root, graph, graph_dict)
        return graph 

def main():
    """
    Creates main function

    Creates class objects and calls necessary methods.
    """
    # Creates an object of the tree class
    myTree = Tree()
    # Read the file and stores it in a list
    infile = open("numbers.txt", "r")
    file_numbers = []
    for data in infile:
        my_list = data.strip()
        if my_list:
            file_numbers.append(int(my_list))
    infile.close()
    # For each number in the list insert it into the tree
    for data in file_numbers:
        myTree.insert(data)
    # Prints the binary tree and matrix using preorder traversal.
    myTree.printPreorder()
    adj_matrix = myTree.get_graph()
    for row in adj_matrix:
        print(row)
 

main()
