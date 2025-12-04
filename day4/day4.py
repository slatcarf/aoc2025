file = open("input")


file_arr = file.readlines()
line_len = len(file_arr[0])
file_len = len(file_arr)


count = 0
for i, line in enumerate(file_arr):
    for j, slot in enumerate(line):
        surrounding_count = 0
        if slot != "@":
            continue

        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                # skip counting the inspected roll itself
                if x == i and y == j:
                    continue

                if 0 <= x < file_len and 0 <= y < line_len and file_arr[x][y] == "@":
                    surrounding_count += 1
        # print(slot,surrounding_count)
        if surrounding_count < 4 and slot == "@":
            count += 1
print(count)
