import numpy as np
class Listnode(object):
    def __init__(self, nodevalue, pre = None, next = None):
        self.value = nodevalue
        self.pre = pre
        self.next = next
class Ownlist(object):
    def __init__(self):
        header = Listnode(None)
        trailer = Listnode(None)
        header.next = trailer
        trailer.pre = header
        self.header = header
        self.trailer = trailer
    def find_value(self, nodevalue):
        p = self.header
        while(p != None):
            if p.value == nodevalue:
                return p
            p  = p.next
        return None
    def insertbefore(self, listnode, nodevalue):
        if listnode != None:
            node = Listnode(nodevalue, listnode.pre, listnode)
            listnode.pre.next = node
            listnode.pre = listnode
        else:
            node = Listnode(nodevalue, self.header, self.trailer)
            self.header.next = node
            self.trailer.pre = node
    def delete(self, listnode):
        value = listnode.value
        listnode.pre.next = listnode.next
        listnode.next.pre = listnode.pre

def copynodes(listnode, n_numbers):
    ownlist = Ownlist()
    for i in range(n_numbers):
       if listnode.value != None and i == 0:
        ownlist.insertbefore(None, listnode.value)
        listnode = listnode.next
       elif listnode.value != None:
        ownlist.insertbefore(listnode.pre, listnode.value) 
       else:
           return ownlist
if __name__ == "__main__":
    ownlist = Ownlist()
    ownlist.insertbefore(None,1)
    ownlist.insertbefore(ownlist.header.next,2)
    ownlist.delete(ownlist.header.next)
    print(ownlist.header.next.value)