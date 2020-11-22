from bintree import binnode

class Binst(object):
    def search(self, nodevalue):
      current_node = self
      previous_node = self
      while(current_node): 
        if nodevalue == current_node.value:
           return current_node
        elif nodevalue< current_node.value:
            previous_node = current_node
            current_node = current_node.lchild
        else:
            previous_node = current_node
            current_node = current_node.rchild
      if current_node:
          return (False, previous_node)
      else:
          return (True, current_node)
          
    def insert(self, value):
        binst = Binst(value)
        location = self.search(binst.value)
        if location(0):
            return "there already exists one same value"
        else:
            insert_location =  location(1)
            if insert_location.value< binst.value:
                insert_location.rchild = binst
                binst.parent = insert_location
            else:
                insert_location.lchild = binst
                binst.parent = insert_location

    def change_parent(self, old_binnode, new_binnode ):
        if old_binnode.parent
         if new_binnode:
           new_binnode.parent = old_binnode.parent
         if old_binnode.parent.value > old_binnode.value:
             old_binnode.parent.lchild = new_binnode
         else:
             old_binnode.parent.rchild = new_binnode
        else:
         pass
    
    def find_leftmostchild(self, binnode):
        current_node  = binnode
        while(current_node):
            current_node = current_node.lchild

    def remove(self, binnode):
        location = binnode.value
        result  =  self.search(binnode)
        if  result(0):
            deleted_node = result(1)
            if  not (deleted_node.rchild):
                self.change_parent(deleted_node, deleted_node.lchild)
            elif not (deleted_node.lchild):
                self.change_parent(deleted_node, deleted_node.rchild)
            else:
                new_node = self.find_leftmostchild(deleted_node.rchild).value
                deleted_node.value =new_node.value
                self.change_parent(new_node,new_node.rchild)
        
                
            
                
            return 'finished'
        else:
            new_node = self.find_leftmostchild(deleted_node.rchild)
            
            return 'there exist no node to be deleted'