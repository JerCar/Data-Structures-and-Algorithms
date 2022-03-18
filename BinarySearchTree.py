# Binary Search Tree


class BSTNode:
    """ Not so lightweight Node Class for a Binary Search Tree """

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def _insertval(self, val):
        """ Insert val into the correct position in the tree """
        if not self.val:
            self.val = val

        if self.val == val:  # duplicate value
            return

        if val < self.val:
            if self.left:
                self.left._insertval(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right._insertval(val)
            return
        self.right = BSTNode(val)

    def _delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left._delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right = self.right._delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        minnode = self.right
        while minnode.left:
            minnode = minnode.left
        self.val = minnode.val
        self.right = self.right._delete(minnode.val)
        return self

    def _inorderprint(self):
        if self.left:
            self.left._inorderprint()

        #if not self.val == None:
        print(self.val)

        if self.right:
            self.right._inorderprint()


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,data):
        self.size += 1
        if self.root:
            return self.root._insertval(data)
        else:
            self.root = BSTNode(data)
            return True

    def delete(self, data):
        return self.root._delete(data)

    def inorderprint(self):
        print("The size of the tree is ", sizeoftree(x.root))
        if self.root is not None:
            return self.root._inorderprint()
        else:
            return

    def find(self, val):
        if self.root is not None:
            return self.root._inordersearch()
        else:
            return

def sizeoftree(node):
    if node is None:
        return 0
    else:
        return (sizeoftree(node.left) + 1 + sizeoftree(node.right))


if __name__ == "__main__":
    mylist = [95,-32,4,57,68,988,91,3]
    print("Original list to input")
    for j in mylist:
        print(j)
    x = Tree()
    for i in mylist:
        x.insert(i)
    x.inorderprint()

    print("Deleting element 988, -32, 91 and 68")
    x.delete(988)
    x.delete(-32)
    x.delete(68)
    x.delete(91)
    x.inorderprint()

 
