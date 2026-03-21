from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

search_input = driver.find_element(By.CSS_SELECTOR, "input#username")
search_input.send_keys("tomsmith") 
print("✅ Username: tomsmith")
sleep(2)

search_input = driver.find_element(By.CSS_SELECTOR, "input#password")
search_input.send_keys("SuperSecretPassword!") 
print("✅ Password: SuperSecretPassword!")
sleep(2)

search_input = driver.find_element(By.CSS_SELECTOR, "i")
search_input.click()
sleep(2)

driver.quit()
print("✅ Браузер закрыт")