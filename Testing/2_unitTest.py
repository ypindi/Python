import unittest

def divide(a: int, b: int) -> int:
    if (b==0):
        raise ValueError("Cannot divide by 0")
    return a/b

class TestMathOperations(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10,2), 5)
        self.assertEqual(divide(6,-2), -3)
        self.assertRaises(ValueError, divide, 5, 0)

if __name__=='__main__':
    unittest.main()


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> py .\2_unitTest.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> 