import LinkedList

my_list=LinkedList.Linked_List()

for i in range(49):
    my_list.insert_start(i)
middle = my_list.no_of_nodes//2
# my_list.traverse_and_print()
def find_middle(middle,mylist):
    
    # print(middle)
    current_node=my_list.head
    counter=0
    while counter<middle:
        current_node=current_node.next_node
        counter+=1
    print(current_node.data)

print(my_list.get_middle_node().data)
find_middle(middle,my_list)
