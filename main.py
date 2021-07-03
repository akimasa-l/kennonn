from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
url="https://docs.google.com/forms/d/e/1FAIpQLSco7LzMebv1ctlOFOvWOZEkd7XAzeNt85bfXawibNDr52ZBNg/viewform"
driver.get(url)
username="61229liu@seiko.ac.jp"
with open("./password.txt") as f:
    password = f.read()
email=driver.find_element_by_css_selector("#identifierId")
email.send_keys(username)
email.send_keys(Keys.ENTER)
password_element=driver.find_element_by_name("password")
password_element.send_keys(password)
email.send_keys(Keys.ENTER)
element=driver.find_element_by_css_selector("input")
element.send_keys(Keys.TAB)
element.send_keys(Keys.TAB)
element.send_keys("なしおたかし")
