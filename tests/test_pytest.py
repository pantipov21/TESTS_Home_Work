import pytest
from main import multiplication_int, multiplication_string

fixture = [
    (2,3,6),
    (1,2,2),
    (-1,-2,2),
    (-2,2,-4)
]


@pytest.fixture()
def data():
    return 'a',3,'aaa'


class TestFunctionsPytest:
    def setup(self):
        print('===> setup')

    def teardown(self):
        print('===> teardown')

    def test_multiplication_string(self, data):
        a, b, result = data
        assert multiplication_string(a, b) == result


    @pytest.mark.parametrize("a, b, result", fixture)
    def test_multiplication_int(self, a, b, result):
        assert multiplication_int(a, b) == result
