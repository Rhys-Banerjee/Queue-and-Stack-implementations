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
    
    def peek(self):
        #returns top element of queue
        return self.items[0]

    def isEmpty(self):
        '''
        is the queue empty?
        '''
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




if __name__=="__main__":
    pass

