# NOTE HEADLESS MEANS NOTHING APPEARS ON YOUR SCREEN! AKA does not show itself opening chrome
import time
from selenium import webdriver
# OPTION 1 for headless chrome testing:
from selenium.webdriver.chrome.options import Options

# OPTION 2  for headless is getting rid of Options import and having chrome_options variable equal to:
# webdriver.ChromeOptions()
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")

# some test require you to disable extensions
# chrome_options.add_argument(" -- disable-extensions")

driver = webdriver.Chrome(options=chrome_options, executable_path="../drivers/chromedriver.exe")
driver.implicitly_wait(13)
driver.get("https://google.com")

print(driver.title)
driver.find_element_by_name("q").send_keys("Automation step by step")
# time.sleep(12)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
print(driver.title)

driver.close()
driver.quit()
print("complete!")
# Reference list: http://www.assertselenium.com/java/list-of-chrome-driver-command-line-arguments/

