
import unittest
from phase1 import SList2
from slistH import SList
from slistH import SNode

class Test(unittest.TestCase):
   	#setUp is a method which is ran before a test method is executed. 
   	#This is useful if you need some data (for example) to be present before running a test.
    def setUp(self):
        #Lists used for the test_delLargestSeq method.
        self.slist1 = SList2()
        self.slist1.addLast(3)
        self.slist1.addLast(3)
        self.slist1.addLast(3)
        self.slist1.addLast(4)
        self.slist1.addLast(5)
        self.slist1.addLast(6)
        self.slist1.addLast(6)
        self.slist1.addLast(6)
        self.slist1.addLast(7)
        self.slist1.addLast(7)
        self.slist1.addLast(7)
        self.slist1.addLast(7)
        self.slist1.addLast(2)

        self.slist2 = SList2()
        self.slist2.addLast(8)
        self.slist2.addLast(8)
        self.slist2.addLast(8)
        self.slist2.addLast(8)
        self.slist2.addLast(4)
        self.slist2.addLast(5)
        self.slist2.addLast(6)
        self.slist2.addLast(6)
        self.slist2.addLast(6)
        self.slist2.addLast(7)
        self.slist2.addLast(7)
        self.slist2.addLast(7)
        self.slist2.addLast(7)
        self.slist2.addLast(2)

        self.slist3 = SList2()
        self.slist3.addLast(6)
        self.slist3.addLast(6)
        self.slist3.addLast(8)
        self.slist3.addLast(8)
        self.slist3.addLast(4)
        self.slist3.addLast(4)
        self.slist3.addLast(12)
        self.slist3.addLast(12)
        
        self.slist16 = SList2()
        self.slist16.addLast(1)
        self.slist16.addLast(2)
        self.slist16.addLast(3)
        self.slist16.addLast(4)
        self.slist16.addLast(5)
        
        self.slist17 = SList2()
        self.slist17.addLast(10)
        
        self.slist18 = SList2()

        #Lists used for the test_fix_loop method.
        self.slist4 = SList2()
        self.slist4.addLast(1)
        self.slist4.addLast(2)
        self.slist4.addLast(3)
        self.slist4.addLast(4)
        self.slist4.addLast(5)
        self.slist4.create_loop(2)
        
        self.slist5 = SList2()
        self.slist5.addLast(1)
        self.slist5.addLast(2)
        self.slist5.addLast(3)
        self.slist5.addLast(4)
        self.slist5.addLast(5)
        self.slist5.create_loop(1)

        self.slist6 = SList2()
        self.slist6.addLast(1)
        self.slist6.addLast(2)
        self.slist6.addLast(3)
        self.slist6.addLast(4)
        self.slist6.addLast(5)
        
        self.slist19 = SList2()
        self.slist19.addLast(1)
        self.slist19.addLast(2)
        self.slist19.create_loop(1)
        
        self.slist20 = SList2()
        self.slist20.addLast(1)
        self.slist20.addLast(2)
        self.slist20.addLast(3)
        self.slist20.addLast(4)
        self.slist20.create_loop(0)
        
        self.slist21 = SList2()
        self.slist21.addLast(1)
        self.slist21.create_loop(0)
        

        #Lists used to test the test_leftrightShift method.
        self.slist7 = SList2()
        self.slist7.addLast(1)
        self.slist7.addLast(2)
        self.slist7.addLast(3)
        self.slist7.addLast(4)
        self.slist7.addLast(5)
        self.slist7.addLast(6)
        self.slist7.addLast(7)

        self.slist8 = SList2()
        self.slist8.addLast(1)
        self.slist8.addLast(2)
        self.slist8.addLast(3)
        self.slist8.addLast(4)
        self.slist8.addLast(5)
        self.slist8.addLast(6)
        self.slist8.addLast(7)

        self.slist9 = SList2()
        self.slist9.addLast(1)
        self.slist9.addLast(2)
        self.slist9.addLast(3)
        self.slist9.addLast(4)
        self.slist9.addLast(5)
        self.slist9.addLast(6)
        self.slist9.addLast(7)

        self.slist10 = SList2()
        self.slist10.addLast(1)
        self.slist10.addLast(2)
        self.slist10.addLast(3)
        self.slist10.addLast(4)
        self.slist10.addLast(5)
        self.slist10.addLast(6)
        self.slist10.addLast(7)

        self.slist11 = SList2()
        self.slist11.addLast(1)
        self.slist11.addLast(2)
        self.slist11.addLast(3)
        self.slist11.addLast(4)
        self.slist11.addLast(5)
        self.slist11.addLast(6)
        self.slist11.addLast(7)
        
        self.slist12 = SList2()
        self.slist12.addLast(1)
        self.slist12.addLast(2)
        self.slist12.addLast(3)
        self.slist12.addLast(4)
        self.slist12.addLast(5)
        self.slist12.addLast(6)
        self.slist12.addLast(7)
        
        self.slist13 = SList2()
        self.slist13.addLast(1)
        self.slist13.addLast(2)
        self.slist13.addLast(3)
        self.slist13.addLast(4)
        self.slist13.addLast(5)
        self.slist13.addLast(6)
        self.slist13.addLast(7)
        
        self.slist14 = SList2()
        self.slist14.addLast(1)
        self.slist14.addLast(2)
        self.slist14.addLast(3)
        self.slist14.addLast(4)
        self.slist14.addLast(5)
        self.slist14.addLast(6)
        self.slist14.addLast(7)
        
        self.slist15 = SList2()


    def test_delLargestSeq(self):
        #assertEqaul basically checks if the method´s result is the same as the expected result, if not, is raises and exception.

        #Test case 1: List has multiple sequences of equal numbers.
        self.slist1.delLargestSeq()
        self.assertEqual(self.slist1.toList(), [3, 3, 3, 4, 5, 6, 6, 6, 2])

        #Test case 2: List has two sequences of same amount but one is at the begining and the other at the end of the list.
        self.slist2.delLargestSeq()
        self.assertEqual(self.slist2.toList(), [8,8,8,8,4,5,6,6,6,2])
        
        #Test case 3: there is no largest sequence of equal numbers.
        self.slist3.delLargestSeq()
        self.assertEqual(self.slist3.toList(), [6,6,8,8,4,4])
        
        #Test case 4: An element is a valid sequence in the list.
        self.slist16.delLargestSeq()
        self.assertEqual(self.slist16.toList(), [1,2,3,4])
    
        #Test case 5: There is only one element in the list.
        self.slist17.delLargestSeq()
        self.assertEqual(self.slist17.toList(), [])

        #Test case 6: Empty list.
        self.slist18.delLargestSeq()
        self.assertEqual(self.slist18.toList(), [])
        
        
    
    def test_fix_loop(self):
        #assertIsNone is used to check whether the next attribute of a given node is None or not. If the attribute is None, then the assertion will pass, otherwise, it will raise an exception indicating that the test has failed.
        #assertTrue checks whether a given condition is true or not, and raises an exception if the condition is not true. assertFalse does opposite.
        
        #Test case 1: List has a loop between middle elements of the list.
        self.assertTrue(self.slist4.fix_loop())
        self.assertEqual(self.slist4.toList(), [1, 2, 3, 4, 5])
        
        #Test case 2: List loops itself (last node connected to first)
        self.assertTrue(self.slist5.fix_loop())
        self.assertEqual(self.slist5.toList(), [1, 2, 3, 4, 5])
        
        #Test case 3: List has no loop
        self.assertFalse(self.slist6.fix_loop())
        
        # Test case 4: List has a loop with only two elements
        self.assertTrue(self.slist19.fix_loop())
        self.assertEqual(self.slist19.toList(), [1, 2])
        
        # Test case 5: List has a loop with all elements
        self.assertTrue(self.slist20.fix_loop())
        self.assertEqual(self.slist20.toList(), [1, 2, 3, 4])
        
        # Test case 6: List has a loop with only one element
        self.assertTrue(self.slist21.fix_loop())
        self.assertEqual(self.slist21.toList(), [1])

    def test_leftrightShift(self):
        
        self.slist7.leftrightShift(True, 2)
        self.assertEqual(self.slist7.toList(), [3, 4, 5, 6, 7, 1, 2])

        self.slist8.leftrightShift(True, 1)
        self.assertEqual(self.slist8.toList(), [2, 3, 4, 5, 6, 7, 1])
        
        self.slist9.leftrightShift(True, 4)
        self.assertEqual(self.slist9.toList(), [5, 6 , 7 , 1,2,3,4])

        self.slist10.leftrightShift(False, 2)
        self.assertEqual(self.slist10.toList(), [6,7,1,2,3,4,5])

        self.slist11.leftrightShift(False, 1)
        self.assertEqual(self.slist11.toList(), [7,1,2,3,4,5,6])
        
        self.slist12.leftrightShift(False, 4)
        self.assertEqual(self.slist12.toList(), [4,5,6,7,1,2,3])
        
        self.slist13.leftrightShift(False, 7)
        self.assertEqual(self.slist13.toList(), [1,2,3,4,5,6,7])
        
        self.slist14.leftrightShift(False, 10)
        self.assertEqual(self.slist14.toList(), [1,2,3,4,5,6,7])
        
        self.slist15.leftrightShift(False, 10)
        self.assertEqual(self.slist15.toList(), [])

        
if __name__ == "__main__":
    unittest.main()