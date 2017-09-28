def divide(num):
    x=list(range(1,101))
    ans=[]
    for denom in x:
        if num%denom==0:
            ans.append(denom)
    return ans


num=int(input('Please enter a number to check if it\'s prime\n'))

ans=divide(num)
if len(ans)==0:
        print('This number is a prime number')
else:
        print(ans,' divide into the number provided')
