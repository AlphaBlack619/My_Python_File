from data.model.entry import Entry
from data.repository.entry_repository import EntryRepository


class EntryRepositoryImpl(EntryRepository):
    def __init__(self):
        self.entries = []
        self.current_id = 1

    def __generate_id(self):
        generated_id = self.current_id + self.entries.count(self)
        self.current_id += 1
        return generated_id

    def save(self, entry: Entry):
        entry_does_not_exist = entry.entry_id == 0
        if entry_does_not_exist:
            self.save_new(entry)
        else:
            self.update(entry)

        return entry

    def save_new(self, entry: Entry):
        entry.entry_id = self.__generate_id()
        self.entries.append(entry)

    def update(self, entry_id):
        new_entry = self.find_by_id(entry_id)
        new_entry.setTitle()
        new_entry.setBody()

    def delete(self, entry):
        found_entry = self.find_by_id(entry.entry_id)
        self.entries.remove(found_entry)

    def count(self):
        return len(self.entries)

    def find_by_id(self, entry_id):
        for entry in self.entries:
            if entry.entry_id == entry_id:
                return entry
        return None

    def find_all(self):
        return self.entries

    def clear(self):
        self.entries.clear()

    def find_by_user(self, entry_id, title):
        for entry in self.entries:
            if entry.entry_id == entry_id and entry.title.lower() == title.lower():
                return entry
        return None
