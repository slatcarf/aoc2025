f = open("input.txt")

current = 50;
count = 0;
for line in f:
    if(line == "\n"):
       break
    stripped = line.strip()
    direction = stripped[0]
    amount = stripped[1:]

    if(direction == "R"):
        current = (current + int(amount)) % 100
    elif(direction == "L"):
        current = (current - int(amount)) % 100
    if(current == 0):
        count += 1

print(count)

