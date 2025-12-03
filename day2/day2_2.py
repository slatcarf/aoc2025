file = open('input')

def is_valid(id):
    id_str = str(id)
    l = len(id_str)
    valid = False
    
    for i in range(1,(l // 2) + 1):
        if l % i != 0:
            continue
        chunk = id_str[:i]
        mul = l // i
        if chunk * mul == id_str:
            valid = True
    return valid
    




count = 0
for r in file.read().split(','):
    [start,end] = r.split("-")

    for i in range(int(start),int(end) + 1):
        if is_valid(i):
            print(i)
            count += i
print(count)

