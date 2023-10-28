from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

# setting options to not have annoying warnings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initializing and starting webdriver
driver = webdriver.Chrome(options=options)
driver.get("https://humanbenchmark.com/login")
driver.implicitly_wait(2)

# Initializing username and password (change to whatever your username and password are)
username = "TheBandit"
password = "D4rkmatter!"

# Input username
usernameInput = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
usernameInput.send_keys(username)

# Input password
passwordInput = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
passwordInput.send_keys(password)

# Click login
loginButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@value='Login']"))
)
loginButton.click()

# Navigate to verbal memory game
verbal = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='Typing']"))
)
verbal.click()

# More navigation
play = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/tests/typing']"))
)
play.click()

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
spans = soup.find_all('span', class_='incomplete')
text_to_type = ''.join([span.get_text() for span in spans])
time.sleep(2)
pyautogui.write(text_to_type, interval=0)


time.sleep(10)
