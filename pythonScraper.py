import time
import re
import os
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine
import psycopg2
import locale
import string
locale.setlocale(locale.LC_ALL, '')


def get_name():

    name_get = input('Please enter the name you find in the url: ')
    return name_get

name_get = get_name()

# global driver
# driver = webdriver.Firefox()
# driver.maximize_window()
# global LoginURL
# global MainURL
# MainURL = ''
# global VideosURL
# VideosURL = ''
# LoginURL = ''
# global name
# name = ''
# global followers
# followers = ''
# global page_likes
# page_likes = ''
# global video_age_views
# video_age_views = []
# global parsed_video_likes
# parsed_video_likes = []







# MainURL = "https://www.facebook.com/thesauruspg/?ref=page_internal"
# VideosURL = "https://www.facebook.com/thesauruspg/videos/?ref=page_internal"


# MainURL = "https://www.facebook.com/EbuGamer1"
# VideosURL = "https://www.facebook.com/EbuGamer1/videos/?ref=page_internal"

# MainURL = input('Page URL:')
# VideosURL = input('Video Page URL:')


# options = Options()
# options.headless = True

global driver
driver = webdriver.Firefox()


def fb_login():
    
    driver.maximize_window()
    LoginURL = "https://www.facebook.com/"
    driver.get(LoginURL)
    time.sleep(0.5)
    for line in open("secret.txt", "r").readlines(): 
        # Make a user_password.txt in the root folder where you enter your email/phone number
        #  and password on a single line separated by a single space
        login_info = line.split()
        username = login_info[0]
        password = login_info[1]
    try:
        cookies_button = driver.find_element_by_xpath(
            '//*[@id="u_0_k"]').click()
    except NoSuchElementException:
        print("Stupid cookie button!")

    emailelement = driver.find_element(By.ID, 'email')
    driver.implicitly_wait(0.5)
    emailelement.send_keys(username)
    passelement = driver.find_element(By.ID, 'pass')
    driver.implicitly_wait(0.5)
    passelement.send_keys(password)
    loginelement = driver.find_element_by_name('login')
    loginelement.click()
    time.sleep(3)


fb_login()


def main_page():
    MainURL = "https://www.facebook.com/{}/?ref=page_internal".format(name_get)
    driver.get(MainURL)
    time.sleep(2)
    
    try:
        delete_useless = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]')
        driver.execute_script("""
                var delete_useless = arguments[0];
                delete_useless.parentNode.removeChild(delete_useless);
                """, delete_useless)
    except NoSuchElementException:
        print("Nothing useless found!")
    driver.execute_script("window.scrollTo(0, 10000)")
    time.sleep(3)
    
main_page()

def do_name():
    try:
        name = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div[1]/h2/span/span').text
        return name
    except NoSuchElementException:
        print('Something wrong with the name element!')

name = do_name()
print(name)



# -----------------GET NUMBER OF FOLLOWERS--------------------------------------------------------------------------




def get_followers():
    try: 
        followers = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div/div/div/div[2]/div/div/span/span').text
        remove = " people follow this"
        pattern = "[" + remove + "]"
        followers = re.sub(pattern, "", followers)
        followers = followers.replace('K', 'e3').replace('M', 'e6')
        removetable = str.maketrans('', '', ',')
        followers = followers.translate(removetable)
        followers = float(followers)
        followers = f'{int(followers):,}'
        removetable = str.maketrans('', '', ',')
        followers = followers.translate(removetable)
        followers = int(followers)
        return followers
    except NoSuchElementException:
        print('Something went wrong with the followers path!')
        follow_path = input('Please input fllowers element xpath: ')
        followers = driver.find_element(By.XPATH, '{}'.format(follow_path)).text
        remove = " people follow this"
        pattern = "[" + remove + "]"
        followers = re.sub(pattern, "", followers)
        followers = followers.replace('K', 'e3').replace('M', 'e6')
        removetable = str.maketrans('' , '' , ',')
        followers = followers.translate(removetable)
        followers = float(followers)
        followers = f'{int(followers):,}'
        removetable = str.maketrans('', '', ',')
        followers = followers.translate(removetable)
        followers = int(followers)
        return followers

    
followers = get_followers()

print(followers)

# ------------------------------------------------------------------------



# ------------------GET NUMBER OF PAGE LIKES------------------------------------------------------------------


def get_page_likes():
    try:
        page_likes = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[4]/div/div/div/div[2]/div/div/span/span[1]').text
        remove2 = ' people'
        pattern2 = "[" + remove2 + "]"
        page_likes = re.sub(pattern2, "", page_likes)
        remove3 = ','
        pattern3 = "[" + remove3 + "]"
        page_likes = re.sub(pattern3, "", page_likes)
        page_likes = int(page_likes)
        removetable = str.maketrans('' , '' , ',')
        return page_likes
    except NoSuchElementException:
        print('Something went wrong with the page_likes element!')
        page_likes_path = input('Please input page_likes element xpath: ')
        page_likes = driver.find_element(By.XPATH, '{}'.format(page_likes_path)).text
        remove2 = ' people'
        pattern2 = "[" + remove2 + "]"
        page_likes = re.sub(pattern2, "", page_likes)
        remove3 = ','
        pattern3 = "[" + remove3 + "]"
        page_likes = re.sub(pattern3, "", page_likes)
        page_likes = int(page_likes)
        removetable = str.maketrans('', '', ',')
        return page_likes

page_likes = get_page_likes()
print(page_likes)


# driver.get(VideosURL)



# try:
#     delete_useless = driver.find_element_by_xpath(
#         '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]')
#     driver.execute_script("""
#             var delete_useless = arguments[0];
#             delete_useless.parentNode.removeChild(delete_useless);
#             """, delete_useless)
#     driver.execute_script("window.scrollTo(0, 10000)")
# except NoSuchElementException:
#     print("Nothing useless found!")

