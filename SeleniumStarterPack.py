#essential libraries and effective tools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#declaration/setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

#functions
driver.get("https://www.messenger.com")
wait.until(EC.presence_of_element_located(By.XPATH()))
driver.find_element_by_xpath().click()

driver.quit()


