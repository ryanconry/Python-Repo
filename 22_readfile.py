counter_dict={}
with open('nameslist.txt') as file:
    line=file.readline()

    while line:
        
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line=file.readline

print(counter_dict)
        
