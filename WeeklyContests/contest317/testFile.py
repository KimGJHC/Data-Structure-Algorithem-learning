
def add(a, b):
    return a + b

def test():
    a = 1
    b = 2
    assert a+b == add(a, b)
    print('tests are done')