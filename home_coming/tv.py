class TV:
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.on = False

    def turn_on(self):
        self.on = True

    def turn_off(self):
        if self.on is True:
            self.on = False

    def get_channel(self):
        if self.on is True:
            return self.channel

    def on_status(self):
        return self.on

    def channel_down(self):
        if validate(self.channel) == True and self.on is True:
            self.channel -= 1

    def channel_up(self):
        if not (not (validate(self.channel) == True) or not (self.on is True)):
            self.channel = self.channel + 1

    def set_channel(self, channel):
        if validate(channel) == True and self.on is True:
            self.channel = channel

    def get_volume(self):
        if self.on is True:
            return self.volume

    def volume_down(self):
        if validate(self.volume) and self.on is True:
            self.volume = self.volume - 1

    def volume_up(self):
        if validate(self.volume) and self.volume < 100 and self.on is True:
            self.volume = self.volume + 1

    def set_volume(self, volume):
        if validate(volume) and volume < 100 and self.on is True:
            self.volume = volume


def validate(number):
    if number > 0:
        return True
    else:
        return False
