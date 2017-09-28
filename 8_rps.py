
while True:
    p1=input('player 1 enter choice\n')
    p2=input('player 2 enter choice\n')
    p1=str(p1)
    p2=str(p2)

    if p1=='rock':
        if p2=='scissors':
            print('p1 wins')
        elif p2=='paper':
            print('p2 wins')
        else:
            print('draw')

    if p1=='scissors':
        if p2=='paper':
            print('p1 wins')
        elif p2=='rock':
            print('p2 wins')
        else:
            print('draw')

    if p1=='paper':
        if p2=='rock':
            print('p1 wins')
        elif p2=='scissors':
            print('p2 wins')
        else:
            print('draw')

    play=input('would you like to play again?\n')
    if play=='no':
        break


    

