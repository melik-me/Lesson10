from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('http://127.0.0.1/oxwall/')
driver.find_element_by_class_name("ow_signin_label").click()
el = driver.find_element_by_name("identity").send_keys("admin\tpass\n")

driver.find_element_by_name("status").send_keys("Success! Again!")
driver.find_element_by_name("save").click()
driver.get("http://127.0.0.1/oxwall/sign-out")

sleep(10)
driver.quit()