strA="python is very powerful"
strB="파이썬은 단순해"

print(len(strA))
print(len(strB))
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strA[-1])
print(strA[-3:])

print("---list형식---")
lst=[1,2,3]
lst.append(4)
print(lst)
colors=['red','blue','green']
colors.append('white')
colors.insert(1,'pink')
print(colors)
colors.remove('red')
print(colors)
colors.sort()
print(colors)
colors.reverse()

print("---set형식---")
a={1,2,3,3}
b={3,4,4,5}
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---tuple---")
tp=(10,20,30)
print(tp)

def calc(a,b):
    return a+b, a*b

result =calc(3,4)
print(result)
print("id: %s, nave: %s"%('kim','김유신'))
tp2=(5,6)
print(calc(*(5,6)))


#print("---형식변환---")
#a=set((1,2,3))
#print(a)
#b=list(a)
#b.append(4)
#print(b)












