# today key man: ctrl + / -> comment
# 필터함수 연습

def getBiggerThan20(i):
    return i>20

l=[10,25,30]

iterL=filter(None, l)

for i in iterL:
    print("Item:{0}".format(i))

# iterL=filter(getBiggerThan20,l)
# for i in iterL:
#     print("Item:{0}".format(i))

iterL=filter(lambda x:x>20,l)
for i in iterL:
    print("Item:{0}".format(i))

          
