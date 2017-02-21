from selenium import webdriver
import urllib2
import time
import shutil
import requests

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Cabinet_of_Donald_Trump")

profile = driver.find_elements_by_class_name('thumbborder')

# Cycle through each connection's picture
for i in range(0,24):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print "On loop #" + str(i)

    profile[i].click()
    time.sleep(2)

    # Get profile picture url
    profile_pic = driver.find_element_by_class_name('jpg')
    img_url = profile_pic.get_attribute("src")
    response = requests.get(img_url, stream=True)
    image_name = str(i) + ".png"

    # Download profile picture
    with open(image_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    driver.back()
    time.sleep(2)
