from stack import Stack

class Queue():
    '''
    A class to implement a queue using arrays.
    '''
    def __init__(self):
        self.items = []

    def retrieve(self):
        #returns the queue as is
        return self.items

    def isEmpty(self):
        #is the queue empty?
        return self.items == []
    
    def push(self,x):
        #push an element to end of queue
        return self.items.append(x)
    
    def pop(self):
        # pop element at beginning of queue
        self.items = self.items[1:]
    
    def size(self):
        # returns length of queue
        return len(self.items)


class QueueUsingStack():
    '''
    Implement a Queue using the Stack class.
    '''
    def __init__(self):
        self.l1 = Stack()
        self.l2 = Stack()
    
    def empty(self):
        return self.l1.isEmpty()

    def retrieve(self):
        return self.l1.retrieve()

    def pushQ(self, x):
        self.l1.push(x)
    
    def popQ(self):
        while self.l1.isEmpty() == False:
            self.l2.push(self.l1.peek())
            self.l1.pop()
        self.l2.pop()

        while self.l2.isEmpty() == False:
            self.l1.push(self.l2.peek())
            self.l2.pop()
        return self.l1
    
    def peekQ(self):
        while self.l1.isEmpty() == False:
            self.l2.push(self.l1.peek())
            self.l1.pop()
        # get return value while we have it.
        ret = self.l2.peek()
        # restore the queue to what it was.
        while self.l2.isEmpty() == False:
            self.l1.push(self.l2.peek())
            self.l2.pop()
        return ret

if __name__=="__main__":
    hello = QueueUsingStack()
    hello.pushQ(1)
    hello.pushQ(2)
    hello.pushQ(3)
    print(hello.retrieve())
    hello.popQ()
    print(hello.retrieve())
    print(hello.peekQ())
    print(hello.retrieve())


