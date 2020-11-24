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
        if listnode.pre != None:
         listnode.pre.next = listnode.next
        if listnode.next != None:
         listnode.next.pre = listnode.pre
    def duplicate(self, listnode):

        pre = 0
        while listnode.next != None:
           find_same_node = self.findnode(listnode.value, pre, listnode)
           if find_same_node!= None:
               self.delete(find_same_node)
               pre =  pre - 1 
           else:
               pre = pre + 1
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

        while (length > 0 ):
            min_node = self.selectmin(first, length)
            self.insertbefore(last,min_node.value)
            self.delete(min_node)     
            length = length - 1   
        # selectsort 会保证没有排序的元素至少不会大于已经排序了的元素， 类似于bubblersort, 但是select的效率远远高于bubblersort, 每次都要比较和交换
        #每次都是相邻元素间的移动排序
    def findnodeforinsert(self, nodevalue,listnode):
        p = listnode
        while p.pre.value != None:
            if p.value >= nodevalue:
                p = p.pre
            else:
                return p.next
        return None
    def insert_sort(self, listnode):

        cur = listnode
        while cur.next != None:   
            nodevalue = cur.value
            insert_location = self.findnodeforinsert(nodevalue, cur)
            if insert_location != None:
                self.insertbefore(insert_location, nodevalue)
                cur = cur.next
                if cur != None:
                 self.delete(cur)
            else:
                cur = cur.next
    
        # insert_sort 是输入敏感的，复杂度和输入序列的有序性关系很大


def quick_sort(original_list,start_point, end_point):
    if (start_point + 1  < end_point):

        i  = partition(original_list, start_point, end_point)
        result1 = quick_sort(original_list, start_point, i )
        resutl2 = quick_sort(original_list, i +1, end_point)
    # istead of while, we shall use if since only one loop is sufficient 
def partition(original_list,start_point, end_point):
    i, p = start_point, start_point
    for j in range(p, end_point):
        if original_list[j] < original_list[end_point -1]:
            value = original_list[j]
            original_list[j] = original_list[i]
            original_list[i] = value
            i = i + 1 
    value = original_list[j]

    original_list[j] = original_list[i]
    original_list[i] = value
    return i 




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
    original_list = [15, 9,10,5,7 ,11,13]
    print(quick_sort(original_list, 0, len(original_list)))
    print(original_list)
    '''
    ownlist = Ownlist()
    ownlist1 = Ownlist()
    ownlist.insertbefore(None,1)
    ownlist.insertbefore(ownlist.header.next,2)
    ownlist.insertbefore(ownlist.header.next,2)
    ownlist.insertbefore(ownlist.header.next,3)
    ownlist.printallnodes(ownlist.header.next)
    ownlist1.insertbefore(None,1)
    ownlist1.insertbefore(ownlist1.header.next,2)

    ownlist1.insertbefore(ownlist1.header.next,3)
    ownlist.duplicate(ownlist.header.next) 
    print('fdasfd')
    ownlist.printallnodes(ownlist.header.next)
    ownlist.select_sort(ownlist.header.next)
    print("aoligei")
    ownlist.printallnodes(ownlist.header.next)
    print("aoligei2")
    ownlist1.printallnodes(ownlist1.header.next)
    ownlist1.insert_sort(ownlist1.header.next)
    ownlist1.printallnodes(ownlist1.header.next)
    '''
