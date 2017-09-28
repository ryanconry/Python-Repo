game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
r1=game[0]
r2=game[1]
r3=game[2]
done=False
for i in range(3):
   if r1[i]!=0:
        if i==0:
           if r1[i]==r1[i+1]==r3[i] or r1[i]==r2[i]==r3[i] or r1[i]==r2[i+1]==r3[i+2]:
               winner=r1[i]
               done=True
        elif i==1:
            if r1[i]==r2[i]==r3[i]:
                winner=r1[i]
                done=True
        elif i==2:
            if r1[i]==r2[i]==r3[i] or r1[i]==r2[i-1]==r3[i-2]:
                winner=r1[i]
                done=True
        
if done==False:
    print('no winner')
else:
    print('Player',winner,'wins')
