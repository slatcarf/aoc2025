file = open("input")


fresh_ranges = []
# get ranges
for line in file:
    if line != "\n":
        start, end = list(map(int, line.strip().split("-")))
        fresh_ranges.append(range(start, end + 1))
    else:
        break


fresh_count = 0
# get ingredients
for line in file:
    if line == "\n":
        break

    id = int(line.strip())
    for range in fresh_ranges:
        if id in range:
            fresh_count += 1
            break  # ingredient can appear in several ranges

print(fresh_count)
