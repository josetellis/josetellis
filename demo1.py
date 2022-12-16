import  numpy as np

ar1=np.arange(1,10).reshape(3,3)
print(ar1[:,0])
import unittest
class testDemo(unittest.TestCase):
    def test1(self):
        assert 10==10