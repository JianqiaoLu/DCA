class DCA(object):
    def __init__(self,list):
        self.list = list
    def recursive(self, list, start_position, final_position):

        if start_position >= final_position:
            return
        else: 
            middle_term = list[start_position]
            list[start_position] = list[final_position]
            list[final_position] = middle_term
            self.recursive(list, start_position +1, final_position -1)
    def Max2(self,list,start_position,final_position):
        if start_position > final_position - 2:
            if list[start_position] > list[final_position]:
                max1 = start_position
                max2 = final_position
            else:
                max1 = final_position
                max2=  start_position
            return max1,max2
        else:
            mid = (start_position+final_position)/2
            max1l,max2l = self.Max2(list, start_position, mid )
            max1r,max2r = self.Max2(list, mid+1, final_position)
            if max1l > max1r:
                max1  =  max1l
                if max2l > max1r:
                    max2 = max2l
                else:
                    max2 = max1r
            else:
                max1  =  max1r
                if max2r > max1l:
                    max2 = max2r
                else:
                    max2 = max1l
            return max1, max2

            

if __name__ == "__main__":
    dca = DCA([1,2,3,4])
    list = [1,2,3,4]
    dca.recursive(list,0,3)
    print(list)