
heap_capacity=10

class Heap:

    def __init__(self):

        self.heap_size=0
        self.heap=[0]*heap_capacity

    def insert(self,data):

        if self.heap_size==heap_capacity:
            return
        

        self.heap[self.heap_size]=data
        self.heap_size+=1

        #now we need to check for the heap properties

        self.heap_prop_up(self.heap_size-1)

    def heap_prop_up(self,heap_size):

        i=heap_size
        p_i=(heap_size-1)//2  #parent index

        if(i>0 and self.heap[i]>self.heap[p_i]):
            self.heap[i],self.heap[p_i]=self.heap[p_i],self.heap[i]
            self.heap_prop_up(p_i)

        return 

    def get_max(self):
        return self.heap[0]

    def poll(self):

        max_item=self.get_max()

        self.heap[0],self.heap[self.heap_size-1]=self.heap[self.heap_size-1],self.heap[0]
        self.heap_size-=1
        self.heap_prop_down(0)

        return max_item

#checking whether heap properties are violated from starting
    def heap_prop_down(self,i):

        l=2*i+1
        r=2*i+2

        #in a max heap the first item is the largest
        largest_index=i


        #checking whether left is larger than parent
        if l<self.heap_size and self.heap[l]>self.heap[i]:
            largest_index=l

        #checking whether right is larger than largest index one
        if r<self.heap_size and self.heap[r]>self.heap[largest_index]:
            largest_index=r

        if i!=largest_index:  #so left or right is larger than parent and we need to heapify
            self.heap[i],self.heap[largest_index]=self.heap[largest_index],self.heap[i]
            self.heap_prop_down(largest_index)
        
    def heap_sort(self):

        for _ in range(self.heap_size):
            max_item=self.poll()
            print(max_item)

        
if __name__ == '__main__':

    heap = Heap()
    heap.insert(13)
    heap.insert(-2)
    heap.insert(0)
    heap.insert(8)
    heap.insert(1)
    heap.insert(-5)
    heap.insert(100)
    heap.insert(-100)
    heap.insert(10)
    heap.insert(20)

    heap.heap_sort()

    




