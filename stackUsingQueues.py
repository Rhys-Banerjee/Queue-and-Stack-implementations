from queue import Queue

from stack import Stack

class StackUsingQueues():
    '''
    A class to implement Queues using Stacks
    '''
    def __init__(self):
        self.items = Queue()
        self.l2 = Queue()
    
    def retrieve(self):
        return self.items.retrieve()
    
    def peek(self):
        ret = []
        while self.items.isEmpty() == False:
            curVal = self.items.peek()
            self.l2.push(curVal)
            self.items.pop()
            if self.items.isEmpty():
                ret.append(curVal)
                break
        while self.l2.isEmpty() == False:
            self.items.push(self.l2.peek())
            self.l2.pop()
        return ret[0]
    
    def push(self, x):
        return self.items.push(x)


    def popS(self):
        while self.items.isEmpty() == False:
            curVal = self.items.peek()
            self.items.pop()
            if self.items.isEmpty():
                break
            self.l2.push(curVal)

        while self.l2.isEmpty() == False:
            self.items.push(self.l2.peek())
            self.l2.pop()
        return self.items

if __name__=="__main__":
    test = StackUsingQueues()
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    print(test.retrieve())
    test.popS()
    print(test.retrieve())
    print(test.peek())
    