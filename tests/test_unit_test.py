import unittest

from main import multiplication_int, multiplication_string


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_multiplication_int(self):
        self.assertEqual(multiplication_int(2,3),6)

    @unittest.expectedFailure
    def test_multiplication_int_failure(self):
        self.assertEqual(multiplication_int(2,3),4)
