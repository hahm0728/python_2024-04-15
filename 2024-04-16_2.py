
data = "  spam and ham   "
result = data.strip()
print(data)
print(result)
result=result.replace("spam","spam egg")
print(result)
print(result.split())
result2=":)".join(result)
print(result2)

import re

result =re.search("[0-9]*th1", "35th")
if result:
    print(result.group())
else:
    print('error')

result =re.search("/d[5]", "올해는 2024년 입니다.")
if result:
    print(result.group())
else:
    print('error')




