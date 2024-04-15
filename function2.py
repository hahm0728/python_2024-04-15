# 가변인자 처리

def union(*ar):
    result =[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union('ham','spam'))
print(union('hahm','spam','egg'))

# 2번째 커밋 테스트
