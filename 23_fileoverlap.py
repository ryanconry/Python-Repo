def get_lists(file):
    nums=[]
    with open(file, 'r') as file:
        line=file.readline()
        while line:
            line=line.strip('\n')
            nums.append(line)
            line=file.readline()
        return nums

file1='primenumbers.txt'
file2='happynumbers.txt'

prime=get_lists(file1)
happy=get_lists(file2)

same=[]
for x in prime:
    if x in happy:
        same.append(x)

print(same)
