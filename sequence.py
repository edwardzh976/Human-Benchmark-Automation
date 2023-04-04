from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()

driver.get("https://humanbenchmark.com/tests/sequence")
# click start
driver.find_element(By.XPATH, "//*[contains(text(),'Start')]").click()

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.001)

count = 1
while True:
    element = []
    for j in range(count):
        time.sleep(0.5)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "square.active")))
        element.append(driver.find_element(By.CLASS_NAME, "square.active"))

    time.sleep(2)
    for x in range(count):
        time.sleep(0.1)
        element[x].click()
    count += 1


time.sleep(4)
driver.quit()