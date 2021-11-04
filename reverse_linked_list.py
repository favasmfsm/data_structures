import LinkedList

my_list = LinkedList.Linked_List()

for i in range(49):
    my_list.insert_start(i)

# length=my_list.size_of_the_list

current_node=my_list.head
prev_node=None
next_node=None

#here we are changing the direction of the linkedlist
while current_node.next_node is not None:
    next_node=current_node.next_node
    current_node.next_node=prev_node
    prev_node=current_node
    current_node=next_node

my_list.head=prev_node

# verify_the reversal
# my_list.traverse_and_print()                     

