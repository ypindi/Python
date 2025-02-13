import unittest
from math_operations import divide

class TestingMathOperations(unittest.TestCase):
    def testDivide(self):
        self.assertEqual(divide(5, 2), 2)
        self.assertEqual(divide(-6, 4), -2)
        with self.assertRaises(ValueError):
            divide(5,0)

if __name__=='__main__':
    unittest.main()


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> py .\2_test_math_operations.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> 