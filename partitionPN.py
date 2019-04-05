class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    # class for individual nodes
    class Node:
        def __init__(self, key=None, value=None, N=None, left=None, right=None):
            self.right = right
            self.left = left
            self.value = value
            self.key = key
            self.N = N

    def size(self):
        return self.__size__(self.root)

    def __size__(self, node):
        if node is None:
            return 0
        else:
            return node.N

    def put(self, key, val):
        self.root = self.__put__(self.root, key, val)

    def __put__(self, node, key, val):
        if node is None:
            return self.Node(key, val)
        if key < node.key:
            node.left = self.__put__(node.left, key, val)
        elif key > node.key:
            node.right = self.__put__(node.right, key, val)
        else:
            node.value = val

    def get(self, key):
        return self.__get__(self.root, key)

    def __get__(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self.__get__(node.left, key)
        elif key >= node.key:
            return self.__get__(node.right, key)
        else:
            return node


class PartitionPN:
    # We will use a BST to represent our partition of positive numbers from 0(included) to m(excluded)
    # each node of the BST will represent a split in the partition.
    # for example if we have a partition composed of one continuous
    # suite of positive numbers from
    # [0 , 100[ will have two nodes : the root will be 100 and the left node will be 0.
    # to know the size of an interval , the left number ( here zero ) is represented by the node
    # to the left or our own node if the node to the left is null . and the right number is the actual node.
    def __init__(self, m):
        self.BT = BinaryTree(self)

    # return interval [Xi-1, Xi[ containing x
    def recherche(self,x):



if __name__ is '__main__':
    partition = PartitionPN()
