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

time.sleep(1)


driver.execute_script("window.scrollTo(0, 10000)")


time.sleep(5)

not_now_button = driver.find_element_by_id('expanding_cta_close_button')
not_now_button.click()


time.sleep(3)




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

video_likes = driver.find_elements_by_class_name('pcp91wgn')



# Iterate trough all elements  
	
#video views - split list into AGE and VIEWS // make AGE/TIME  ?? Undecided
# "a day ago" = 1
# "a week ago" = 7
# "a month ago" = 30
# "weeks" = 7
# "months" = 30

video_age_views = [x.text for x in video]
video.extend(video_age_views)
video_age_views = [i for i in video_age_views if i]


# trying to find a way to quantify the date for each video
# [w.replace("a day ago", "1").replace("a week ago", "7").replace("days ago", "").replace("weeks ago" , "").replace("months ago" , "") for w in video_age_views]

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

df = pd.DataFrame(video_age_views, columns=["Age_and_Views"])
df = df[~df.Age_and_Views.str.contains('|'.join(searchfor))]

df1 = pd.DataFrame(parsed_video_likes, columns=["Video_Likes"])

df2 = pd.DataFrame([name], columns=['Name'], index =[0])

df3 = pd.DataFrame([followers], columns=['Followers'], index=[0])

df4 = pd.DataFrame([page_likes], columns=['Page Likes'], index=[0])

result = pd.concat([df2, df3, df4, df, df1], axis=1)

result = result.fillna(" ")

result.to_csv('ParsedConcat.csv')


#driver.close()
