f = open("input.txt")


    


current = 50;
count = 0;

def turn_dial(direction, amount):
  global current
  global count
  for i in range(0, amount):
    if(direction == "R"):
        current = (current + 1) % 100
    elif(direction == "L"):
        current = (current - 1) % 100
    if(current == 0):
        count += 1

for line in f:
    if(line == "\n"):
       break
    stripped = line.strip()
    direction = stripped[0]
    amount = stripped[1:]
    turn_dial(direction, int(amount))

  

print(count)

