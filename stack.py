class Stack():
    '''
    A class to implement a stack using arrays.
    '''
    def __init__(self):
        self.items = []

    def retrieve(self):
        return self.items

    def isEmpty(self):
        #is this stack empty
        return self.items == []
    
    def peek(self):
        return self.items[-1]

    def push(self, x):
        #push x to the end of items
        self.items.append(x)
    
    def pop(self):
        #removes last item from array
        self.items.pop()
    
    def size(self):
        # return size of stack
        return len(self.items)



if __name__=="__main__":
    test2 = Stack()
    test2.push(1)
    test2.push(2)
    test2.push(3)
    print(test2.retrieve())
    test2.pop()
    print(test2.retrieve())
    print(test2.peek())
