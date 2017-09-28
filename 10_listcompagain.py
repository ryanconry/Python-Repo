import random

a = [random.sample(range(1,30), 15)]
b = [random.sample(range(1,30), 12)]

print(a,'\n',b,'\n')

print([comm for comm in b if comm in a])
