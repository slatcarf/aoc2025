file = open('input')


file_arr = list(map(list,file.readlines()))
line_len = len(file_arr[0])

def get_surrounding_count(i,j):
    surrounding_count = 0
    
    for x in range(i if i == 0 else i - 1,i+1 if i == len(file_arr) - 1 else i + 2):
        for y in range(j if j == 0 else j - 1,j+1 if j == line_len - 1 else j + 2):
            # skip counting the inspected roll itself
            if(x == i and y == j):
                continue

            if file_arr[x][y] == '@':
                surrounding_count += 1
     
    return surrounding_count



count = 0
last_count = 0
while(True):
    for i, line in enumerate(file_arr):
        for j, slot in enumerate(line):
            surrounding_count = get_surrounding_count(i, j)
            # print(slot,surrounding_count)
            if surrounding_count < 4 and slot == '@':
                count += 1
                file_arr[i][j] = 'x'
    if(last_count == count):
        break
    last_count = count

print(file_arr)

print(count)
                
            
            
