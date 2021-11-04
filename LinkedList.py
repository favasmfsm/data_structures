
class Node:

    def __init__(self,data):
        self.data=data
        self.next_node=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.no_of_nodes=0

    #inserting the data at the start

    def insert_start(self,data):
        
        self.no_of_nodes+=1
        new_node=Node(data)

        if not self.head:
            self.head=new_node

        else:
            new_node.next_node=self.head
            self.head=new_node

    #inserting to the end of the list

    def insert_end(self,data):

        self.no_of_nodes+=1
        new_node=Node(data)

        current_node=self.head

        while current_node.next_node is not None:
            current_node=current_node.next_node

        current_node.next_node=new_node

    def size_of_the_list(self):

        return self.no_of_nodes

    def traverse_and_print(self):

        current_node=self.head

        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next_node

    def remove(self,data):

        if self.head is None:             #list is empty
            return

        current_node=self.head

        while current_node is not None and current_node.data !=data:
            previous_node=current_node
            current_node=current_node.next_node

        if current_node is None:
            return

        if previous_node is None:
            self.head=current_node.next_node
        else:
            previous_node.next_node=current_node.next_node



