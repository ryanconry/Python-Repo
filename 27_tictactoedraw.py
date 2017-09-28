def update(game,move,player):
    
    if player==1:
        game[move[0]][move[1]]='X'
    elif player==2:
        game[move[0]][move[1]]='O'
    print(game[0],'\n',game[1],'\n',game[2])
    return game


game=[['-','-','-'],
      ['-','-','-'],
      ['-','-','-']]
player=1
turn=1
while True:         
    print('Player',player,' enter co-ordinates for move (row,column)')
    move=input()
    move=move.split(',')
    move=[int(x)-1 for x in move]
    if game[move[0]][move[1]]=='X' or game[move[0]][move[1]]=='O':
        print('space occupied, please try again')
    else:
        turn+=1
        game=update(game,move,player)
        if player==1:
            player=2
        else:
            player=1
    if turn==10:
        break

print('game over')
    
