# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
# 해당 사이트 관리자가 웹봇 차단 로직 적용했을 때, 회피 목적

resultA=[]
resultB=[]

for n in range(1,2):
        url ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' \
            + str(n)
        # print(url)
        req = urllib.request.Request(url, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()

        soup = BeautifulSoup(data, 'html.parser')
        # <tr class="view list_tr_humordata" mn="63095">
        #             <td class="no"><a href="/board/view.php?table=bestofbest&amp;no=454510&amp;s_no=454510&amp;no_tag=1&amp;kind=search&amp;search_table_name=bestofbest&amp;page=1&amp;keyfield=subject&amp;keyword=%EC%8A%A4%ED%8E%98%EC%9D%B8" target="_top" style="color:#444;font-size:10px;font-family:Tahoma">454510</a></td>
        #             <td class="icon"><a href="list.php?kind=bestofbest_sort&amp;o_table=humordata"><div class="board_icon_mini humordata" style="background-image: url(&quot;//www.todayhumor.co.kr/board/images/icon_sprites.png?7923243&quot;);"></div></a></td>
        #             <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=454510&amp;s_no=454510&amp;kind=search&amp;search_table_name=bestofbest&amp;page=1&amp;keyfield=subject&amp;keyword=%EC%8A%A4%ED%8E%98%EC%9D%B8" target="_top">스페인 승무원이 본 한국승객 특징</a><span class="list_memo_count_span"> [2]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> </td>
        #             <td class="name"><a href="list.php?kind=member&amp;mn=63095" target="_blank" class="list_name_member">눈물한스푼</a></td>
        #             <td class="date">22/04/27 20:15</td>
        #             <td class="hits">12834</td>
        #             <td class="oknok">148</td>
        #         </tr>

        list = soup.find_all('td', attrs={'class':'no'})

        for item in list:
            try: # 자료가 넘어올때 에러 발생하면 pass 목적
                titleNo = item.find("a").text.strip()
                resultA.append(titleNo)
            except:
                pass

        list2 = soup.find_all('td', attrs={'class':'name'})

        for item in list2:
            try: # 자료가 넘어올때 에러 발생하면 pass 목적
                title = item.find("a").text.strip()
                resultB.append(title)
                
            except:
                pass

for i in range(0, len(resultA)):
     print(resultA[i], resultB[i])






