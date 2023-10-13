from abc import ABC


class DiaryRepository(ABC):
    def save(self, diary):
        pass

    def delete(self, diary):
        pass

    def find_by_id(self, user_id):
        pass

    def find_all(self):
        pass

    def count(self):
        pass

    def clear(self):
        pass

    def find_by_user(self, username):
        pass
