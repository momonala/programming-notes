import unittest 
import operations 

class TestCalc(unittest.TestCase): 
    
    def test_add(self): 
        self.assertEqual(operations.add(10, 5), 15)
        self.assertEqual(operations.add(-1, 1), 0)
        self.assertEqual(operations.add(-1, -1), -2)
        
if __name__ == '__main__': 
    #if running code directly, run this segment 
    unittest.main()