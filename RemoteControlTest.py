from RemoteControl import RemoteControl


class RemoteControlTest:
    def __init__(self):
        self.max_y = 0
        self.max_x = 0
        self.min_y = 0
        self.min_x = 0

        self.state = 0

        self.remote = RemoteControl()

        if self.remote.is_available():
            self.remote.start()

            self.remote.events.on_stick_left_north += self.print_north
            self.remote.events.on_stick_left_east += self.print_east
            self.remote.events.on_stick_left_south += self.print_south
            self.remote.events.on_stick_left_west += self.print_west

            self.remote.events.on_stick_left += self.detect_max

            self.remote.events.on_north += self.change_state
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

    def print_north(self, code, state):
        if self.state == 0:
            print code, state

    def print_east(self, code, state):
        if self.state == 1:
            print code, state

    def print_south(self, code, state):
        if self.state == 2:
            print code, state

    def print_west(self, code, state):
        if self.state == 3:
            print code, state

    def change_state(self, code, state):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 3
        elif self.state == 3:
            self.state = 0


remote = RemoteControlTest()
