import os
from pydoc import classname
import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from threading import Thread
import requests

import asyncio

options = Options()
options.set_preference("media.volume_scale", "0.0");


# using webdriver's install_addon API to install the downloaded Firefox extension
service = Service("C:/Users/x79/PycharmProjects/ScrapeJAVHDPORN/geckodriver-v0.30.0-win64/geckodriver.exe")

driver = webdriver.Firefox(service=service,options=options)

# driver.install_addon(extension_path, temporary=True)

main_page = driver.current_window_handle

driver.get("https://vlxx.sex/tag/tsumugi-akari/")

# switch to first tab
driver.switch_to.window(driver.window_handles[0])

all_video = driver.find_element(By.ID, "video-list").find_elements(By.CLASS_NAME, "video-item")
# clear txt file data
open('video_url.txt', 'w').close()
# write new data
file_object = open('video_url.txt', 'a')
for a_video in all_video:
    print(a_video.find_element(By.TAG_NAME, 'a').get_attribute("href"))
    # Append 'hello' at the end of file
    file_object.write(a_video.find_element(By.TAG_NAME, 'a').get_attribute("href"))
    file_object.write("\n")

# Close the file
file_object.close()

# create action chain object
action = ActionChains(driver)
exit()