# Why are waits required:
# All elements on a web page may not load at the same time. Required for websites using Ajax and Javascript.
# To avoid ElementNotVisible exception from Selenium.
# Selenium web driver has 2 types of waits:
# Implicit - poll the DOM for a specific duration to locate an element 500ms until timeout 10 sec -
# Explicit - waits for a certain condition to occur before proceeding with next step

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
# Implicit Waits
# driver.implicitly_wait(10)

driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation")
wait = WebDriverWait(driver, 10)

try:
    element = wait.until(EC.element_to_be_clickable((By.NAME,"btnK1")))
    print("element is clickable")
except TimeoutException:
    print("element is not clickable")
    exit(1)

element.click()

# driver.find_element_by_name("btnK").click()
print("Test Completed")
driver.close()
driver.quit()
