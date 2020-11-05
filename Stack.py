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
    stack = Stack([])
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
# 栈混洗还挺有意思的奥， 栈混洗中，原位置的三个顺序元素不能出现 j+1, i, j for j >i, 这里用>表示距离栈顶的位置，当然这个算法需要枚举任意三个元素的相对位置
# 所以我们还是采用栈模拟的方式来印证
def judgestack(orginalstack, mixedstack):

    stack_b = Stack([])
    stack_a = Stack(orginalstack)
    stack_c = Stack(mixedstack)
    while len(stack_a.list) > 0:
      if stack_c.top() in stack_b.list: 
        if stack_b.top() == stack_c.top():
            stack_b.pop()
            stack_c.pop()
        else:
            return False
      stack_b.push(stack_a.pop())
    if len(stack_b.list) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
   jinzhizhuanhuan(2,10).print_all()
   print(columncomp('[111]'))
   print(judgestack('321', '213'))

    