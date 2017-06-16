import unittest
from UnitTests import MyDict


class TestMyDict(unittest.TestCase):

    def setUp(self):
        print('----setup---')

    def tearDown(self):
        print('---- tear down ---')


    def test_init(self):
        d = MyDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertIsInstance(d, MyDict)

if __name__ == '__main__':
    unittest.main()