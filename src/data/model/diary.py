class Diary:
    def __init__(self, user_name: str, password: str, diary_id: int):
        self.diary_id = diary_id
        self.password = password
        self.user_name = user_name
        self.is_locked = True
        self.list_of_entry = []


