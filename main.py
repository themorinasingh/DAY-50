#TODO import libraries
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url= "https://tinder.com/"

#TODO setup the driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

#Todo click login button
time.sleep(3)
login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()

#todo sign in via fb
time.sleep(3)
sign_in = driver.find_element(By.XPATH, value='//*[@id="q-699262256"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
sign_in.click()

#handling windows
time.sleep(3)
base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)

#enter login info
time.sleep(5)
login_input = driver.find_element(By.XPATH, value='//*[@id="email"]')
login_input.send_keys('5062694986')

password_input = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password_input.send_keys("Lumia920$")
password_input.send_keys(Keys.ENTER)

time.sleep(4)
continue_as = driver.find_element(By.CSS_SELECTOR, value= "[aria-label='Continue as Singh']")
continue_as.click()

#switching back to tinder
time.sleep(10)
driver.switch_to.window(base_window)

time.sleep(25)
#clicking the location, cookies and notifications
location_button = driver.find_element(By.XPATH, value='//*[@id="q-699262256"]/div/div/div/div/div[3]/button[1]/div[2]/div[2]')
location_button.click()
notification_button = driver.find_element(By.XPATH, value='//*[@id="q-699262256"]/div/div/div/div/div[3]/button[2]/div[2]/div[2]')
notification_button.click()
cookie_button = driver.find_element(By.XPATH, value='//*[@id="q1029118820"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookie_button.click()

#todo swiping left
for i in range(10):
    time.sleep(2)
    swipe_left_button = driver.find_element(By.CSS_SELECTOR,value="[class = 'gamepad-2nd-icon-wrapper']")
    swipe_left_button.click()
