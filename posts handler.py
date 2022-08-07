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


for i in range(50):
    time.sleep(2)
    list2 = driver.find_element_by_xpath('//*[@aria-label="More post approval actions"]')
    driver.execute_script("arguments[0].click();", list2)
    time.sleep(2)
    Decline = driver.find_element(By.XPATH, '(//div[@role="menuitem"])[2]').click()
    time.sleep(2)
    txt = driver.find_element(By.XPATH, '//*[@aria-label="Additional notes from the admins (optional)"]').send_keys(
        Declinetxt)
    time.sleep(2)
    DeclineConfirm = driver.find_element_by_xpath ( '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/div').click()
    #   time.sleep(2)
    # driver.get("https://www.facebook.com/groups/428118924043465/pending_posts")


driver.quit()
