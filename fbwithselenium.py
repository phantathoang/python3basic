#downloads selenium 
#pip3 install selenium

#dowload chrome driver 
#http://chromedriver.chromium.org

from selenium import webdriver
username = 'example@gmail.com'
password = 'abc-HyN-286-@@'

url = 'https://www.facebook.com'

driver = webdriver.Chrome('/Users/pcName/Downloads/chromedriver')
driver.get(url)

#find element by id in chrome browser at fb homepage

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.file_element_by_id('loginbutton').click()

