# -*- coding: utf-8 -*-


#import
from selenium import webdriver
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


#Chromedriver
path = "ur_Chromedriver"
driver = webdriver.Chrome(path)

#Pop Up notification
option = Options()
driver = webdriver.Chrome(
    chrome_options=option, executable_path=path)

#url
driver.get("https://www.facebook.com/")

#cookies page ???
time.sleep(3)
yes1 = driver.find_element(By.XPATH, '//*[@title="Only allow essential cookies"]').click()

#cookies.load
"""
#export_cookies
driver = selenium.webdriver.Firefox()
driver.get("http://www.google.com")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

"""
#import_cookies
time.sleep(3)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(3)

#redirection
driver.get("https://www.facebook.com/")

#login
def login(id,password):
 email = driver.find_element_by_id("email")
 email.send_keys(id)
 Password = driver.find_element_by_id("pass")
 Password.send_keys(password)
 butto = driver.find_element(By.XPATH, '//*[@data-testid="royal_login_button"]').click()
 pass
login("ur_email","ur_password")

#the group pending_posts

Declinetxt  = "ur_txt"

time.sleep(5)
driver.get("pending_posts_page")


time.sleep(5)
list = driver.find_element(By.XPATH, '//*[@aria-label="More post approval actions"]').click()
time.sleep(5)
Decline = driver.find_element(By.XPATH, '(//div[@role="menuitem"])[2]').click()
time.sleep(5)
txt = driver.find_element(By.XPATH, '//*[@aria-label="Additional notes from the admins (optional)"]').send_keys(Declinetxt)
time.sleep(5)
Confirm = driver.find_element(By.XPATH, '//div[@aria-label="Confirm"]').click()
time.sleep(5)

driver.quit()
