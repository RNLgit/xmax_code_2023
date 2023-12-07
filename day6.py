import sys
import time

ts = time.time()

with open(sys.argv[1], "r") as fh:
    data = fh.readlines()
data_stripped = [i.split()[1:] for i in data]
# data_zipped = [(int(time_req), int(record_dist)) for time_req, record_dist in zip(data_stripped[0], data_stripped[1])]
# p2
data_zipped = [[int("".join(i)) for i in data_stripped]]


def calc_distance(tot_s, hold_s, record_dist):
    res = (tot_s - hold_s) * hold_s
    return res if res > record_dist else None


def find_win_ways(race_time, record_dist):
    ct = 0
    for i in range(1, race_time + 1):
        if calc_distance(race_time, i, record_dist):
            ct += 1
    return ct


ways_ct = 1
for race_time, record_dist in data_zipped:
    ways_ct *= find_win_ways(race_time, record_dist)
print(f"answer: {ways_ct}, {time.time() - ts}s to run")
