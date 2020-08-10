import time
import csv
import json
from bs4 import BeautifulSoup
import re
import os
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locale
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

print(name)

# -------------------------------------------------------------------------------------------


#Get Followers / Check if it works for other pages / Remove text , keep int only in var

followers = driver.find_element_by_css_selector('div._2pi2:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text
remove = " people follow this,"
pattern = "[" + remove + "]"
followers = re.sub(pattern, "", followers)
followers = int(followers)
followers = f'{followers:,}'
# followers = format(followers, "n") / another method

print(followers)

#------------------------------------------------------------------------

time.sleep(1)


#Get Page Likes / Check if it works for other pages / Remove text , keep int only in var

page_likes = driver.find_element_by_css_selector('div._2pi2:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text
remove2 = ' people like this'
pattern2 = "[" + remove + "]"
page_likes = re.sub(pattern2, "" , page_likes)
remove3 = 'k'
pattern3 = "[" + remove3 + "]"
page_likes = re.sub(pattern3, "" , page_likes)
page_likes = int(page_likes)
page_likes = f'{page_likes:,}'

print(page_likes)

# ----------------------------------------------------------------

time.sleep(1)

# Switch to video page

driver.get(VideosURL)


def do_scroll():

    time.sleep(1)

    driver.execute_script("window.scrollTo(0, 10000)")

    time.sleep(5)

    not_now_button = driver.find_element_by_id('expanding_cta_close_button')
    not_now_button.click()

    time.sleep(3)



do_scroll()

# time.sleep(1)


# driver.execute_script("window.scrollTo(0, 10000)")


# time.sleep(5)

# not_now_button = driver.find_element_by_id('expanding_cta_close_button')
# not_now_button.click()


# time.sleep(3)




# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
   
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    
#     time.sleep(3)

    
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height


#--------------------------------------------------------------------------------------------------------
# init var for views and video likes / remove ALL text eventaully , only keep int / It's an array of elements

video = driver.find_elements_by_class_name('bnpdmtie')

element = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[1]/div[4]/div/div/div[1]/div/div[1]/span[2]/span/span')
driver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)

element2 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/div[4]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[2]/div/div/span/div/span[2]/span/span')
driver.execute_script("""
var element2 = arguments[0];
element2.parentNode.removeChild(element2);
""", element2)
video_likes = driver.find_elements_by_class_name('pcp91wgn')



# Iterate trough all elements || Must do otherwise errors 
	
#video views - split list into AGE and VIEWS // make AGE/TIME :: 
# "a day ago" = 1
# "a week ago" = 7
# "a month ago" = 30
# "weeks" = 7
# "months" = 30

video_age_views = [x.text for x in video]
video.extend(video_age_views)
video_age_views = [i for i in video_age_views if i if not 'ago' in i]
video_age_views = [w.replace("Views", "") for w in video_age_views]
#removetable1 = str.maketrans('', '', '.')
#video_age_views = [s.translate(removetable1) for s in video_age_views]
#video_age_views = [w.replace("K", "") for w in video_age_views]
#video_age_views = [w.replace("M", "") for w in video_age_views]
#video_age_views = [w.replace(".", "") for w in video_age_views]

k_val = "K"
m_val = "M"

# if any(k_val in s for s in video_age_views):
#     video_age_views = [w.replace("K", "") for w in video_age_views]
#     video_age_views = [float(i) for i in video_age_views]
#     video_age_views = [elem * 1000 for elem in video_age_views]

# elif any(m_val in x for x in video_age_views):
#     video_age_views = [w.replace("M", "") for w in video_age_views]
#     video_age_views = [float(i) for i in video_age_views]
#     video_age_views = [elem * 1000000 for elem in video_age_views]


## app 1
e_list = [i.replace('K', 'e3').replace('M', 'e6') for i in video_age_views]
values = [float(i) for i in e_list]
video_age_views = [f'{int(i):,}' for i in values]





     

#video_likes_int = [float(i) for i in video_age_views]
        



# for i in range(0, len(video_age_views)):
#     video_age_views[i] = int(video_age_views[i])
#     video_age_views[i] = format(video_age_views[i], 'n')


# inds_k = [ i for i, s in enumerate(video_age_views) if 'K' in s] + [len(video_age_views)]
# div_1 = [video_age_views[inds_k[i]:inds_k[i+1]] for i in range(len(inds_k)-1)]

# def divide_List(video_age_views):
#     dct = {}
#     for k_val in video_age_views:
#         if k_val not in dct:
#             dct[k_val] = k_val
#     res = []
#     for key in sorted(dct):
#         res.append(dct[key])
#     return res                

print(video_age_views)



# video likes
parsed_video_likes = [x.text for x in video_likes]
video_likes.extend(parsed_video_likes)
parsed_video_likes = [i for i in parsed_video_likes if i]
parsed_video_likes = [w.replace('K', '000') for w in parsed_video_likes]
removetable = str.maketrans('', '', '.')
parsed_video_likes = [s.translate(removetable) for s in parsed_video_likes]
for i in range(0, len(parsed_video_likes)):
    parsed_video_likes[i] = int(parsed_video_likes[i])
    parsed_video_likes[i] = format(parsed_video_likes[i], "n")	


print(parsed_video_likes)

# --------------------------------------------------------------------------------------------------------------
time.sleep(3)



searchfor = ['ago']

df = pd.DataFrame(video_age_views, columns=["Views"])
#df = df[~df.Age_and_Views.str.contains('|'.join(searchfor))]

df1 = pd.DataFrame(parsed_video_likes, columns=["Video_Likes"])

df2 = pd.DataFrame([name], columns=['Name'], index =[0])

df3 = pd.DataFrame([followers], columns=['Followers'], index=[0])

df4 = pd.DataFrame([page_likes], columns=['Page_Likes'], index=[0])

result = pd.concat([df2, df3, df4, df, df1], axis=1)

result = result.fillna(" ")

result.to_csv('ParsedConcat.csv')


#driver.close()
