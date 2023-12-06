with open("day_5_data.txt", "r") as fh:
    my_fh = fh.readlines()


def calc(seed: int, stop, start, distance) -> int:
    if int(seed) in range(int(start), int(start) + int(distance)):
        return int(seed) + int(stop) - int(start)
    else:
        return int(seed)


def get_val(seed: int) -> int:
    fh = iter(my_fh)
    map_done = False
    try:
        while True:
            line = next(fh)
            if any(["\n" == line, "seed" in line]):
                continue
            if "map" in line:
                map_done = False
            else:
                if map_done:
                    continue
                stop, start, distance = line.split()
                before_seed = seed
                seed = calc(seed, stop, start, distance)
                if before_seed != seed:
                    map_done = True
    except StopIteration:
        return seed


seeds = [int(i) for i in open("day_5_data.txt", "r").readline().split()[1:]]
print(min([get_val(int(seed)) for seed in seeds]))
