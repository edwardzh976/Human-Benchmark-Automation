from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
driver.get("https://humanbenchmark.com/tests/chimp")

# click start
driver.find_element(By.XPATH, "//*[contains(text(),'Start')]").click()

while True:
    #find all elements and map them to their text number
    elements = driver.find_elements(By.CLASS_NAME, "css-19b5rdt")
    element_dict = {}
    for element in elements:
        index = element.text
        element_dict[index] = element

    for i in range(1, len(element_dict) + 1):
        time.sleep(0.1)
        element_dict[str(i)].click()

    # click continue
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'css-de05nr').click()