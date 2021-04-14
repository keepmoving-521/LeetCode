"""
三合一。描述如何只用一个数组来实现三个栈。

你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。
stackNum表示栈下标，value表示压入的值。

构造函数会传入一个stackSize参数，代表每个栈的大小。

示例1:

 输入：
["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
[[1], [0, 1], [0, 2], [0], [0], [0], [0]]
 输出：
[null, null, null, 1, -1, -1, true]
说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
示例2:

 输入：
["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
[[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
 输出：
[null, null, null, null, 2, 1, -1, -1]
"""


class TripeInOne(object):
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.tripe_stack = [[] for _ in range(3)]

    def push(self, stack_num, value):
        if len(self.tripe_stack[stack_num]) < self.stack_size:
            self.tripe_stack[stack_num].append(value)
        else:
            return -1

    def pop(self, stack_num):
        if len(self.tripe_stack[stack_num]) != 0:
            return self.tripe_stack[stack_num].pop()
        else:
            return -1

    def peek(self, stack_num):
        if len(self.tripe_stack[stack_num]) != 0:
            return self.tripe_stack[stack_num][-1]
        else:
            return -1

    def is_empty(self, stack_num):
        return self.tripe_stack[stack_num] == []


if __name__ == '__main__':
    obj = TripeInOne(10)
    print(obj.is_empty(0))
    obj.push(0, 3)
    obj.push(0, 2)
    obj.push(0, 1)
    print(obj.is_empty(0))
    print(obj.peek(1))
    print(obj.peek(0))
    print(obj.pop(0))
    print(obj.peek(0))
