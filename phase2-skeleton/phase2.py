"""
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree
from dlist import DList


# Exercise #1
class BST2(BinarySearchTree):
    
    def find_distance_from_lca(self, lca, target):
        def helper(lca, target, distance):
            if lca is None:
                return -1
            if lca.elem == target.elem:
                return distance

            left_distance = helper(lca.left, target, distance + 1)
            if left_distance != -1:
                return left_distance

            return helper(lca.right, target, distance + 1)

        return helper(lca, target, 0)

    
    def find_dist_k(self, n: int, k: int) -> list:
        list = []
        nodesList = []
        result = []
        root = self._root.elem
        rootNode = self._root
        nodeDistance = 0
        targetDistance = 0
        
        #Find Node
        node = self.search(n)
        
        #If not Found throw error
        if node is None:
            print("Element n not found in Tree")
            return list

        #If distance from element is 0
        if k == 0:
            list.append(n)
            return list
        
        list = self.preorder_list()
        #Obtain Nodes
        for i in list:
            nodesList.append(self.search(i))
            

        #Obtain nodes that are at a distance k from n. 
        for i in range (len(nodesList)):
            rootNode = self._root
            while rootNode:
                if node.elem < rootNode.elem and nodesList[i].elem < rootNode.elem:
                    rootNode = rootNode.left
                elif node.elem > rootNode.elem and nodesList[i].elem > rootNode.elem:
                    rootNode = rootNode.right
                else:
                    break
               
            nodeDistance = self.find_distance_from_lca(rootNode ,node)
            targetDistance = self.find_distance_from_lca(rootNode ,nodesList[i])
            
            if nodeDistance + targetDistance == k:
                result.append(nodesList[i].elem)   
            
        return result  
   

# Exercise #2
def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    
    if input_tree1 is not None and input_tree2 is not None:
        newBST = BinarySearchTree()
    else:
        print ("Lists must not be empty")
        return None
    
    if opc == 'merge':
        #Merge the two lists
        # traverse the first tree and append its elements to the list
        mergeList(input_tree1._root, newBST, input_tree1, input_tree2, input_tree2._root)
        mergeList(input_tree2._root, newBST, input_tree1, input_tree2)
        return newBST
    
    elif opc == "intersection":
        inCommon(input_tree1._root, newBST, input_tree2)
        if (input_tree1.inorder_list() == input_tree2.inorder_list()):
            newBST._root = None
        return newBST
    
    elif opc == "difference":
        difference(input_tree1._root, newBST, input_tree2)
        return newBST
    else:
        print('Please enter a valid value for opc')
        return None
    
#Helper Methods    
def mergeList(node1: BinaryNode, newBST: BinarySearchTree, input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, node2: BinaryNode = None) -> None:
    if node1 is not None:
        if node2 is not None:
            tempNode = input_tree2.search(node1.elem)

            if tempNode is None and newBST.search(node1.elem) is None:
                newBST.insert(node1.elem)

            mergeList(node1.left, newBST, input_tree1, input_tree2, node2)
            mergeList(node1.right, newBST, input_tree1, input_tree2, node2)

        else:
            if newBST.search(node1.elem) is None:
                newBST.insert(node1.elem)

            mergeList(node1.left, newBST, input_tree1, input_tree2)
            mergeList(node1.right, newBST, input_tree1, input_tree2)

def inCommon(node: BinaryNode, newBST: BinarySearchTree, input_tree2: BinarySearchTree) -> None:
    
    if node is not None:
        tempNode = input_tree2.search(node.elem)
        
        if tempNode is not None:
            newBST.insert(node.elem)
        
        inCommon(node.left, newBST, input_tree2)
        inCommon(node.right, newBST, input_tree2)
        
def difference (node: BinaryNode, newBST: BinarySearchTree, input_tree2: BinarySearchTree) -> None:
    
    if node is not None:
        tempNode = input_tree2.search(node.elem)
        
        if tempNode is None:
            newBST.insert(node.elem)
        
        difference(node.left, newBST, input_tree2)
        difference(node.right, newBST, input_tree2)        
        
        

if __name__ == '__main__':
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]
    input_list_01 = [5, 3, 7, 1, 4]
    input_list_02 = [5, 3, 7, 1, 4]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["intersection"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()



