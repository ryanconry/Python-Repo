import random

num=str(random.randint(1,10000))
print(num)

while True:
    guess=input("make a guess\n")
    if len(guess)==4:
        break
    print('must be 4 digits in length\n')

c=0

for i in guess:
    if i in num:
        print('guess in number')
    else:
        print('guess not in number')

