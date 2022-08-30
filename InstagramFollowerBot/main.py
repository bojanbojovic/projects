import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

chrome_driver = "/home/bojan/Downloads/chromedriver_linux64/chromedriver"
SIMILAR_ACCOUNT = "businessinsider"
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

s = Service(chrome_driver)
browser = webdriver.Chrome(service=s)

browser.get("https://www.instagram.com/")
time.sleep(5)
username = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
username.send_keys(USERNAME)
password = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
password.send_keys(PASSWORD)
login = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div')
login.click()
time.sleep(5)
search = browser.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(SIMILAR_ACCOUNT)
time.sleep(3)
bi = browser.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
bi.click()
time.sleep(10)
following = browser.find_elements(By.CSS_SELECTOR, 'a[href*="businessinsider"')[1]
following.click()
time.sleep(5)
listOfFollowing = browser.find_element(By.CLASS_NAME, "_aano")

i = 3
while True:
    try:
        followButton = browser.find_element(By.XPATH, f"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{i}]/div/div[2]/button")
        if followButton.text == "Follow":
            followButton.click()
            time.sleep(1)
    except NoSuchElementException:
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", listOfFollowing)
        time.sleep(8)

    i += 1
    if i > 20:
        break
    

browser.quit()
