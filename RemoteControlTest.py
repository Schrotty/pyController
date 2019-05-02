from RemoteControl import RemoteControl


class RemoteControlTest:
    def __init__(self):
        self.max_y = 0
        self.max_x = 0
        self.min_y = 0
        self.min_x = 0

        self.remote = RemoteControl()

        if self.remote.is_available():
            self.remote.start()

            self.remote.events.on_stick_right += self.detect_min
            self.remote.events.on_stick_right += self.detect_max

            self.remote.events.on_north += self.print_max
            self.remote.events.on_north += self.print_min

    def detect_min(self, code, state):
        if state < self.min_y:
            self.min_y = state

        if state < self.min_x:
            self.min_x = state

    def detect_max(self, code, state):
        if state > self.max_x:
            self.max_x = state

        if state > self.max_y:
            self.max_y = state

    def print_max(self, code, state):
        print "MAX_Y:", self.max_y, "MAX_X:", self.max_x

    def print_min(self, code, state):
        print "MIN_Y:", self.min_y, "MIN_X:", self.min_x


remote = RemoteControlTest()
