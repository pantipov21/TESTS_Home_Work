import pytest
from HW1 import get_name, get_shelf, delete_document

Numbers_Names = [
    ("2207 876234", "Василий Гупкин"),
    ("11-2", "Геннадий Покемонов"),
    ("10006", "Аристарх Павлов")
]

Numbers_Shelves = [
    ('2207 876234', '1'),
    ('11-2', '1'),
    ('10006', '2')
]


@pytest.fixture()
def data_negative():
    return '23423423', False



class TestFunctions:
    def setup(self):
        print('===> setup')

    def teardown(self):
        print('===> teardown')

    @pytest.mark.parametrize("a, result", Numbers_Names)
    def test_get_name(self, a, result):
        assert get_name(a) == result

    @pytest.mark.parametrize("a, result", Numbers_Shelves)
    def test_get_shelf(self, a, result):
        assert get_shelf(a) == result

    def test_delete_document(self, data_negative):
        a, result = data_negative
        assert delete_document(a) == result
