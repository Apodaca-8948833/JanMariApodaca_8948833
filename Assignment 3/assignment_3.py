# Selenium test script to open: Pixel 8 Pro pre-order page

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Opening google.com site
driver.get("https://www.google.com")
time.sleep(1)

# Clicking store button
store_button = driver.find_element("xpath","/html/body/div[1]/div[1]/a[2]")
store_button.click();
time.sleep(2)

# Clicking the search button
search_button = driver.find_element("xpath","/html/body/c-wiz[1]/div/div[2]/div[2]/div/div/div[1]/div")
search_button.click();
time.sleep(2)

# Inputting data in search bar
search_bar = driver.find_element("xpath","/html/body/c-wiz[1]/div/div[2]/div[2]/div/c-wiz[2]/div/div/div[1]/label/input")
search_bar.send_keys("pixel 8 pro")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# Clicking the item to order
pixel8Pro_image = driver.find_element("xpath","/html/body/c-wiz[2]/c-wiz/div/div/main/div/section[2]/div/div[1]/span")
pixel8Pro_image.click();
time.sleep(5)

# Clicking the pre-order button
preOrder_button = driver.find_element("xpath","/html/body/c-wiz[2]/c-wiz/div/div/main/div[1]/div/c-wiz[1]/div/div[3]/div/div[2]/div[2]/button")
preOrder_button.click();
time.sleep(5)

# Closing the webdriver
driver.close()