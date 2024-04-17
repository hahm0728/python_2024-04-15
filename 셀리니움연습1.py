from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.naver.com")
# driver.get("https://www.google.co.kr")

time.sleep(3)

searchBox = driver.find_element(By.CLASS_NAME, "search_input_box")
searchBox.send_keys("맥북")
searchBox.send_keys(Keys.ENTER)

time.sleep(10)

# <div class="search_input_box"> <input id="query" name="query" type="search" title="검색어를 입력해 주세요." placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" class="search_input" data-atcmp-element=""> </div>

# <textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="검색" value="" jsaction="paste:puy29d;" aria-label="검색" aria-autocomplete="both" aria-expanded="true" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" id="APjFqb" maxlength="2048" name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwj-3PuezciFAxV9s1YBHd-_CJAQ39UDCA4" aria-activedescendant="" style=""></textarea>