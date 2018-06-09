import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://novaposhta.ua')
el = driver.find_element_by_class_name("logo_in")

# list = driver.find_elements_by_partial_link_text("tutorial")
# print(len(list))
action = webdriver.ActionChains(driver)
action.key_down(Keys.CONTROL)
action.click(el)
action.key_down(Keys.CONTROL)
action.perform()

all_windows  = driver.window_handles
this_window = driver.current_window_handle
print(all_windows)
print(this_window)
driver.switch_to.window(all_windows[1])