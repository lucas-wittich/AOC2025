import bisect


def parse_input(lines):
    ranges = []
    ids = []

    it = iter(lines)
    for line in it:
        line = line.strip()
        if not line:
            break

        start, stop = line.split('-')
        ranges.append((int(start), int(stop)))

    for line in it:
        if not line:
            continue

        ids.append(int(line))

    return ranges, ids


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = []
    cur_start, cur_end = ranges[0]
    for s, e in ranges[1:]:
        if s <= cur_end:
            cur_end = max(cur_end, e)

        else:
            merged.append((cur_start, cur_end))
            cur_start = s
            cur_end = e

    merged.append((cur_start, cur_end))

    return merged


file = open('input.txt', 'r')
ranges, ids = parse_input(file)
merged = merge_ranges(ranges)
starts = [s for (s, _) in merged]


# Part 1
# fresh_count = 0
# for x in ids:
#     idx = bisect.bisect_right(starts, x) - 1
#     if idx >= 0:
#         s, e = merged[idx]
#         if s <= x <= e:
#             fresh_count += 1

# print(fresh_count)

fresh_count = 0
for (s, e) in merged:
    fresh_nmbrs = e - s + 1
    fresh_count += fresh_nmbrs

print(fresh_count)
