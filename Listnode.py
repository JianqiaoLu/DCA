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
    def findnode(self, nodevalue, nprevious, listnode):
        for i in range(nprevious):
            listnode = listnode.pre
            if listnode.pre != None:
                if listnode.value == nodevalue:
                    return listnode
        return None
    def insertbefore(self, listnode, nodevalue):
        if listnode != None:

            node = Listnode(nodevalue, listnode.pre, listnode)
            listnode.pre.next = node
            listnode.pre =  node
        else:
            node = Listnode(nodevalue, self.header, self.trailer)
            self.header.next = node
            self.trailer.pre = node
    def delete(self, listnode):
        value = listnode.value
        listnode.pre.next = listnode.next
        listnode.next.pre = listnode.pre
    def duplicate(self, listnode):
        r = 0
        while listnode.next != None:
           find_same_node = self.findnode(listnode.value, r, listnode)
           if find_same_node!= None:
               self.delete(find_same_node)
           else:
               r = r + 1
               listnode = listnode.next
        return 
    def printallnodes(self,listnode):
        while listnode.next != None:
            print(listnode.value)
            listnode = listnode.next
    def selectmin(self, listnode, n_succs):
        min  =  listnode.next
        listnode = listnode.next
        i = 1
        while(i < n_succs):
            listnode = listnode.next
            if listnode.value <= min.value:
                min = listnode
                i = i +1 
            else:
                i =i + 1
        return min
    def select_sort(self, listnode):
        first = listnode.pre
        last  = listnode
        length= 1
        while(last.next!= None):
            last = last.next
            length = length + 1
        length = length -1
        import pdb
        pdb.set_trace()
        while (length > 0 ):
            max_node = self.selectmin(first, length)
            self.insertbefore(last,max_node.value)
            self.delete(max_node)     
            length = length - 1



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
    ownlist.insertbefore(ownlist.header.next,2)
    ownlist.insertbefore(ownlist.header.next,3)
    ownlist.printallnodes(ownlist.header.next)

    ownlist.duplicate(ownlist.header.next)
    print('fdasfd')
    ownlist.printallnodes(ownlist.header.next)
    ownlist.select_sort(ownlist.header.next)
    print("aoligei")
    ownlist.printallnodes(ownlist.header.next)