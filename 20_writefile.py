

if __name__=="__main__":
    text="i'm writing to a file!"
    with open('filesave.txt','w') as filevar:
        filevar.write(text)
    
