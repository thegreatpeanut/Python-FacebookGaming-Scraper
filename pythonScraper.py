import time
import csv
import json
import io
import psycopg2
from bs4 import BeautifulSoup
import re
import os
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import locale
from sqlalchemy import create_engine
locale.setlocale(locale.LC_ALL, '')


MainURL = "https://www.facebook.com/thesauruspg/"
VideosURL = "https://www.facebook.com/pg/thesauruspg/videos/?ref=page_internal"

# MainURL = input('Page URL:')
# VideosURL = input('Video Page URL:')

# Open Firefox
global driver
driver = webdriver.Firefox()

driver.get(MainURL)


time.sleep(1)

#Get the name / fixed tag
name = driver.find_element_by_id('seo_h1_tag').text
#name = driver.find_element_by_xpath('//*[@id="js_m"]').text

print(name)

# -----------------GET NUMBER OF FOLLOWERS--------------------------------------------------------------------------


followers = driver.find_element_by_css_selector(
    'div._2pi2:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text
remove = " people follow this,"
pattern = "[" + remove + "]"
followers = re.sub(pattern, "", followers)
followers = int(followers)
#followers = f'{followers:,}'

print(followers)

#------------------------------------------------------------------------

time.sleep(1)


#------------------GET NUMBER OF PAGE LIKES------------------------------------------------------------------

page_likes = driver.find_element_by_css_selector(
    'div._2pi2:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text
remove2 = ' people like this'
pattern2 = "[" + remove + "]"
page_likes = re.sub(pattern2, "", page_likes)
remove3 = 'k'
pattern3 = "[" + remove3 + "]"
page_likes = re.sub(pattern3, "", page_likes)
page_likes = int(page_likes)
#page_likes = f'{page_likes:,}'

print(page_likes)

# ----------------------------------------------------------------

time.sleep(1)

# Switch to video page

driver.get(VideosURL)


def do_scroll():
    try:
        time.sleep(1)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0, 10000)")

        time.sleep(5)

        not_now_button = driver.find_element_by_id(
            'expanding_cta_close_button')
        not_now_button.click()

        time.sleep(3)

        driver.find_element_by_tag_name(
            'body').send_keys(Keys.CONTROL + Keys.HOME)

        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 5000)")
    except NoSuchElementException:
        print("No button found")


do_scroll()

time.sleep(3)


last_height = driver.execute_script("return document.body.scrollHeight")

# while True:

#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


#     time.sleep(7)


#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         time.sleep(10)
#         break
#     last_height = new_height


#----------------------DELETE UNWANTED ELEMENTS-------------------------------------------------------------------------------


try:
    element = driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div[3]/div/div/div/ul')
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)
except NoSuchElementException:
    print("No element found")

try:
    element2 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/ul')
    driver.execute_script("""
    var element2 = arguments[0];
    element2.parentNode.removeChild(element2);
    """, element2)
except NoSuchElementException:
    print("No element2 found")

try:
    element3 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div[3]/div[2]/div/div/div[3]/div/div/div/ul')
    driver.execute_script("""
    var element3 = arguments[0];
    element3.parentNode.removeChild(element3);
    """, element3)
except NoSuchElementException:
    print("No element3 found")

try:
    element4 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div[4]/div[2]/div/div/div[3]/div/div/div/ul')
    driver.execute_script("""
    var element4 = arguments[0];
    element4.parentNode.removeChild(element4);
    """, element4)
except NoSuchElementException:
    print("No element4 found")

try:
    element5 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div[5]/div[2]/div/div/div[3]/div/div/div/ul')
    driver.execute_script("""
    var element5 = arguments[0];
    element5.parentNode.removeChild(element5);
    """, element5)
except NoSuchElementException:
    print("No element5 found")

try:
    element6 = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[1]')
    driver.execute_script("""
    var element6 = arguments[0];
    element6.parentNode.removeChild(element6);
    """, element6)
except NoSuchElementException:
    print("No element6 found")


ele = [x for x in element_list]

def
    try:
        driver.execute_script("""
        var ele = arguments[0];
        ele.parentNode.removeChild(ele);
        """, ele)
    except NoSuchElementException:
        print("No ele found")
        

#-------------------GET LIST OF VIDEO LIKES AND VIEWS----------------------------------------------------

video = driver.find_elements_by_class_name('bnpdmtie')
video_likes = driver.find_elements_by_class_name('pcp91wgn')

#-------------------------PARSE AND PROCESS VIDEO VIEWS-------------------------------------------------------------------------------

video_age_views = [x.text for x in video]
video.extend(video_age_views)
video_age_views = [i for i in video_age_views if i if not 'ago' in i]
video_age_views = [w.replace("Views", "") for w in video_age_views]
k_val = "K"
m_val = "M"
e_list = [i.replace('K', 'e3').replace('M', 'e6') for i in video_age_views]
values = [float(i) for i in e_list]
video_age_views = [f'{int(i):,}' for i in values]
removetable = str.maketrans('', '', ',')
video_age_views = [s.translate(removetable) for s in video_age_views]
print(video_age_views)


#------------------------PARSE AND PROCESS VIDEO LIKES----------------------------------------------------------------------------------------------


parsed_video_likes = [x.text for x in video_likes]
video_likes.extend(parsed_video_likes)
parsed_video_likes = [i for i in parsed_video_likes if i]
parsed_video_likes = [w.replace('K', '000') for w in parsed_video_likes]
removetable = str.maketrans('', '', '.')
parsed_video_likes = [s.translate(removetable) for s in parsed_video_likes]
for i in range(0, len(parsed_video_likes)):
    parsed_video_likes[i] = int(parsed_video_likes[i])
    #parsed_video_likes[i] = format(parsed_video_likes[i], "n")


print(parsed_video_likes)

# --------------------------------------------------------------------------------------------------------------


time.sleep(3)

#--------------------------------INIT DATA FRAMES, SEPARATELY THEN JOIN THEM INTO ONE DATA FRAME--------------------------------

searchfor = ['ago']

df = pd.DataFrame(video_age_views, columns=["Views"]).astype(int)
#df = df[~df.Age_and_Views.str.contains('|'.join(searchfor))]

df1 = pd.DataFrame(parsed_video_likes, columns=["Video_Likes"]).astype(int)

df2 = pd.DataFrame([name], columns=['Name'], index=[0])


df3 = pd.DataFrame([int(followers)], columns=['Followers'], index=[0])
df3 = df3.fillna(0).astype(int)

df4 = pd.DataFrame([int(page_likes)], columns=[
                   'Page_Likes'], index=[0]).astype(int)
df4 = df4.fillna(0).astype(int)
result = pd.concat([df2, df3, df4, df, df1], axis=1)

#result = result.fillna(" ")

#-----------------SEND DATA FRAME TO CSV THEN TO DB----------------------------------------------------------------------------------------------

result.to_csv('ParsedConcat.csv')

engine = create_engine('postgresql://postgres:@localhost:5432/FacebookGaming')
result.to_sql('FBGaming2', engine)

#driver.close()
