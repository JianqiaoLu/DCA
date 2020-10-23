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

if __name__ == "__main__":
    dca = DCA([1,2,3,4])
    list = [1,2,3,4]
    dca.recursive(list,0,3)
    print(list)