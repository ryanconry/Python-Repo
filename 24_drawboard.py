horiz_st=' ---'
vert_st='|   '
vert_end='|'
horiz=''
vert=''
size=3

for i in range(size):
   horiz+=horiz_st
   vert+=vert_st
   if i==size-1:
       vert+='|'

for i in range(size):
    print(horiz)
    print(vert)
    if i==size-1:
        print(horiz)
  

        

