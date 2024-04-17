
from bs4 import BeautifulSoup

# file loading
page = open("c:\\work\\Chap09_test.html","rt", encoding="UTF-8").read()

# parsing
soup = BeautifulSoup(page, "html.parser")

# print(soup)
# print(soup.prettify())

# print(soup.prettify().find_all("p"))

# print(soup.find("p"))

# print(soup.find_all("p", class_="outer-text"))

# print(soup.find_all("p", attrs={"wang":"inner-text"}))

# print(soup.find_all(wang="inner-text"))

for tag in soup.find_all("p"):
    title = tag.text.strip()
    # title = title.replace("\n","")
    print(title)

# print(soup.find_all("p"))











