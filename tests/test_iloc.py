import pytest

from specialdict import SpecialDict, IlocException


@pytest.fixture
def check_keys():
    return ['1', '1, 5', '10, 5', '2', '3', '5, 5', 'value1', 'value2', 'value3']


@pytest.fixture
def check_values():
    return [10, 100, 300, 20, 30, 200, 1, 2, 3]


class TestIloc:
    def test_init(self):
        first_map = \
            {'value1': 1, 'value2': 2, 'value3': 3, '1': 10, '2': 20, '3': 30, '1, 5': 100, '5, 5': 200, '10, 5': 300}
        second_map = \
            {'value1': 1, 'value2': 2, 'value3': 3, '1': 10, '2': 20, '3': 30, '(1, 5)': 100,
             '(5, 5)': 200, '(10, 5)': 300, '(1, 5, 3)': 400, '(5, 5, 4)': 500, '(10, 5, 5)': 600}

        specialdict1 = SpecialDict(first_map)
        specialdict2 = SpecialDict(second_map)
        assert specialdict1['value1'] == 1 and specialdict1['10, 5'] == 300
        assert specialdict2['value3'] == 3 and specialdict2['(10, 5, 5)'] == 600

    def test_iloc(self, check_keys, check_values):
        sorted_keys = check_keys
        sorted_values = check_values

        first_map = \
            {'value1': 1, 'value2': 2, 'value3': 3, '1': 10, '2': 20, '3': 30, '1, 5': 100, '5, 5': 200, '10, 5': 300}

        specialdict = SpecialDict(first_map)

        for i in [0, 2, 5, 8]:
            assert specialdict.iloc[i] == sorted_values[i] and specialdict.iloc[i] == first_map[sorted_keys[i]]

        with pytest.raises(IlocException):
            assert specialdict.iloc[10]
        with pytest.raises(IlocException):
            assert specialdict.iloc['sfdfs']


