import datetime


class Entry:
    def __init__(self, user_id, title, body):
        self.entry_id = user_id
        self.title = title
        self.body = body
        self.time = datetime.datetime.now()
