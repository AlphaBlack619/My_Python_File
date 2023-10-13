from data.repository.diary_repository import DiaryRepository


class DiaryRepositoriesImpl(DiaryRepository):
    def __init__(self):
        self.diaryList = []
        self.current_id = 1

    def __generate_id(self):
        generated_id = self.diaryList.count(self)
        return generated_id + 1

    def save(self, diary):
        diary.setId(self.__generate_id())
        self.diaryList.append(diary)
        return diary

    def delete(self, diary):
        self.diaryList.remove(diary)

    def find_by_id(self, user_id):
        for diary in self.diaryList:
            if diary.getId() == user_id:
                return diary
        return None

    def find_by_user(self, username):
        for diary in self.diaryList:
            if diary.getUser_Name() == username:
                return diary
        return None

    def find_all(self):
        return self.diaryList

    def count(self):
        return len(self.diaryList)

    def clear(self):
        self.diaryList.clear()
