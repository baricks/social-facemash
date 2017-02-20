from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib2
import time
import shutil
import requests

driver = webdriver.PhantomJS()
driver.get("https://www.linkedin.com/uas/login")

# Log into LinkedIn
login = driver.find_element_by_css_selector('#session_key-login')
login.send_keys(' ')
password = driver.find_element_by_css_selector('#session_password-login')
password.send_keys(' ')
password.send_keys(Keys.RETURN)
time.sleep(3)

# Go to list of connections
driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
time.sleep(3)


# Cycle through each connection's picture
for i in range(0,600):
    print "On loop #" + str(i)

    profile = driver.find_elements_by_class_name('lazy-image')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    profile[i].click()
    time.sleep(3)

    # Get profile picture url
    profile_pic = driver.find_element_by_class_name('pv-top-card-section__image')
    img_url = profile_pic.get_attribute("src")
    response = requests.get(img_url, stream=True)
    image_name = str(i) + ".png"

    # Download profile picture
    with open(image_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    driver.back()
    time.sleep(3)

    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(3)

driver.quit()
