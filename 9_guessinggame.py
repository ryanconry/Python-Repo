import random
while True:
    num=random.randint(1,9)

    while True:
        guess=input('enter your guess or quit\n')
        if guess=='quit':
            break
        else:
            guess=int(guess)
            if guess==num:
                    print('right')
                    break
            else:
                    print('wrong')

    play=input('Type "y" to play or "n" to quit\n')
    if play=='n':
        print('goodbye')
        break

               
                    
