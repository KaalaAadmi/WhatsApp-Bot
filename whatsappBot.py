from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge("D://Edge Driver//msedgedriver.exe")

driver.get("https://web.whatsapp.com")

input("Please scan QR Code and press any key to continue: ")
name = input("Please enter the name of the person you want to send the message: ")
message = input("Please enter the Message you want to send to "+name+": ")

#Timer
delay = int(input("please enter the delay in minutes: "))
time.sleep(delay * 60)

user = driver.find_element_by_css_selector('span[title="'+name+'"]')
user.click()

textInput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

textInput.send_keys(message)
textInput.send_keys(Keys.RETURN)