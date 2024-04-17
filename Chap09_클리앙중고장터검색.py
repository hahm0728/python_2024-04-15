#Chap09_클리앙중고장터검색.py
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

for n in range(0,100):
        #클리앙의 중고장터 주소 
        url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # # <span class="subject_fixed" data-role="list-title-text" title="맥북프로 M2 13인치 24/512 실버">
		# # 		맥북프로 M2 13인치 24/512 실버
		# # </span>
        for item in list:
            title = item.text.strip()

            if re.search("아이패드", title):
                  print(title)




# <span class="subject_fixed" data-role="list-title-text" title="아이패드 프로 12.9인치 4세대 256 wifi 스페이스 그레이">
# 							아이패드 프로 12.9인치 4세대 256 wifi 스페이스 그레이
# 						</span>