from db.main import database
from json_.main import json_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from create_all import create_all
import time
import os

urls = []

name = input("enter name of your file: ")
url = input('enter your videos page url: ')
driver = webdriver.Chrome("./chromedriver")
try:
    driver.get(url)
    time.sleep(3)
    print('now you must scroll down.')
    time.sleep(15)
    try:
        videos = driver.find_elements(By.CSS_SELECTOR, '#video-title')
    except NoSuchElementException:
        print("can't find a video movie.")
    for video in videos:
        try:
            if video.get_attribute('href') in urls:
                continue
            else:
                urls.append(video.get_attribute('href'))
        except:
            if videos:
                if '.' in name:
                    new_name = name[:name.find('.')]
                    os.mkdir(new_name)
                    create_all.all(path=new_name, name=name, datas=urls)
                else:
                    os.mkdir(name)
                    create_all.all(path=name, name=name, datas=urls)
except Exception as e:
    print('error on this url => {0}, reason => {1}'.format(url, e))

if '.' in name:
    new_name = name[:name.find('.')]
    os.mkdir(new_name)
    create_all.all(path=new_name, name=name, datas=urls)
else:
    os.mkdir(name)
    create_all.all(path=name, name=name, datas=urls)

