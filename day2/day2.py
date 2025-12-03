file = open('input')

count = 0
for r in file.read().split(','):
    [start,end] = r.split("-")

    for i in range(int(start),int(end) + 1):
        if len(str(i)) % 2 != 0:
          continue
        if str(i)[:len(str(i))//2] == str(i)[(len(str(i))//2):]:
            count += i
print(count)

