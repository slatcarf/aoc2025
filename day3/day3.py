

def get_largest_pair(battery):
    largest_index = 0
    sec_largest_index = 1
    for index, j_str in enumerate(battery.strip()):
        largest_joltage = int(battery[largest_index])
        sec_largest_joltage = int(battery[sec_largest_index])
        joltage = int(j_str)
        
        if joltage > largest_joltage and index < len(battery) - 2:
            largest_index = index
            sec_largest_index = index + 1
        if(index > largest_index and joltage > sec_largest_joltage):
            sec_largest_index = index
        
    return int(battery[largest_index] + battery[sec_largest_index])
  

#123912
file = open('input')

sum = 0;
for line in file:
    if(line == '\n'):
        break
    sum += get_largest_pair(line)
print(sum)
    
    
   
    
