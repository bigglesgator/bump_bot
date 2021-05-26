from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import unittest
from random import randint
from time import sleep

#Login Info
my_username = "REPLACE
my_password = "REPLACE"
activity_thread = ("https://www.myth-weavers.com/showthread.php?t=439977")

# Initiate the browser
driver  = webdriver.Chrome(ChromeDriverManager().install())
#Maximizes window
driver.maximize_window()
#Small delay to allow window to resize
time.sleep(1)
# Open the Website
driver.get("https://www.myth-weavers.com/showthread.php?t=439977")

def bump_process():
    #Clicks Login button in top right
    login_button = driver.find_element_by_xpath("//*[@id='login_register']/a[1]").click();
    time.sleep(2)
    #Locates and sends username to username box
    id_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/ul/li[7]/form/input[1]")
    id_box.click();
    id_box.send_keys(my_username)
    #Locates and sends password to password box
    pw_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/ul/li[7]/form/input[2]")
    pw_box.click();
    pw_box.send_keys(my_password)
    driver.find_element_by_xpath("//*[@id='login_form']/input[3]").click();
    #TWaits for Post Quick Reply to become clickable
    wait = WebDriverWait(driver, 300)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/form/div[3]/input[10]")))
    #Find table on My bets page
    quick_reply_box = driver.find_element_by_id("vB_Editor_QR_textarea")
    #Define double bet button
    post_quick_reply = driver.find_element_by_id("qr_submit")
    #Sends bump post to Quick Reply box
    quick_reply_box.send_keys("Bumperino fellow human beings!")
    post_quick_reply.click();

bump_process()

driver.quit()
