class ConditionParserException(Exception):
    pass


class ConditionParser:

    def __init__(self, condition_string):
        self.condition_string = condition_string

    def check_condition(self, operation, digit) -> bool:
        operations = ['=', '<', '>', '<=', '>=', '<>']
        if operation in operations and digit.isdigit():
            return True
        else:
            return False

    def parse(self):
        trimmed_conditions = self.condition_string.split()
        trimmed_conditions = ''.join(trimmed_conditions)
        trimmed_conditions = trimmed_conditions.split(',')

        conditions_list = []
        condition = {'operation': '', 'digit': None}  # проверить ок ли операция

        symbols = ['<', '>', '=']

        if len(trimmed_conditions) > 1:
            digit = ''
            for ind in range(len(trimmed_conditions)):
                trimmed_condition = trimmed_conditions[ind]
                for current_char in trimmed_condition:
                    if current_char in symbols:
                        condition['operation'] += current_char
                    elif current_char.isdigit():
                        digit += current_char
                    elif current_char == ',':
                        condition['digit'] = digit
                        if self.check_condition(condition['operation'], digit):
                            condition['digit'] = float(digit)
                            conditions_list.append(condition)
                        else:
                            raise ConditionParserException(f"Wrong condition")
                        condition = {'operation': '', 'digit': None}
                        digit = ''
                condition['digit'] = digit
                if self.check_condition(condition['operation'], digit):
                    condition['digit'] = float(digit)
                    conditions_list.append(condition)
                else:
                    raise ConditionParserException(f"Wrong condition")
                condition = {'operation': '', 'digit': None}
                digit = ''
        else:
            digit = ''
            for current_char in trimmed_conditions[0]:
                if current_char in symbols:
                    condition['operation'] += current_char
                elif current_char.isdigit():
                    digit += current_char
            if self.check_condition(condition['operation'], digit):
                condition['digit'] = float(digit)
                conditions_list.append(condition)
            else:
                raise ConditionParserException(f"Wrong condition")

        if len(conditions_list) < 1:
            raise ConditionParserException("No edible conditions found")

        return conditions_list


