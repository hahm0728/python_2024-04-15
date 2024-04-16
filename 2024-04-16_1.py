# today key man: ctrl + / -> comment

def getBiggerThan20(i):
    return i>20

l=[10,25,30]

iterL=filter(None, l)

for i in iterL:
    print("Item:{0}".format(i))

iterL=filter(getBiggerThan20,l)
for i in iterL:
    print("Item:{0}".format(i))
    
          
