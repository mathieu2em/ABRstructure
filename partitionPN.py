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
    # we want a partition of size m in which each node contains a suite
    # of numbers for Xi to Xi+1 Xi is the key and Xi+1 is the value
    # we need to define the size of
    def __init__(self, m):
        self.BT = BinaryTree(self)


if __name__ is '__main__':
    partition = PartitionPN()
