import threading
import ControllerMapping
import pandas
from inputs import devices, get_gamepad
from RemoteControlEvents import RemoteControlEvents


class RemoteControl:
    def __init__(self, profile="default"):
        self.events = RemoteControlEvents()

        self.profile = profile
        self.thread = None
        self.remote_found = True
        self.remote_online = False

        print "> INIT REMOTE CONTROL"
        print "> Looking for gamepad..."
        if not devices.gamepads:
            self.remote_found = False
            print "> No gamepad detected!"
        else:
            print "> Gamepad detected!"

        print ">"
        print "> Load profile '" + self.profile + "'"
        self.load_profile()
        print "> Profile loaded!"
        print ">"

        if self.remote_found:
            print "> Remote control is now available!"
        else:
            print "> Remote control is unavailable!"

    def start(self):
        if self.remote_online:
            print "> Remote control already running!"
        else:
            self.remote_online = True
            self.thread = threading.Thread(target=self.control, args=())
            self.thread.start()

        return self.remote_online

    def stop(self):
        self.remote_online = False
        self.thread.join()

    def load_profile(self):
        try:
            profile = pandas.read_csv('profiles/' + self.profile + '.csv')

            # LEFT BUTTONS
            ControllerMapping.BTN_NORTH = profile['BTN_NORTH'][0]
            ControllerMapping.BTN_EAST = profile['BTN_EAST'][0]
            ControllerMapping.BTN_SOUTH = profile['BTN_SOUTH'][0]
            ControllerMapping.BTN_WEST = profile['BTN_WEST'][0]

            # START AND SELECT
            ControllerMapping.START = profile['START'][0]
            ControllerMapping.SELECT = profile['SELECT'][0]

            # CROSS
            ControllerMapping.CROSS_Y = profile['CROSS_Y'][0]
            ControllerMapping.CROSS_X = profile['CROSS_X'][0]

            # STICK R & STICK L
            ControllerMapping.STICK_RIGHT_Y = profile['STICK_R_Y'][0]
            ControllerMapping.STICK_RIGHT_X = profile['STICK_R_X'][0]
            ControllerMapping.STICK_LEFT_Y = profile['STICK_L_Y'][0]
            ControllerMapping.STICK_LEFT_X = profile['STICK_L_X'][0]

            # TRIGGER AND SHOULDER
            ControllerMapping.TRIGGER_R = profile['TRIGGER_R'][0]
            ControllerMapping.SHOULDR_R = profile['SHOULDER_R'][0]
            ControllerMapping.TRIGGER_L = profile['TRIGGER_L'][0]
            ControllerMapping.SHOULDR_L = profile['SHOULDER_L'][0]

        except (KeyError, IOError):
            print "> Invalid profile! Switching back to default!"
            self.profile = "default"
            self.load_profile()

    def is_available(self):
        return self.remote_found

    def control(self):
        prev_cross_state = None

        while self.remote_online:
            events = get_gamepad()
            for event in events:
                code = event.code
                state = event.state

                self.events.on_any(code, state)

                # BUTTON RELEASED
                if state == 0:

                    # RIGHT BUTTONS
                    if code in ControllerMapping.BTN_NORTH:
                        self.events.on_north(code, state)

                    if code in ControllerMapping.BTN_EAST:
                        self.events.on_east(code, state)

                    if code in ControllerMapping.BTN_SOUTH:
                        self.events.on_south(code, state)

                    if code in ControllerMapping.BTN_WEST:
                        self.events.on_west(code, state)

                    # START AND SELECT
                    if code in ControllerMapping.START:
                        self.events.on_start(code, state)

                    if code in ControllerMapping.SELECT:
                        self.events.on_select(code, state)

                # CONTROLLER CROSS
                if code in ControllerMapping.CROSS_Y or code in ControllerMapping.CROSS_X:

                    # CROSS NORTH AND SOUTH
                    if code in ControllerMapping.CROSS_Y:
                        if state == -1:
                            self.events.on_cross_north_p(code, state)
                            prev_cross_state = -1

                        if state == 1:
                            self.events.on_cross_south_p(code, state)
                            prev_cross_state = 1

                        if state == 0:
                            if prev_cross_state == 1:
                                self.events.on_cross_south_r(code, state)
                            else:
                                self.events.on_cross_north_r(code, state)

                    # CROSS WEST AND EAST
                    if code in ControllerMapping.CROSS_X:
                        if state == -1:
                            self.events.on_cross_west_p(code, state)
                            prev_cross_state = -1

                        if state == 1:
                            self.events.on_cross_east_p(code, state)
                            prev_cross_state = 1

                        if state == 0:
                            if prev_cross_state == 1:
                                self.events.on_cross_east_r(code, state)
                            else:
                                self.events.on_cross_west_r(code, state)

                # TRIGGERS
                if code in ControllerMapping.TRIGGER_L or code in ControllerMapping.TRIGGER_R:

                    # LEFT TRIGGER
                    if code in ControllerMapping.TRIGGER_L:
                        self.events.on_trigger_left(code, state)

                    # RIGHT TRIGGER
                    if code in ControllerMapping.TRIGGER_R:
                        self.events.on_trigger_right(code, state)

                # SHOULDERS
                if code in ControllerMapping.SHOULDR_L or code in ControllerMapping.SHOULDR_R:

                    # LEFT SHOULDER
                    if code in ControllerMapping.SHOULDR_L:

                        # ON RELEASE
                        if state == 0:
                            self.events.on_shoulder_left_r(code, state)

                        # WHEN PRESSED
                        if state == 1:
                            self.events.on_shoulder_left_p(code, state)

                    # RIGHT SHOULDER
                    if code in ControllerMapping.SHOULDR_R:

                        # ON RELEASE
                        if state == 0:
                            self.events.on_shoulder_right_r(code, state)

                        # WHEN PRESSED
                        if state == 1:
                            self.events.on_shoulder_right_p(code, state)

                # LEFT STICK
                if code in ControllerMapping.STICK_LEFT_X or code in ControllerMapping.STICK_LEFT_Y:

                    # X-AXIS
                    if code in ControllerMapping.STICK_LEFT_X:

                        # MOVEMENT EAST
                        if state > 0:
                            self.events.on_stick_left_east(code, state)

                        # MOVEMENT WEST
                        if state < 0:
                            self.events.on_stick_left_west(code, state)

                    # Y-AXIS
                    if code in ControllerMapping.STICK_LEFT_Y:

                        # MOVEMENT NORTH
                        if state > 0:
                            self.events.on_stick_left_north(code, state)

                        # MOVEMENT SOUTH
                        if state < 0:
                            self.events.on_stick_left_south(code, state)
