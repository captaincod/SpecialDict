class IlocException(Exception):
    pass


class Iloc(dict):

    def __init__(self, special_dict: dict):
        super().__init__()
        self.special_dict = special_dict

    def __getitem__(self, item_index):
        if not isinstance(item_index, int) or item_index > len(self.special_dict) or item_index < 0:
            raise IlocException("Invalid index: must be positive integer in range of dictionary")
        else:
            self.special_dict = {k: v for k, v in sorted(self.special_dict.items(), key=lambda item: item[0])}
            sorted_indices = list(self.special_dict.keys())
            return self.special_dict[sorted_indices[item_index]]