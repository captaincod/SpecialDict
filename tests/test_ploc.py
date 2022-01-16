import pytest

from specialdict import SpecialDict, PlocException, ConditionParserException


class TestPloc:
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

    def test_ploc(self):
        second_map = \
            {'value1': 1, 'value2': 2, 'value3': 3, '1': 10, '2': 20, '3': 30, '(1, 5)': 100,
             '(5, 5)': 200, '(10, 5)': 300, '(1, 5, 3)': 400, '(5, 5, 4)': 500, '(10, 5, 5)': 600}

        specialdict = SpecialDict(second_map)

        assert specialdict.ploc[">=1"] == '{1 = 10, 2 = 20, 3 = 30}'
        assert specialdict.ploc["<3"] == '{1 = 10, 2 = 20}'
        assert specialdict.ploc[">0, >0"] == '{(1, 5) = 100, (5, 5) = 200, (10, 5) = 300}'
        assert specialdict.ploc[">=10, >0"] == '{(10, 5) = 300}'
        assert specialdict.ploc["<5, >=5, >=3"] == '{(1, 5, 3) = 400}'
        assert specialdict.ploc[">0, >0, >0, >0"] == '{}'

        with pytest.raises(PlocException):
            assert specialdict.ploc[0]
        with pytest.raises(ConditionParserException):
            assert specialdict.ploc["lorum"]


