# function1.py

# 1) 함수 정의

def setValue(newValue):
    x=newValue
    print("지역변수: ", x)

# 2) 호출

retValue=setValue(5)
print(retValue)

# tuple return
def swap(x,y):
    return y,x
# call
print(swap(*(3,4)))



