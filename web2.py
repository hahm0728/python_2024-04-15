
# <div class="card-photo ">
#         <img alt="다이슨 선풍기" src="https://dnvefa72aowie.cloudfront.net/origin/article/202404/487e6fb1767768a4fea7f3b3fc86184ba7701a908f68ec835a7fc6aedb2c8d03.jpg?f=webp&amp;q=82&amp;s=300x300&amp;t=crop" />
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">다이슨 선풍기</h2>
#       <div class="card-price ">
#         50,000원
#       </div>
#       <div class="card-region-name">
#         경기도 성남시 분당구 백현동
#       </div>

from bs4 import BeautifulSoup
import requests

url = "https://learningspoons.com/course/detail/pythonforfinance/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")


posts = soup.find_all("div", attrs={"class":"accordion-title"})
# posts = soup.find_all("div", attrs={"class":"flex flex-justify-between"})

# print(posts)

for post in posts:
    try:
        title = post.find("p").text.strip()
        print(title)
    except:
        pass 

    subPost = post.find_all("li", attrs={"class":"flex flex-justify-between"})
    for item in subPost:
        title2 = item.find("strong").text.strip()
        print("---", title2 )
        # <div class="flex flex-justify-between">
        #                                 <div class="">
                                            
        #                                     <p><strong>1-0. Intro 과정소개</strong></p>
                                            
        #                                 </div>
        #                                 <div class="details">
                                            
        #                                     <span>00:04:05</span>
                                            
        #                                 </div>
        #                             </div>
        # # <li class="accordion-item active">
        #                         <div class="accordion-title">
        #                             <p>SECTION 7. 파이썬을 활용한 금융 데이터 수집 및 분석</p>
                                    
        #                                 <div class="details">
        #                                     <span>12:15:22</span>
        #                                 </div>
                                    
        #                         </div>
                            
                                

    #
    # priceElem = post.find("div",attrs={"class":"accordion-title"})
    # price = priceElem.text.strip()

    # print(f"{price}")
    # print(f"{title},{price},{addr}")


# file loading
# page = open("https://www.daangn.com/fleamarket/","rt", encoding="UTF-8").read()

# parsing
# soup = BeautifulSoup(page, "html.parser")

# print(soup)
# print(soup.prettify())

# print(soup.prettify().find_all("p"))

# print(soup.find("p"))

# print(soup.find_all("p", class_="outer-text"))

# print(soup.find_all("p", attrs={"wang":"inner-text"}))

# print(soup.find_all(wang="inner-text"))

# for tag in soup.find_all("p"):
#     title = tag.text.strip()
#     # title = title.replace("\n","")
#     print(title)

# print(soup.find_all("p"))











