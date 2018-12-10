from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
# firefox_options.set_headless(headless=True)

ffpath = "../drivers/geckodriver.exe"
driver = webdriver.Firefox(executable_path=ffpath, firefox_options=firefox_options)
driver.set_page_load_timeout(10)
driver.get("https://google.com")

print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(2)

driver.close()
driver.quit()

# reference selenium firefox options list
