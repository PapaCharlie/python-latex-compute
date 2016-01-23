from __future__ import division
import unittest
from texpy.integrals import tex_integrals, plain_integrals

class TestIntegrals(unittest.TestCase):

    def test_tex_integrals(self):
        self.assertEqual(tex_integrals("integrate x^3 from 2 to 4"), None)
        self.assertEqual(tex_integrals("\int_0^5 \int_0^x xy+ 4 dy dx"), 1025/8)


    def test_plain_integrals(self):
        self.assertEqual(plain_integrals("integrate x^3 from 2 to 4"), 60)

if __name__ == '__main__':
    unittest.main()