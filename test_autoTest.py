import unittest

from catuo import *
from ELEKTRA_autoTest import *


class TestELEKTRA(unittest.TestCase):
    def setUp(self):
        self.elektra = ELEKTRA()
        foreground()

    def test_pic(self):
        moveTo_image(self.elektra.pic_wenjianming)
        # pg.press("123")


if __name__ == "__main__":
    unittest.main()
