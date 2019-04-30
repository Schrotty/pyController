from events import Events


class RemoteControlEvents(Events):
    __events__ = ('on_north', 'on_east', 'on_south', 'on_west',
                  'on_select', 'on_start',
                  'on_cross_north_p', 'on_cross_north_r', 'on_cross_south_p', 'on_cross_south_r',
                  'on_cross_west_p', 'on_cross_west_r', 'on_cross_east_p', 'on_cross_east_r')

