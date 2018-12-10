from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys

capa = webdriver.DesiredCapabilities.INTERNETEXPLORER
# desired capabilities in selenium
capa['ignoreProtectedModeSettings']= True

IEpath = "../drivers/IEDriverServer.exe"
driver = webdriver.Ie(executable_path=IEpath, desired_capabilities=capa)

driver.get("https://google.com")

driver.find_element_by_name("q").send_keys("Abcd")
driver.find_element_by_name("btnK").click()

driver.quit()
print("Completed Demo Test")
