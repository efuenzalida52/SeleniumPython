from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

driver.get("https://google.com")

# orangeHRM  demo website
# sample html document w3

# FIND ELEMENTS IN THIS ORDER
driver.find_element_by_id()

searchBox = driver.find_element_by_name()
searchBox.send_keys('Elizabeth Fuenzalida')
# driver.find_element_by_class_name()
# driver.find_elements_by_css_selector()
# driver.find_element_by_tag_name()
# driver.find_element_by_link_text()
# driver.find_element_by_partial_link_text()
# driver.find_element_by_xpath()

# driver.find_elements_by_id()
# driver.find_elements_by_name()
# driver.find_element_by_class_name()
# driver.find_elements_by_css_selector()
# driver.find_elements_by_tag_name()
# driver.find_elements_by_link_text()
# driver.find_elements_by_partial_link_text()

# xpath tutorial on w3schools
# driver.find_elements_by_xpath()
