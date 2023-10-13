from abc import ABC

from data.model.entry import Entry


class EntryRepository(ABC):
    def save(self, entry: Entry):
        pass

    def delete(self, entry: Entry):
        pass

    def find_by_id(self, user_id: int):
        pass

    def find_all(self):
        pass

    def count(self):
        pass

    def clear(self):
        pass

    def find_by_user(self, entry_id: int, username: str):
        pass
