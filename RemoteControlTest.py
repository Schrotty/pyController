from RemoteControl import RemoteControl


def event_handler(code, state):
    print ">", code, state


def start(code, state):
    print "> Pressed start"


remote = RemoteControl(debug_mode=True)
if remote.is_available():
    remote.start()

    # register events
    remote.events.on_north += event_handler
    remote.events.on_west += event_handler
    remote.events.on_east += event_handler
    remote.events.on_south += event_handler

    remote.events.on_cross_north_p += event_handler
    remote.events.on_cross_north_r += event_handler

    remote.events.on_cross_south_p += event_handler
    remote.events.on_cross_south_r += event_handler

    remote.events.on_cross_west_p += event_handler
    remote.events.on_cross_west_r += event_handler

    remote.events.on_cross_east_p += event_handler
    remote.events.on_cross_east_r += event_handler

    remote.events.on_start += event_handler
    remote.events.on_select += event_handler

    remote.events.on_trigger_left += event_handler
    remote.events.on_trigger_right += event_handler

    remote.events.on_shoulder_left_p += event_handler
    remote.events.on_shoulder_left_r += event_handler

    remote.events.on_shoulder_right_p += event_handler
    remote.events.on_shoulder_right_r += event_handler

    remote.events.on_stick_left_north += event_handler
    remote.events.on_stick_left_south += event_handler
    remote.events.on_stick_left_east += event_handler
    remote.events.on_stick_left_west += event_handler

    remote.events.on_any += event_handler
