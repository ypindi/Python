import pytest

# Function to be tested
def subtract(a, b):
    return a - b

# Pytest Test Cases
def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 10) == 0
    assert subtract(7, 9) == -2

def divide0():
    with pytest.raises(ZeroDivisionError):
        1/0

divide0()


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> py .\3_pytest.py
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Testing> 