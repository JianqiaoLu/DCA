from bintree import binnode
def zig(node_1,node_2):
    node_2.parent = node_1.parent
    node_2.rchild.parent = node_1
    node_2.rchild  = node_1
    node_1.parent = node_2
    node_1.lchild = node_2.rchild
def zag(node_1, node_2):
    node_2.parent = node_1.parent
    node_2.lchild.parent = node_1
    node_2.lchild  = node_1
    node_1.parent = node_2
    node_1.rchild = node_2.lchild  
#好像没必要写zagzig 或者zigzag这样子吧。。。

class Splaytree(binnode):

    def splay_operation(self):
        current_node = self
        while(current_node.parent and  current_node.parent.parent):
            parent = current_node.parent 
            grad_parent = current_node.parent.parent
            if current_node == current_node.parent.lchild:
                if current_node.parent == current_node.parent.lchild:
                        zig(grad_parent, parent)
                        zig(parent, current_node)
                else:
                        zig(parent,current_node)
                        zag(grad_parent,parent)
            else:
                if current_node.parent == current_node.parent.rchild:
                        zag(grad_parent, parent)
                        zag(parent,current_node)
                else:
                        zag(parent,current_node)
                        zig(grad_parent,parent)
            grad_parent.updateheight()
            parent.updateheight()
            current_node.updateheight()
        if current_node.parent:
            if current_node == current_node.parent.lchild:
                zig(current_node.parent,current_node)
            else:
                zag(current_node.parent,current_node)
        current_node.parent = null
        return current_node
    def splay_search(self, value):
        result  = self.search(value)
        return [result[0],self.splay_operation(result[1])]
    def splay_insert(self, value):
        result  = self.splay_search(value)
        node = Splaytree(value)
        if result[0]:
            return 'already exist'
        else:
            if value < result[1].value:
               node.rchild = result[1]
               node.lchild = result[1].lchild
               result[1].parent = node
               result[1].lchild.parent = node
            else:
               node.lchild = result[1]
               node.rchild = result[1].rchild
               result[1].parent = node
               result[1].rchild.parent = node
        return node
    def findleftchild(self, node):
        while node.lchild:
            node = node.lchild
    def splay_delete(self,value):
        result  = self.splay_search(value)
        node = Splaytree(value)
        if not result[0]:
            return 'no result found'
        else:
            right_most_leftchild = self.findleftchild(result[1].rchild)
            right_most_leftchild.parent  = null
            right_most_leftchild.lchild  = result[1].lchild
            right_most_leftchild.rchild  = result[1].rchild
            result[1].rchild.parent  = right_most_leftchild
            result[1].lchild.parent  = right_most_leftchild

    