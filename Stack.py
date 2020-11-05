import numpy as np

digit=[
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]
colunm = { '(':')', '[':']', '{':'}'}
class Stack(object):
    def __init__(self, list):
        self.list = list
    def push(self, value):
        self.list.append(value)
    def pop(self):
        value = self.list[-1]
        self.list = self.list[:-1]
        return value
        
    def top(self):
        return self.list[-1]
    def print_all(self):
        while len(self.list)!= 0:
            print(self.pop())
def jinzhizhuanhuan(jinzhiweishu, originalvalue):
    cur_value = originalvalue
    stack = Stack([])

    while cur_value != 0:
         multipers = int(cur_value/jinzhiweishu)
         transformvalue = cur_value - multipers*jinzhiweishu
         stack.push(digit[transformvalue])
         cur_value = multipers
    return stack
def columncomp(string):
    stack = Stack([0])
    for item in string:
        if item == '(' or "[" or '{' :
            stack.push(item)
        elif item == colunm['('] or colunm['{'] or colunm['[']:
            if len(stack.list) != 0:
                if colunm[stack.pop] == item:
                    continue
                else:
                    return False
            else:
                return False
        else:
            continue
    return True
# 栈可以用于实时匹配过程，这一性质是减治和分治都不可做到的

if __name__ == "__main__":
   jinzhizhuanhuan(2,10).print_all()
   print(columncomp('[111]'))
    