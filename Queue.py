#Queue

class Queue:

    def __init__(self):

        self.queue=[]

    def enqueue(self,data):

        self.queue.append(data)

    def dequeue(self):

        if(self.queue==[]):
            return -1
        else:
            data=self.queue[0]
            del self.queue[0]
            return data

    def is_empty(self):

        return self.queue==[]

    def queue_size(self):

        return len(self.queue)

    