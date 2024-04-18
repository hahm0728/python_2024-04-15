# demoform.ui : 화면구성, demoform.py : 로직단

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from bs4 import BeautifulSoup
import requests
import time

form_class = uic.loadUiType("demoForm2.ui")[0]

# print(form_class)

class Demoform(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("버튼 클릭 데모")
    def firstClick(self):
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

            # print(f"{title},{price},{addr}")
            #time.sleep(3)
            f.write(f"{title},{price},{addr}\n")
        f.close()
        self.label.setText(f"{title},{price},{addr}\n")

    def secondClick(self):
        self.label.setText("두 번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세 번째 버튼을 클릭")
    def init(self):
        self.label.setText("버튼 클릭 데모")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoform = Demoform()
    demoform.show()
    app.exec_()




