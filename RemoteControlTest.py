from RemoteControl import RemoteControl


def event_handler(code, state):
    print ">", code, state


def start(code, state):
    print "> Pressed start"


remote = RemoteControl()
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

    remote.events.on_start += start
