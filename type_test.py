from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Safari()

driver.get("https://humanbenchmark.com/tests/typing")
text = driver.find_element(By.CLASS_NAME, "letters")

Input = driver.find_element(By.CLASS_NAME, "letters")

for letter in text.text:
    time.sleep(0.025)
    Input.send_keys(letter)

time.sleep(15)
driver.quit()