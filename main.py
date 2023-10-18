from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from datetime import time

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(10)
link = "https://www.youtube.com/watch?v=2diqLGcfxYo&list=PL-A2dZy0djeKVCZHbVEqBMx-tIZn27cmT&pp=iAQB"
browser.get(link)

try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//ytd-playlist-panel-video-renderer//'
                                                  'div[@id="time-status"]/span[@id="text"]'))
    )
except:
    print("Exception occurred")

playlist = browser.find_elements(By.XPATH, '//ytd-playlist-panel-video-renderer//'
                                           'div[@id="time-status"]/span[@id="text"]')
time_list = []
for x in playlist:
    time_list.append(x.get_attribute('aria-label'))
    # print(x.get_attribute('innerHTML').strip())
    # print(x.get_attribute('aria-label'))

time_hours = 0
time_minutes = 0
time_seconds = 0
for time_stamp in time_list:

    time_split = time_stamp.split(',')

    for time_in in time_split:
        time_in = time_in.strip()
        time_in_list = time_in.split(" ")
        if time_in_list[1].__contains__("hours"):
            time_hours = time_hours + int(time_in_list[0])
        elif time_in_list[1].__contains__("minutes"):
            time_minutes = time_minutes + int(time_in_list[0])
        elif time_in_list[1].__contains__("seconds"):
            time_seconds = time_seconds + int(time_in_list[0])

print(f"total time will be {time_hours} hours, {time_minutes} minutes and {time_seconds} seconds")
if time_seconds >= 60:
    seconds_to_minutes = time_seconds // 60
    time_minutes = time_minutes + seconds_to_minutes
    time_seconds = time_seconds % 60

if time_minutes >= 60:
    minutes_to_hours = time_minutes // 60
    time_hours = time_hours + minutes_to_hours
    time_minutes = time_minutes % 60

print(f"total time will be {time_hours} hours, {time_minutes} minutes and {time_seconds} seconds")
