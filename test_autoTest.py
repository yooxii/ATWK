import unittest

from catuo import *
from ELEKTRA_autoTest import *


class TestELEKTRA(unittest.TestCase):
    def setUp(self):
        self.elektra = ELEKTRA()
        foreground()

    def test_pic(self):
        moveTo_image(self.elektra.pic_qujian, ["bottom", (80, 20)])


if __name__ == "__main__":
    unittest.main()
