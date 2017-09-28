def compare(nums,guess):
    new_nums=[]
    for x in nums:
        if x < guess:
            new_nums.append(x)
    print(new_nums)



nums=[1,3,5,9,16,24,35,39,42,44,67]

if __name__=="__main__":
    guess=int(input('guess a number in the list'))
    result=compare(nums,guess)
    
