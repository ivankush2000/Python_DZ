from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button = "button.btn.btn-primary"
press = driver.find_element(By.CSS_SELECTOR, button)
press.click()

sleep(4)