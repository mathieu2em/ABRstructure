import math


class BinaryTree:
    def __init__(self, rootkey, rootvalue=0):
        self.root = BinaryTree.Node(rootkey, rootvalue)

    # class for individual nodes
    class Node:
        def __init__(self, key=None, value=None, N=0, left=None, right=None):
            self.right = right
            self.left = left
            self.value = value
            self.key = key
            self.N = N

    def showExposition(self):

        if self.root is None:
            print(0)
            return
        else:
            return self._showExposition(self.root)

    def _showExposition(self, node):
        if node is None:
            print(0)
            return 0
        else:
            exp = min(self._showExposition(node.left), self._showExposition(node.right))+1
            print("node ",node.value," is exposition ",exp)
            return exp

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

    # return node with smallest key
    def treeMin(self, r):
        x = r
        y = None
        while x is not None:
            y = x
            x = x.left
        return y

    #r return node with biggest key
    def treeMax(self, r):
        x = r
        y = None
        while x is not None:
            y = x
            x = x.right
        return y

    # iterative way of getting a node value
    def getIter(self, node , key):
        while node is not None and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        if node is None:
            return None
        else:
            return node.value

    # tree traversal using postfix method
    def prefixTraversal(self, node):
        if node is not None:
            print(node.value)
            self.prefixTraversal(node.left)
            self.prefixTraversal(node.right)

    def postfixTraversal(self, node):
        if node is not None:
            self.postfixTraversal(node.left)
            self.postfixTraversal(node.right)
            print(node.value)


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
    # [0 , 100[  it will have 1 node : the root will be 100 .
    def __init__(self, m):

        self.BT = BinaryTree(m, m)
        self.smallest = 0
        self.biggest = m

    def getSmallest(self):
        return self.smallest

    def getBiggest(self):
        return self.biggest

    # return interval [Xi-1, Xi[ containing x
    # while searching it will always keep in mind the smallest bigger than x visited
    # so that when arriving in front of a smaller while having a bigger in memory it will
    # take the smaller bigger then x as the msb
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
        elif node.value <= x < msb:
            mss = node.key
            return self.__rechercher__(node.right, x, mss, msb)
        else:
            print("error")
            return

    # this method will search for a certain interval and delete the node between
    # this interval and the one bigger
    # than him. it will use the same pattern as search and then delete the correct
    # node using the delete method from
    # BST class
    def fusion(self, x):
        if x == self.biggest:
            return
        self.BT.delete(self.rechercher(x)[0])
        return

    # the tranche function will split the partition into two smaller ones
    # the one to the left excluding x and the one
    # to right including it. The way it will do so is simply like a normal put(x) .
    # it will search to the right place
    # in the tree and place the node there. It is important to keep in mind that
    # the binary search tree serves as a
    # representation of the splitting positions in our partition. and that
    # the smallest element and biggest which are
    # set up at the creation of the partition are kept separately in "biggest" and "smallest" .
    # by doing so we insure
    # that the tree will be more balanced and will always works
    def tranche(self, x):
        self.BT.put(x, x)


class MainTest:

    @staticmethod
    def testBT():
        bintree = BinaryTree(6, 6)
        bintree.put(5, 5)
        bintree.put(3, 3)
        bintree.put(7, 7)
        bintree.postfixTraversal(bintree.root)
        print("\n")
        bintree.prefixTraversal(bintree.root)
        bintree.showExposition()
    @staticmethod
    def testpartition(m):
        partition = PartitionPN(m)
        partition.rechercher(m)
        partition.rechercher(m - 1)


MainTest.testBT()
# MainTest.testpartition(100)
