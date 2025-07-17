
def add(a, b):
    return a + b

def test_add():
    print("\n\nThe output for 2+3 is: "+ str(add(2, 3)))
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
