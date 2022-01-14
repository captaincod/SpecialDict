class KeyParserException(Exception):
    pass


class KeyParser:
    def __init__(self, key_for_parse):
        self.key = key_for_parse

    def parse(self):
        if self.key[0] == '(':
            key = self.key[1:-1]
        else:
            key = self.key

        key_values = []
        key = key.split()
        key = ''.join(key)
        key = key.split(',')
        if len(key) > 1:
            for j in key:
                if j.isdigit():
                    key_values.append(float(j))
                else:
                    key_values = []
                    break
        else:
            if key[0].isdigit():
                key_values.append(float(key[0]))

        return key_values
