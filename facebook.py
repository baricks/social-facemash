from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading
import shutil
import requests

currentLoop = 0

def downloadImage():

    # Create unique filenames
    global currentLoop
    currentLoop += 1
    print "Current loop is " + str(currentLoop)
    image_name = str(currentLoop) + ".png"

    # # Am I the only one tagged?
    # tagged = driver.find_element_by_class_name('tagswrapper')
    # print tagged

    # Get the image src
    big_image = driver.find_element_by_class_name('spotlight')
    img_url = big_image.get_attribute("src")
    response = requests.get(img_url, stream=True)

    # Download the image
    with open(image_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    time.sleep(2)

    # Click to the next image
    big_image = driver.find_element_by_class_name('spotlight')
    big_image.click()
    time.sleep(2)

    # Start another loop
    threading.Timer(3, downloadImage()).start()


# Set up Driver
driver = webdriver.PhantomJS()
driver.get("http://www.facebook.com/login")

# Log into Facebook
login = driver.find_element_by_css_selector('#email')
login.send_keys('')
password = driver.find_element_by_css_selector('#pass')
password.send_keys(' ')
password.send_keys(Keys.RETURN)
time.sleep(2)

# Go to tagged photos
username = ' '
url = "https://www.facebook.com/" + username + "/photos_of"
driver.get(url)
time.sleep(2)

# Click on the first tagged photo
gallery_image = driver.find_elements_by_class_name('uiMediaThumbImg')
gallery_image[0].click()

# Run the download image function
downloadImage()

driver.quit()
