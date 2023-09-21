from oop.bank import Bank


class CentralBank:
    def __init__(self, name: str):
        self.name = name
        self.bank_list = []

    def search_for_banks(self, bank: str):
        try:
            for banks in self.bank_list:
                if bank == banks.get_bank_name():
                    return banks
                else:
                    raise ValueError('Bank Not Found')
        except ValueError:
            print('Bank Not Found')
        except TypeError:
            print('Invalid Type')

    def register_bank(self, bank: Bank):
        try:
            self.bank_list.append(bank)
        except TypeError:
            print('Invalid bank')
        except ValueError:
            print('Invalid Type')

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        try:
            self._name = value
        except ValueError:
            print('Check Value')
        except TypeError:
            print('Invalid Type')

