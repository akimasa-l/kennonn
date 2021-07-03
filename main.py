from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
url=f"https://docs.google.com/forms/d/e/1FAIpQLSco7LzMebv1ctlOFOvWOZEkd7XAzeNt85bfXawibNDr52ZBNg/viewform?usp=pp_url&entry.704563200=なしおたかし&entry.925303296={random.randint(360,365)/10}"

driver.get(url)
username="61229liu@seiko.ac.jp"
with open("./password.txt") as f:
    password = f.read()
email=driver.find_element_by_css_selector("#identifierId")
email.send_keys(username)
email.send_keys(Keys.ENTER)
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"input[name=\"password\"]")))
password_element=driver.find_element_by_css_selector("input[name=\"password\"]")
password_element.send_keys(password)
password_element.send_keys(Keys.ENTER)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.freebirdFormviewerViewHeaderEmailAddress")))#読み込まれるまで待つ
send_button=driver.find_element_by_css_selector("div[role=\"button\"]")
send_button.click()

driver.close
driver.quit
