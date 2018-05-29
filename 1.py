from copy import copy


class Node:
    def __init__(self, data, number, root):
        self.number = number
        self.data = data
        self.left = None
        self.right = None
        if number == 0:
            self.root = self
        else:
            self.root = root

    def insertion(self, new_node):

        if self.left is None:
            self.left = new_node
        else:
            self.right = new_node

    def insertNode(self, new_node, numroot):

            self.root.find(numroot).insertion(new_node)

    def find(self, x):
        if self.number is x:
            return self
        if self.left is not None:
            n = self.left.find(x)
            if n is not None:
                return n
        if self.right is not None:
            w = self.right.find(x)
            if w is not None:
                return w
        return


def isBSTmy(node):
    if node.right is None and node.left is None:
        return True
    elif node.right is not None and node.left is not None:
        if int(node.data) < int(node.left.data):
            return False
        elif int(node.data) > int(node.right.data):
            return False
        return isBSTmy(node.right)and isBSTmy(node.left)
    elif node.right is not None:
        return isBSTmy(node.right)
    else:
        return isBSTmy(node.left)


def reading_input():
    count = int(raw_input())
    mylist = map(int, raw_input().split())
    return count, mylist
    pass


count, mylist=reading_input()
root = Node(mylist[0],0,0)
refrence = copy(root)
for x in xrange(int(count)-1):
    infu=map(int,raw_input().split())
    newNode= Node(mylist[x+1], infu[1],root)
    refrence.insertNode(newNode, infu[0])
if isBSTmy(root) is True:
    print "YES"
else:
    print "NO"
