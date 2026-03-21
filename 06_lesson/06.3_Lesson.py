from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

src = driver.find_element(By.CSS_SELECTOR,"#award")

print(src.get_attribute("src"))

driver.quit()

# Вариант №2

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape")))

# third_image = driver.find_element(By.CSS_SELECTOR, "#award")
 
# src = third_image.get_attribute("src")
    
# print(src)

# driver.quit()