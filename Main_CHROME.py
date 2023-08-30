from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

def create_files_from_web(index):
    #elements and offers are the same however "elements" become stale after first loop - variable must be declared every loop
    offers = driver.find_elements(by=By.CSS_SELECTOR, value='[class^="card card"]')
    card = offers[index]
    card.click()
    header = driver.find_element(by=By.CSS_SELECTOR, value='h1.mb-1')
    story_text = driver.find_element(by=By.CSS_SELECTOR, value='div.story__text')
    clean_header_text = re.sub(r'[^\w\s]', '', header.text).replace(' ', '_')
    file_name = f"{clean_header_text}.txt"
    with open(file_name, "w") as file:
        file.write(story_text.text)
    driver.back()

#Start webpage
driver_path = "C:\Program Files (x86)\chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.cts-tradeit.cz/kariera/")

#Get rid of cookies
button = driver.find_element(by=By.ID, value="c-p-bn")
button.click()

elements = driver.find_elements(by=By.CSS_SELECTOR, value='[class^="card card"]')

#loop through all offers
for index, value in enumerate(elements):
    create_files_from_web(index)


driver.close()



