#Boilerplate code for web scraping.

from selenium import webdriver
driver=webdriver.Chrome()
url = ""
driver.get(url)
someText=driver.find_element_by_id('body-content')
print(someText.text)
driver.close()
