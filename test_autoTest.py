import unittest

from catuo import *
from ELEKTRA_autoTest import *

class TestELEKTRA(unittest.TestCase):
    def setUp(self):
        self.elektra = ELEKTRA()
        foreground()
        
    def test_pic(self):
        self.assertTrue(exists_image(self.elektra.pic_ln_l1, confidence=0.93))
        
if __name__ == '__main__':
    unittest.main()