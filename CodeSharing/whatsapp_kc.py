from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

# construct the whatsapp message
# phone number
# message -- need to be urlencoded
message = "hello from STLog"

# replace with your own phone numbers
driver.get("https://api.whatsapp.com/send?phone=6590609803&text="+ message)

# click on send button
#elem = driver.find_element_by_id("action-button")
#Edited by TML 10 Oct 2022
driver.implicitly_wait(3)
elem = driver.find_element("id","action-button")
elem.send_keys(Keys.RETURN)

# click on the use WhatsApp Link
driver.implicitly_wait(20) # seconds only need to call once, it will wait for 10 sec
elem = driver.find_element("link text", "use WhatsApp Web")
actions = ActionChains(driver)
actions.click(elem)
actions.perform()

time.sleep(10)
'''
# the selector can be found using 'right-click->Inspect' in Chrome browser
# In the copy the chrome developer window, right-click->copy->Copy Selector
#elem = driver.find_element_by_css_selector("#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text")
elem = driver.find_element_by_css_selector("#main > footer > div._2BU3P.tm2tP.copyable-area > div > div > div._2lMWa > div.p3_M1 > div > div._13NKt.copyable-text.selectable-text")
time.sleep(1)
elem.send_keys(Keys.RETURN)
'''

#updated by TML: 31 Oct 2021
#inp_xpath = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
#input_box = driver.find_element_by_xpath(inp_xpath)
#updated by TML: 10 Oct 2022
#inp_xpath = "#main > footer > div._2BU3P.tm2tP.copyable-area > div > span:nth-child(2) > div > div._2lMWa > div._3HQNh._1Ae7k > button > span"
#input_box = driver.find_element("css selector", inp_xpath)
#updated by TML: 14 Mar 2023
#inp_xpath = "#main > footer > div._2lSWV._3cjY2.copyable-area > div > span:nth-child(2) > div > div._1VZX7 > div._2xy_p._3XKXx > button > span"
#updated by TML: 11 Jul 2023
inp_xpath = "#main > footer > div._2lSWV._3cjY2.copyable-area > div > span:nth-child(2) > div > div._1VZX7 > div._2xy_p._3XKXx > button > span"
input_box = driver.find_element("css selector", inp_xpath)


time.sleep(2)
#input_box.send_keys(Keys.ENTER)
input_box.click()
time.sleep(2)


