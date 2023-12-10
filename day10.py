data = open("day_10_data.txt", "r").readlines()
start_loc = next((data.index(j), j.index(i)) for j in data for i in j if i == 'S')

vertical_pipe = ("|", (-1, 0), (1, 0))
horizontal_pipe = ("-", (0, -1), (0, 1))
north_east_pipe = ("L", (-1, 0), (0, 1))
north_west_pipe = ("J", (-1, 0), (0, -1))
south_west_pipe = ("7", (1, 0), (0, -1))
south_east_pipe = ("F", (1, 0), (0, 1))
gnd = (".", (0, 0), (0, 0))
pipes = [vertical_pipe, horizontal_pipe, north_east_pipe, north_west_pipe, south_west_pipe, south_east_pipe, gnd]
NESW = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def pipe_connectable(a, b) -> bool:
    pass


ct_pos = 0
ct_neg = 0
