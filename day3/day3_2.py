file = open("input")
num_bats = 12

sum = 0
for line in file:
    if line == "\n":
        break
    line = line.strip()
    largest = []
    shift = 0

    n = num_bats - 1
    while n >= 0:
        start = 0 if n == num_bats - 1 else shift
        end = len(line) - n
        window = line[start:end]
        # print("start:", start, "end:", end, "window:", window, "max:", max(window))
        max_rel_index = window.index(max(window))
        largest.append(max_rel_index + shift)
        shift += max_rel_index + 1
        n -= 1
        # print(largest)
    num = int("".join(list(map(lambda n: line[n], largest))))
    sum += num

print(sum)


# 4129329345224342348111
# 12345

# expected: 888911112111

# get 4 largest numbers in string:
# il = search for largest number in line[:-3]
# append il to list
# il2 = search for largest number in line[(il + 1):-2]
# append il to list
# il3(6) = serach for largest number in line [(il2 + 1):-1]
# append il to list
# il4(18) = search for largest numberin line [(il3 +1):]
