import sys
import threading
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import *
from PyQt5 import uic
from bs4 import BeautifulSoup
import requests
import time

# Load UI file
form_class = uic.loadUiType("demoForm2.ui")[0]

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

    def scrape_website(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.find_all("div", attrs={"class": "card-desc"})
        for post in posts:
            title_elem = post.find("h2", attrs={"class": "card-title"}).text.strip()
            price_elem = post.find("div", attrs={"class": "card-price"}).text.strip()
            addr_elem = post.find("div", attrs={"class": "card-region-name"}).text.strip()
            message = f"{title_elem},{price_elem},{addr_elem}"
            self.progress.emit(message)
            time.sleep(3)
        self.finished.emit()

class Demoform(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("버튼 클릭 데모")
        self.worker = None

    def firstClick(self):
        self.worker = Worker()
        self.worker.finished.connect(self.on_worker_finished)
        self.worker.progress.connect(self.on_worker_progress)
        thread = threading.Thread(target=self.worker.scrape_website)
        thread.start()

    def on_worker_progress(self, message):
        self.label.setText(message)

    def on_worker_finished(self):
        self.label.setText("작업 완료")

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
    sys.exit(app.exec_())
