from db.main import database
from json_.main import json_
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from create_all import create_all
import time


name_of_path = input("enter path name: ")
urls = json_.read_data(path=name_of_path, name=name_of_path)
iframes = {}

driver = webdriver.Chrome('.\chromedriver.exe')

for index, url in enumerate(urls):
    try:
        driver.get(url)
        if index == 0:
            time.sleep(20)
        else:
            time.sleep(7)
        try:
            name = driver.find_element(By.CSS_SELECTOR, '#container > h1 > yt-formatted-string').text
            author = driver.find_element(By.CSS_SELECTOR, '#text > a').text
            author_link = driver.find_element(By.CSS_SELECTOR, '#text > a').get_attribute('href')
            share = driver.find_element(By.CSS_SELECTOR, '#top-level-buttons-computed > ytd-button-renderer:nth-child(3) > a')
            share.click()
            time.sleep(1.7)
            embed = driver.find_element(By.CSS_SELECTOR, '#target > yt-icon')
            embed.click()
            time.sleep(1.7)
            text_area = driver.find_element(By.CSS_SELECTOR, '#textarea')
            iframe = text_area.get_attribute('value')
            try:
                if iframe in iframes:
                    continue
                else:
                    iframes[url] = [name, author, author_link, iframe]
            except:
                if iframes:
                    create_all.all(path=name_of_path, name='iframes', datas=iframes)
                    break
        except Exception as e:
            print('error on this url => {0}, reason => {1}'.format(url, e))
    except NoSuchElementException:
        print("can't find a element.")
if iframes:
    create_all.all_iframe(path=name_of_path, name='iframes', datas=iframes)