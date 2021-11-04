
class Node:

    def __init__(self,data):
        self.data=data
        self.next_node=None
        self.prev_node=None

class DoublyLinkedList:

    def __init__(self,data):

        self.head=None
        self.tail=None
        self.no_of_nodes=0
    
    
    #inserting data at the end
    def insert_end(self,data):

        self.no_of_nodes+=1
        new_node=Node(data)

        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prev_node=self.tail
            self.tail.next_node=new_node
            self.tail=new_node
    
    
    #inserting data at the starting
    def insert_start(self,data):

        self.no_of_nodes+=1
        new_node=Node(data)
        
        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:

            new_node.next_node=self.head
            self.head.prev_node=new_node
            self.head=new_node


    #print from start to end
    def traverse_forward_print(self):

        current_node=self.head

        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next_node


    #print from tail to start
    def traverse_backward_print(self):

        current_node=self.tail

        while current_node is not None:

            print(current_node.data)
            current_node=current_node.prev_node

    