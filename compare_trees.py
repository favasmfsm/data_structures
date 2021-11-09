import Binary_Search_Tree

class TreeCompare:
    def treecomparator(self,node1,node2):

        if(node1 is None or node2 is None):
            return node1==node2

        if(node1.data!=node2.data):
            return False

        return self.treecomparator(node1.left_node,node2.left_node) and self.treecomparator(node1.right_node,node2.right_node)

if __name__=="__main__":
    tree1=Binary_Search_Tree.BinarySearchTree()
    tree1.insert(15)
    tree1.insert(11)
    tree1.insert(13)
    tree1.insert(18)
    tree1.insert(19)
    tree1.insert(1)
    tree1.insert(16)
    tree1.insert(12)

    # tree1.traverse()

    tree2 = Binary_Search_Tree.BinarySearchTree()
    tree2.insert(15)
    tree2.insert(11)
    tree2.insert(13)
    tree2.insert(18)
    tree2.insert(19)
    tree2.insert(14)
    tree2.insert(16)
    tree2.insert(12)

    comparator=TreeCompare()
    print(comparator.treecomparator(tree1.root,tree2.root))