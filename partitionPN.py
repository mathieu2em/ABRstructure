import math


class BinaryTree:
    def __init__(self, rootkey, rootvalue=0):
        self.root = BinaryTree.Node(rootkey,rootvalue)

    # class for individual nodes
    class Node:
        def __init__(self, key=None, value=None, N=0, left=None, right=None):
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
            return self.Node(key, val, 1)
        if key < node.key:
            node.left = self.__put__(node.left, key, val)
        elif key > node.key:
            node.right = self.__put__(node.right, key, val)
        else:
            node.value = val
        node.N = self.__size__(node.left) + self.__size__(node.right)
        return node

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

    def deleteMin(self):
        if self.root is None:
            return
        self.root = self._deleteMin(self)

    def _deleteMin(self, node):
        if node.left is None:
            return node
        else:
            node.left = self._deleteMin(self, node.left)
            node.n = self.__size__(node.left) + self.__size__(node.right) + 1
            return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key > node.key:
            node.right = self._delete(node.right, key)
        elif node.key < key:
            node.left = self._delete(node.left, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            tNode = node
            node = min(tNode.right)
            node.right = self._deleteMin(tNode.right)
            node.left = tNode.left
        node.N = self.__size__(node.left) + self.__size__(node.right)
        return node

    def printBST(self):
        if self.root is None:
            print('empty')
        else:
            print(self.root.value)
            self.__printBST__(self.root.left)
            self.__printBST__(self.root.right)

    def __printBST__(self, node):
        if node is None:
            print('empty')
        else:
            print(node.value)
            self.__printBST__(node.left)
            self.__printBST__(node.right)


class PartitionPN:

    # We will use a BST to represent our partition of positive numbers from 0(included) to m(excluded)
    # each node of the BST will represent a split in the partition.
    # for example if we have a partition composed of one continuous
    # suite of positive numbers from
    # [0 , 100[ will have two nodes : the root will be 100 and the left node will be 0.
    # to know the size of an interval , the left number ( here zero ) is represented by the node
    # to the left or our own node if the node to the left is null . and the right number is the actual node.
    def __init__(self, m):

        self.BT = BinaryTree(m,m)
        self.smallest = 0
        self.biggest = m

    def getSmallest(self):
        return self.smallest

    def getBiggest(self):
        return self.biggest

    # return interval [Xi-1, Xi[ containing x
    # while searching it will always keep in mind the latest bigger than x visited
    # so that when arriving in front of a smaller while having a bigger in memory it will
    # return the partition from the smaller to the one in memory
    # METHODE RECHERCHER
    def rechercher(self, x):
        return self.__rechercher__(self.BT.root, x)

    # helper method RECHERCHER
    def __rechercher__(self, node, x, mss=None, msb=None):
        if mss is None: mss = self.getSmallest()
        if msb is None: msb = self.getBiggest()
        if node is None:
            print("for " + str(x) + " : [ " + str(mss) + " , " + str(msb) + " [ ")
            return mss, msb
        elif x < node.key:
            msb = node.key
            return self.__rechercher__(node.left, x, mss, msb)
        elif x >= node.value:
            mss = node.key
            return self.__rechercher__(node.right, x, mss, msb)

    # this method will search for a certain interval and delete the node between this interval and the one bigger
    # than him. it will use the same pattern as search and then delete the correct node using the delete method from
    # BST class
    def fusion(self, x):
        if x == self.biggest:
            return
        self.BT.delete(self.rechercher(x)[0])
        return

    # the tranche function will split the partition into two smaller ones the one to the left excluding x and the one
    # to right including it. The way it will do so is simply like a normal put(x) . it will search to the right place
    # in the tree and place the node there. It is important to keep in mind that the binary search tree serves as a
    # representation of the splitting positions in our partition. and that the smallest element and biggest wich are
    # set up at the creation of the partition are kept separatey in "biggest" and "smallest" . by doing so we insure
    # that the tree will be more balanced
    def tranche(self, x):
        self.BT.put(x, x)


class MainTest:

    @staticmethod
    def testBT():
        bintree = BinaryTree(6,6)
        bintree.put(5, 5)
        bintree.put(3, 3)
        bintree.put(7, 7)
        bintree.printBST()

    @staticmethod
    def testpartition(m):
        partition = PartitionPN(m)
        partition.tranche(100)
        partition.fusion(101)
        partition.BT.printBST()
        partition.fusion(100)
        partition.BT.printBST()



#MainTest.testBT()
MainTest.testpartition(math.inf)
