import time
from selenium import webdriver

driver = webdriver.Chrome("../drivers/chromedriver.exe")

# 10 seconds
driver.set_page_load_timeout(10)

driver.get("https://google.com")

# go to site, inspect element to find name
# send_keys acts as keyboard.In this instance, types given string into given textbox
driver.find_element_by_name("q").send_keys("Automation step by step")

# simulates button click
driver.find_element_by_name("btnK").click()

time.sleep(7)

# closes browser/driver
driver.close()
driver.quit()

print("Test has been completed")
