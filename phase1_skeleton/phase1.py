from slistH import SList
from slistH import SNode

import sys

class SList2(SList):

    
    def delLargestSeq(self): 
        index = 0
        finalIndex = 0
        count = 0
        tempNode = self._head
        flag = False
        max = 0
        once = True
        
        if (self._size == 1):
            self.removeFirst()
            
        elif self._size != 0:
            for i in range (self._size):
                
                if tempNode.elem == tempNode.next.elem:
                    once = False
                    if flag == False:
                        index = i
                        count = 2
                        flag = True
                    else :
                        flag = True
                        count += 1        
                        
                else:
                    if count >= max and once == False:
                        max = count
                        finalIndex = index
                    flag = False
                    count = 0
                    
                if i == self._size - 1:
                    if count >= max:
                        
                        max = count - 1
                        finalIndex = index
                    flag = False
                    count = 0
                    
                if once == True:
                    finalIndex = self._size -1
                    max = 1
                    

                if i != (self._size - 2):    
                    tempNode = tempNode.next        
                            
            if max != 0:
                for i in range (finalIndex , (finalIndex + max)):
                    self.removeAt(finalIndex)
     


    def fix_loop(self):
        flag = False
        
        tempNode = self._head
        secondNode = self._head


        while secondNode and secondNode.next :
            
            tempNode = tempNode.next
            secondNode = secondNode.next.next

            if tempNode == secondNode:
                flag = True
                
                break

        if not flag:
            return False


        loopSize = 1
        secondNode = secondNode.next
        
        while tempNode != secondNode:
            secondNode = secondNode.next
            loopSize += 1

 
        tempNode = self._head
        secondNode = self._head


        for i in range(loopSize):
            secondNode = secondNode.next

        prevSecondNode = None
        
        while tempNode != secondNode:
            tempNode = tempNode.next
            prevSecondNode = secondNode
            secondNode = secondNode.next


        if prevSecondNode == None:  
            tempNode = self._head
            
            for i in range(loopSize - 1):
                tempNode = tempNode.next
                
                
            tempNode.next = None
            
        else:
            prevSecondNode.next = None
        return True

     


    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next        
        current.next = start_node
		
		
	
    def leftrightShift(self,left,n):
        if n <= 0 or n > self._size:
            return

        if left == True:
            for i in range (n):
                tempNode = self._head
                elem = tempNode.elem
                self.removeFirst()
                self.addLast(elem)
        else:
            for i in range (n):
                tempNode = self._head
                for k in range (self._size - 1):
                    tempNode = tempNode.next
            
                elem = tempNode.elem
                self.removeLast()
                self.addFirst(elem)


    def toList(self):
        result = []
        current = self._head
        while current:
            result.append(current.elem)
            current = current.next
        return result


    