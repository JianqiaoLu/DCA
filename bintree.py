import math
from Stack import Stack
class binnode(object):
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.lchild = None
        self.rchild = None
        self.height = 0
    def size(self):
        tree_size = 1
        if self.lchild :
            tree_size = tree_size +  self.lchild.size()
        if self.rchild :
            tree_size = tree_size  + self.rchild.size()
        return tree_size
        # interesting
    def insertaslchild(self, binnode_e):

        self.lchild = binnode_e
        binnode_e.parent = self
        self.updateheightabove()
    def insertasrchild(self, binnode_e):

        self.rchild = binnode_e
        binnode_e.parent = self
        self.updateheightabove()

    def updateheight(self):
        self.height = 1 + max(getheight(self.lchild), getheight(self.rchild))

    def updateheightabove(self):
        self.updateheight()
        if self.parent:
            self.parent.updateheight()
    def traverse(self):
        print(self.value)
        if self.lchild:
            self.lchild.traverse()
        if self.rchild:
            self.rchild.traverse()
    def traverse_version1(self):
        node_stack = [self]
        while len(node_stack)!= 0:
           node =node_stack.pop(-1)
           print(node.value)
           if node.rchild:
               node_stack.append(node.rchild)
           if node.lchild:
               node_stack.append(node.lchild)
        print('finished')
    def travalalongleft(self,node_stack):
        
        node = self
        while(node):
            print(node.value)
            node_stack.append(node.rchild)
            node =node.lchild
        return node_stack

    def traverse_version2(self):
        node_stack = [self]
        while (len(node_stack) != 0):
            node = node_stack.pop(0)
            node_stack =  node.travalalongleft(node_stack)
    def middletraverse(self):
        binnode = self
        if not binnode:
           return 
        if binnode.lchild:
         binnode.lchild.middletraverse()
        print(binnode.value)
        if binnode.rchild:
         binnode.rchild.middletraverse()
    def middletraverse_version2(self):
        binnode_stack = Stack([])
        binnode = self
        while True:
         if binnode:
          binnode_stack = binnode.importgoalonglchild(binnode_stack)
         if len(binnode_stack.list) == 0:
             break
         binnode = binnode_stack.pop()
         print(binnode.value)
         binnode = binnode.rchild
        
        
    def importgoalonglchild(self, binnode_stack):
        binnode = self
        while(binnode):
            binnode_stack.push(binnode)
            binnode = binnode.lchild
        return binnode_stack
        

        


        
        

                   

def getheight(node):
    if node:
        return node.height
    else :
        return -1

if __name__ == "__main__":
    a = binnode(1)
    b = binnode(2)
    c = binnode(3)
    d = binnode(4)
    c.insertaslchild(b)
    b.insertaslchild(a)
    c.insertasrchild(d)
    c.traverse_version1()
    c.middletraverse()
    c.middletraverse_version2()
    #print(c.height)