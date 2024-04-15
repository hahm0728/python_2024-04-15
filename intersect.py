def intersect(prelist, postlist):
    result=[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect('ham','spam'))

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server, port):
    strURL="https://"+server+":"+port
    return strURL

print(connectURI("multi.com", "80"))
print(connectURI(port="80", server="test.com"))
