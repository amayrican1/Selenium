from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#def lambda_handler(event=None, context=None):

# initiate drivers
chrome_options = Options()
driver = webdriver.Remote('http://selenium:4444/wd/hub', options=chrome_options)
driver.maximize_window()

# browse website and take a screenshot
driver.get("https://google.com")
searchbar = driver.find_element(By.NAME, "q")
searchbar.clear()
searchbar.send_keys("Selenium")
searchbar.send_keys(Keys.RETURN)
driver.save_screenshot('screenshot.png')
print(driver.title)

# exit driver
driver.quit()