# ----------------------DELETE UNWANTED
# ELEMENTS-------------------------------------------------------------------------------


def delete_unwanted():
    VideosURL = "https://www.facebook.com/{}/videos/?ref=page_internal".format(name_get)
    driver.get(VideosURL)
    element1 = 0
    element2 = 0
    element3 = 0
    element4 = 0
    element5 = 0
    try:
        time.sleep(2)
        element1 = input("Please input the xpath of the 1st element you want deleted: ")
        element2 = input("Please input the xpath of the 2nd element you want deleted: ")
        element3 = input("Please input the xpath of the 3rd element you want deleted: ")
        element4 = input("Please input the xpath of the 4th element you want deleted: ")
        element5 = input("Please input the xpath of the 5th element you want deleted: ")
        # element1 = driver.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[1]')

        # element2 = driver.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[2]')
        # element3 = driver.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[3]/div')
        # element4 = driver.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div[4]')
        # element5 = driver.find_element_by_xpath(
        #     '/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[1]')
        
    except NoSuchElementException:
        
        print("Elements not present")

    element_path = [element1, element2, element3, element4, element5]
    try:
        for element in element_path:
            driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)
    except NoSuchElementException:
        print("Elements couldn't be delete!")

delete_unwanted()


def inf_scroll():
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(5)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            time.sleep(3)
            break
        last_height = new_height


#inf_scroll()


# -------------------GET LIST OF VIDEO LIKES AND VIEWS----------------------------------------------------
def get_views_likes():
    
    try:
        video = driver.find_elements_by_class_name('bnpdmtie')
        video_likes = driver.find_elements_by_class_name('pcp91wgn')
    except NoSuchElementException:
        print('Views and Likes element paths broken!!')
    return video, video_likes;
        
get_views_likes()

# -------------------------PARSE AND PROCESS VIDEO
# VIEWS-------------------------------------------------------------------------------




def get_video_views():
    video, video_likes = get_views_likes()
    video_age_views = [x.text for x in video]
    video.extend(video_age_views)
    video_age_views = [i for i in video_age_views if i if not 'ago' in i]
    video_age_views = [w.replace("Views", "") for w in video_age_views]
    e_list = [i.replace('K', 'e3').replace('M', 'e6') for i in video_age_views]
    values = [float(i) for i in e_list]
    video_age_views = [f'{int(i):,}' for i in values]
    removetable = str.maketrans('', '', ',')
    video_age_views = [s.translate(removetable) for s in video_age_views]
    return video_age_views


# video_age_views = get_video_views()
video_age_views = get_video_views()

# print(video_age_views)

# ------------------------PARSE AND PROCESS VIDEO
# LIKES----------------------------------------------------------------------------------------------



def get_video_likes():
    video, video_likes = get_views_likes()
    parsed_video_likes = [x.text for x in video_likes]
    video_likes.extend(parsed_video_likes)
    # parsed_video_likes = [s.strip("AaBbCcDdEeFfGgHhIiJjLlnOoPpQqRrSsTtUuVvWwXxYyZz") for s in parsed_video_likes]
    no_letters = str.maketrans(
        "", "", "    AaBbCcDdEeFfGgHhIiJjLlmMNnOoPpQqRrSsTtUuVvWwXxYyZz")
    parsed_video_likes = [s.translate(no_letters) for s in parsed_video_likes]
    e_list = [i.replace('K', 'e3').replace('M', 'e6')
              for i in parsed_video_likes]
    e_list = list(filter(None, e_list))
    values = [float(i) for i in e_list]
    parsed_video_likes = [f'{int(i):,}' for i in values]
    removetable2 = str.maketrans('', '', ',')
    parsed_video_likes = [s.translate(removetable2) for s in parsed_video_likes[::2]]
    return parsed_video_likes


parsed_video_likes = get_video_likes()
# # parsed_video_likes.remove(parsed_video_likes[0]
print(parsed_video_likes)

# --------------------------------------------------------------------------------------------------------------


time.sleep(3)

# --------------------------------INIT DATA FRAMES, SEPARATELY THEN JOIN THEM INTO ONE DATA
# FRAME--------------------------------

# searchfor = ['ago']
#


def table_to_csv():
    
    df2 = pd.DataFrame([name], columns=['Name'], index=[0])
    df3 = pd.DataFrame([int(followers)], columns=['Followers'], index=[0])
    df4 = pd.DataFrame([int(page_likes)], columns=[
                       'Page_Likes'], index=[0]).astype(int)
    df = pd.DataFrame(video_age_views, columns=["Views"]).astype(int)
    df1 = pd.DataFrame(parsed_video_likes, columns=["Video_Likes"]).astype(int)

    df3 = df3.fillna(0).astype(int)
    df4 = df4.fillna(0).astype(int)
    result = pd.concat([df2, df3, df4, df, df1], axis=1)
    result.to_csv(path_or_buf='CSVFiles\{}.csv'.format(name))


table_to_csv()

driver.close()
    
# time.sleep(1)
# fb_login()
# time.sleep(1)
# main_page()
# time.sleep(0.5)
# do_name()
# print(name)
# followers = get_followers()
# print(followers)
# page_likes = get_page_likes()
# print(page_likes)
# time.sleep(5)
# delete_unwanted()
# video_age_views = get_video_views()
# print(video_age_views)
# parsed_video_likes = get_video_likes()
# print(parsed_video_likes)
# table_to_csv()
# driver.close()


# engine = create_engine('postgresql://postgres:@localhost:5432/FacebookGaming')
# result.to_sql('FBGaming2', engine)



