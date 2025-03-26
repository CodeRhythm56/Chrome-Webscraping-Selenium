#essential libraries and effective tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#declaration/setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver)

#functions
driver.get("https://www.messenger.com")
driver.find_element_by_xpath().click()
wait.until(EC.presence_of_element_located(By.XPATH()))


driver.quit()


