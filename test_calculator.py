from calculator import addition, subtraction, multiplication, division

def test_addition():
    # normal cases
    assert addition(2,4) == 6
    assert addition(-4,2) == -2
    assert addition(0,0) == 0
    # edge cases
    assert addition(1e10, 1e10) == 2e10
    assert addition(-2,-3) == -5
    
def test_subtraction():
    # normal cases
    assert subtraction(14,5) == 9 
    assert subtraction(2,8) == -6
    assert subtraction(0,0) == 0
    # edge cases
    assert subtraction(1e10,1e10) == 0
    assert subtraction(-4,-3) == -1

def test_multiplication():
    # normal cases
    assert multiplication(8,4) == 32
    assert multiplication(-7,4) == -28
    assert multiplication(0,4) == 0
    # edge case
    assert multiplication(1e10,1e-10) == 1
    assert multiplication(-1,-1) == 1

def test_division():
    # normal cases 
    assert division(8,4) == 2  
    assert division(-16,4) == -4
    assert division(1,2) == 0.5
    # edge cases
    assert division(1e10, 1e10) == 1
    assert division(-1,-1) == 1
    # test division by zero
    try:
        division(1,0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError for divion by zero"

if __name__ == "__main__":
        test_addition()
        print("test_addition passed.")

        test_subtraction()
        print("test_subtraction passed.")

        test_multiplication()
        print("test_multiplication passed.")

        test_division
        print("test_division passed.")
              