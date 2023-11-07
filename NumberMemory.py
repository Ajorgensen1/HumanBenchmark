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
import re

# setting options to not have annoying warnings
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initializing and starting webdriver
driver = webdriver.Chrome(options=options)
driver.get("https://humanbenchmark.com/login")
driver.implicitly_wait(2)

# Initializing username and password (change to whatever your username and password are)
username = "username"
password = "password"

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

# Navigate to number memory game
verbal = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='Number Memory']"))
)
verbal.click()

# More navigation
play = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[@href='/tests/number-memory']"))
)
play.click()

# Start number memory game
start = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Start')]"))
)
start.click()

while True:
    # Update page source with new number
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    # Locate number
    number = soup.find('div', class_='big-number')
    # Wait until soup cannot find timer bar (This means timer bar has concluded and input box is present)
    while soup.find('div', class_='number-timer-bar'):
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

    # Type in number and submit
    submitBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    submitButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Submit')]"))
    )
    submitBox.click()
    submitBox.send_keys(number)
    submitButton.click()
    time.sleep(1)
    # Continue to next number
    next = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'NEXT')]"))
    )
    next.click()


