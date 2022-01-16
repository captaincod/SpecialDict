import pytest
from specialdict import SpecialDict, SpecialDictException


@pytest.fixture
def check_keys():
    return ['1', '1, 5', '10, 5', '2', '3', '5, 5', 'value1', 'value2', 'value3']


@pytest.fixture
def check_values():
    return [10, 100, 300, 20, 30, 200, 1, 2, 3]


class TestSpecialDict:
    def test_init(self, check_keys, check_values):
        sorted_keys = check_keys
        sorted_values = check_values
        specialdict = SpecialDict()
        specialdict["value1"] = 1
        specialdict["value2"] = 2
        specialdict["value3"] = 3
        specialdict["1"] = 10
        specialdict["2"] = 20
        specialdict["3"] = 30
        specialdict["1, 5"] = 100
        specialdict["5, 5"] = 200
        specialdict["10, 5"] = 300
        assert specialdict['value1'] == 1 and specialdict['10, 5'] == 300
        assert specialdict[sorted_keys[0]] == sorted_values[0]
        with pytest.raises(SpecialDictException):
            wrongspecialdict = SpecialDict('i am dictionary')