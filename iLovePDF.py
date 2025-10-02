from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.ilovepdf.com/")
sleep(5)

# Account sign up code
# driver.find_element(By.CSS_SELECTOR, value= 'div[class= "tag workflows"][data-filter="workflows"]').click()
# sleep(2)
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, value= "Sign up").click()
# sleep(2)
# Name = driver.find_element(By.ID, value= "name")
# Name.send_keys("CoreXManzoid")
# Email = driver.find_element(By.NAME, value= "SignupForm[email]")
# Email.send_keys("happymod366@gmail.com")
# Password = driver.find_element(By.CSS_SELECTOR , value= "input[placeholder='Password']")
# Password.send_keys("xxxxxxxxxxxxx")
# sleep(3)
# driver.find_element(By.ID, value= "registerButton").click()

driver.find_element(By.LINK_TEXT , value= "Login").click()
sleep(2)
email = driver.find_element(By.ID, value= "loginEmail")
email.send_keys("xxxxxxxxxxxxxxxx")
sleep(1)
password = driver.find_element(By.NAME, value= "LoginForm[password]")
password.send_keys("xxxxxxxxxxxxx")
driver.find_element(By.ID, value= "loginBtn").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, value= "a[title= 'Compress PDF']").click()
sleep(2)
pick_files = driver.find_element(By.ID, value= "pickfiles")
# pick_files.send_keys("C:/Users/munee/OneDrive/Desktop")  # Update with the actual file path
input("Select the file manually and press Enter to continue...")
driver.find_element(By.XPATH, value= '//*[@id="processTask"]').click()

WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".downloader a[slot='downloadUrl']")))
download = driver.find_element(By.CSS_SELECTOR, value= ".downloader a[slot= 'downloadUrl']").click()
sleep(5)
print("Your file has been compressed and downloading Automatically...")
sleep(2)
print("Thanks for using our service!\n Please wait for the download to complete.")
sleep(3)
print("If the download does not start, please click the download button manually.")
sleep(2)
print("Powered by: CoreXManzoid")
# Assuming the file upload dialog is handled manually or with another method
