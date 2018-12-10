# To run w/o code on lines 7 & 8
# in command line, copy path, open CL, navigate to folder file is in,
# type : python -m unittest 'nameOfUnitTestFile'
import unittest
from Examples import Example

if __name__ == '__main__':
    unittest.main()

class MyTestCase(unittest.TestCase):
    # dummy test
    # def test_something(self):
    #     self.assertEqual(True, False)

    @classmethod
    def setUpClass(cls):
        print('Starting all test methods...')
        print('\n')

    @classmethod
    def tearDownClass(cls):
        print('all test methods completed!')

    def setUp(self):
        print('Test starting...')

    def tearDown(self):
        print('test completed!')
        print('\n')

    # have to start unit tests with the word test or pycharm will fail to recognize
    def test_add(self):
        result = Example.add(self, 10, 32)
        self.assertEqual(result, 42)
    # following should cause fail: self.assertEqual(result,52)

    def test_sub(self):
        result = Example.sub(self, 50, 10)
        self.assertEqual(result, 40)

    def test_add2(self):
        self.assertEqual(Example.add(self, -10, -32), -42)
        self.assertEqual(Example.add(self, 0, 0), 0)
        self.assertEqual(Example.add(self, 10, 32), 42)


