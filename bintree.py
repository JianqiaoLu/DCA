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
    def insertaslchild(self, e):
        lchild = binnode(e)
        self.lchild = lchild
        lchild.parent = self
    def insertasrchild(self, e):
        rchild = binnode(e)
        self.rchild = rchild
        rchild.parent = self
    def updateheight(self):
        self.height = 1 + max(getheight(self.lchild), getheight(self.rchild))

    def updateheightabove(self):
        self.updateheight()
        if self.parent:
            self.parent.updateheight()

def getheight(node):
    if node:
        return node.height
    else :
        return -1