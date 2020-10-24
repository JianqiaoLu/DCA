class DCA(object):
    def __init__(self,list1):
        self.list2 = list1
    def recursive(self, list1, start_position, final_position):

        if start_position >= final_position:
            return
        else: 
            middle_term = list1[start_position]
            list1[start_position] = list1[final_position]
            list1[final_position] = middle_term
            self.recursive(list1, start_position +1, final_position -1)
    def Max2(self,list1,start_position,final_position):
        if start_position > final_position - 2:
            if list1[start_position] > list1[final_position]:
                max1 = start_position
                max2 = final_position
            else:
                max1 = final_position
                max2=  start_position
            return max1,max2
        else:
            mid = (start_position+final_position)/2
            max1l,max2l = self.Max2(list1, start_position, mid )
            max1r,max2r = self.Max2(list1, mid+1, final_position)
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
    def findsubsequence(self,list1,list2):

        
        if len(list1) ==0 or len(list2) == 0:
            return {'':0}
        elif  list1[-1] == list2[-1]:
            subanswer  =  self.findsubsequence(list1[:-1],list2[:-1]) 
            answer = {}

            for key, value in subanswer.items():
                answer[key+list1[-1]] = value + 1 
             
        else:
           answer1 = self.findsubsequence(list1[:-1], list2)
           answer2 = self.findsubsequence(list1,list2[:-1])
           
           if len(list(answer1.keys())[0]) > len(list(answer2.keys())[0]):
               answer = answer1
           elif len(list(answer1.keys())[0]) < len(list(answer2.keys())[0]):
               answer = answer2
           else:
               answer = dict(list(answer1.items())+list(answer2.items()))
        return answer
            

if __name__ == "__main__":
    dca = DCA([1,2,3,4])
    list2 = [1,2,3,4]
    dca.recursive(list2,0,3)
    print(list2)
    print(dca.findsubsequence('educational','advantage'))