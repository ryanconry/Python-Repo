num=int(input('provide number \n'))
mod=num%4
if mod!=0:
    print('this number is not divisible by four')
else:
    print('this number is divisible by four')
    
if mod==0 or mod==2:
    print('this number is an even number')
elif mod==1 or mod==3:
    print('this is an odd number')
