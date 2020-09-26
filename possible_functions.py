# def no_login():
#     try:
#         time.sleep(1)
#         driver.maximize_window()
#         driver.execute_script("window.scrollTo(0, 10000)")

#         time.sleep(5)

#         not_now_button = driver.find_element_by_id(
#             'expanding_cta_close_button')
#         not_now_button.click()

#         time.sleep(3)

#         driver.find_element_by_tag_name(
#             'body').send_keys(Keys.CONTROL + Keys.HOME)

#         time.sleep(1)

#         driver.execute_script("window.scrollTo(0, 5000)")
#     except NoSuchElementException:
#         print("No button found")
