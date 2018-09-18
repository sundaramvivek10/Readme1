from function import *
def test_large():
    for numb in [1, 2, -2]:
        x = large(numb, 0)
        assert x > 0
