import unittest

class Test(unittest.TestCase):
    def test_loci_true(self):
        start = 10
        len = 5
        pos = 12
        self.assertTrue((start<= pos < start+len))

    def test_loci_false(self):
        start = 10
        len = 5
        pos = 18
        self.assertFalse((start<= pos < start+len))


if __name__ == '__main__':
    unittest.main()