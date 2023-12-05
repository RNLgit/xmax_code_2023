def calc(seed: int, stop, start, distance) -> int:
    if int(seed) in range(int(start), int(distance)):
        return int(stop) - int(start) + int(seed)