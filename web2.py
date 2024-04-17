
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

url = "https://www.daangn.com/fleamarket/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

f = open("daangn.txt","wt", encoding="utf-8")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2",attrs={"class":"card-title"})
    title = titleElem.text.strip()
    priceElem = post.find("div",attrs={"class":"card-price"})
    price = priceElem.text.strip()
    addrElem = post.find("div",attrs={"class":"card-region-name"})
    addr = addrElem.text.strip()

    print(f"{title},{price},{addr}")
    f.write(f"{title},{price},{addr}\n")

f.close()




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











