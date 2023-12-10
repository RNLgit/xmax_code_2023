data = open("day_10_data.txt", "r").readlines()
start_loc = next((data.index(j), j.index(i)) for j in data for i in j if i == "S")

vertical_pipe = ("|", (-1, 0), (1, 0))
horizontal_pipe = ("-", (0, -1), (0, 1))
north_east_pipe = ("L", (-1, 0), (0, 1))
north_west_pipe = ("J", (-1, 0), (0, -1))
south_west_pipe = ("7", (1, 0), (0, -1))
south_east_pipe = ("F", (1, 0), (0, 1))
gnd = (".", (0, 0), (0, 0))
pipes = (vertical_pipe, horizontal_pipe, north_east_pipe, north_west_pipe, south_west_pipe, south_east_pipe, gnd)
NESW = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def pipe_connect(current_val, next_pipe_val):
    """
    e.g. curr: (0, 1), trial: ((0, 1), (0, -1)) gives (0, 1)
    """
    for i in range(0, 2):
        for j in next_pipe_val:
            if current_val[i] == 0 or j[i] == 0:
                continue
            elif current_val[i] == -1 * j[i]:
                return next(val for val in next_pipe_val if val != j)  # return the other free end
    return None


def pipe_val(loc):
    symbol = data[loc[0]][loc[1]]
    return next((val1, val2) for sym, val1, val2 in pipes if sym == symbol)


def moving(dir_loc, curr_loc):
    sym, val1, val2 = data[curr_loc[0] + dir_loc[0]][curr_loc[1] + dir_loc[1]]
    dir_loc = pipe_connect(data[curr_loc[0]][curr_loc[1]], (val1, val2))
    if dir_loc:
        moving(dir_loc, (curr_loc[0] + dir_loc[0], curr_loc[1] + dir_loc[1]))
    else:
        return data[curr_loc[0] + dir_loc[0]][curr_loc[1] + dir_loc[1]]


ct_pos = 1
next_loc = [[start_loc[0] - 1], [start_loc[1]]]
# ct_neg = 0
# pos_neg = data[start_loc[0]][start_loc[1] + 1]
while True:
    for i in NESW:
        moving()
