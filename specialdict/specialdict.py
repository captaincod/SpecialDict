from specialdict.iloc import Iloc
from specialdict.ploc import Ploc


class SpecialDictException(Exception):
    pass


class SpecialDict(dict):

    def __init__(self, values=None):
        if values is None:
            values = {}
        if not isinstance(values, dict):
            raise SpecialDictException("Values should be dictionary")
        super().__init__(values)
        self.iloc = Iloc(self)
        self.ploc = Ploc(self)
