from specialdict.condition_parser import ConditionParser
from specialdict.key_parser import KeyParser


class PlocException(Exception):
    pass


def compare(key, operation, condition_digit) -> bool:
    if operation == '=':
        return key == condition_digit
    if operation == '<':
        return key < condition_digit
    if operation == '>':
        return key > condition_digit
    if operation == '<=':
        return key <= condition_digit
    if operation == '>=':
        return key >= condition_digit
    if operation == '<>':
        return key != condition_digit


class Ploc(dict):

    def __init__(self, special_dict: dict):
        super().__init__()
        self.special_dict = special_dict

    def __getitem__(self, condition):
        if not isinstance(condition, str):
            raise PlocException("Invalid condition: must be string")

        conditions = ConditionParser(condition)
        parsed_conditions = conditions.parse()

        selected = '{'

        for k, v in self.special_dict.items():
            key_for_parse = KeyParser(k)
            key_values = key_for_parse.parse()

            if len(key_values) != len(parsed_conditions):
                continue
            else:
                for j in range(len(key_values)):
                    key = key_values[j]
                    operation = parsed_conditions[j]['operation']
                    digit = parsed_conditions[j]['digit']

                    if compare(key, operation, digit):
                        if len(selected) > 1:
                            selected += ', '
                        selected += str(k) + ' = ' + str(v)
                        break
                    else:
                        break

        selected += '}'

        return selected
