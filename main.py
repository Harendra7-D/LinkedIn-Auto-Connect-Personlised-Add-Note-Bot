from selenium import webdriver
import time
import parameters

driver=webdriver.Chrome('chromedriver.exe')
driver.get('https://linkedin.com')

time.sleep(2)

username=driver.find_element_by_xpath("//input[@name='session_key']")
password=driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys(parameters.linkedin_username)
password.send_keys(parameters.linkedin_password)
time.sleep(2)

submit=driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

import random
driver.get('https://www.linkedin.com/in/aditya-kothari-451b9817')
time.sleep(1)


connect_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'connect')]")
driver.execute_script('arguments[0].click();', connect_button)
time.sleep(1)

ADD_NOTE_Button = driver.find_element_by_xpath("//button[starts-with(@class, 'mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view')]")
driver.execute_script('arguments[0].click();', ADD_NOTE_Button)
time.sleep(1)

main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'relative')]")
driver.execute_script('arguments[0].click();', main_div)
time.sleep(1)

greetings = ["Hello", "Hi", "Hey", "Ahoy", "Yo yo", "Sup"]
greetings_idx = random.randint(0, len(greetings) - 1)
message = greetings[greetings_idx] + " " + "Sorry, I didnt mean to bother you. This is a Automated message. Thanks!"
paragraph = driver.find_elements_by_tag_name('textarea')
paragraph[0].send_keys(message)
time.sleep(2)

Send = driver.find_element_by_xpath("//button[starts-with(@class, 'ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view')]")



