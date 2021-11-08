
#Stack

class Stack:

    def __init__(self):
        
        self.stack=[]

    #inserting an element to the stack
    def push(self,data):

        self.stack.append(data)
    
    #removing an element from the end:
    def pop(self):

        if(len(self.stack)<1):
            return -1
        else:
            data=self.stack[-1]
            del self.stack[-1]
            return data

    #returning the last item
    def peep(self):

        return self.stack[-1]


    def is_empty(self):

        return self.stack==[]


    def stack_size(self):
        
        return len(self.stack)


    