def calc(seed: int, stop, start, distance) -> int:
    if int(seed) in range(int(start), int(distance)):
        return int(seed) + int(stop) - int(start)
    else:
        return int(seed)


def get_val(seed: int) -> int:
    fh = open("day_5_data.txt", "r")
    try:
        while True:
            line = next(fh)
            if any(["\n" == line, "map" in line, "seed" in line]):
                continue
            else:
                stop, start, distance = line.split()
                seed = calc(seed, stop, start, distance)
    except StopIteration:
        return seed
    finally:
        fh.close()


seeds = open("day_5_data.txt", "r").readline().split()[1:]
print(sorted([get_val(seed) for seed in seeds])[0])
