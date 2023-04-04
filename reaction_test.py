from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Safari()


driver.get("https://humanbenchmark.com/tests/reactiontime")

react = driver.find_element(By.TAG_NAME, "h1")
if react.text == "Reaction Time Test":
    react.click()

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.1)


for i in range(5):
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'Click'))
    driver.find_element(By.TAG_NAME, "h1").click()

    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'ms'))
    driver.find_element(By.TAG_NAME, "h1").click()


time.sleep(15)
driver.quit()
