"""
Using this script to test scrapping outside of Alexa
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from alexaVOICENUG import nav_functions as nf

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('-headless')
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get("https://www.eaze.com/menu")


intro_popup = driver.find_element_by_class_name("css-0")
intro_popup_buttons = intro_popup.find_element_by_tag_name('button')

intro_popup_text = intro_popup_buttons.text
intro_popup_buttons.click()

button = driver.find_element_by_tag_name('button')
button_class = button.get_attribute("class")

button.click()

form = driver.find_element_by_tag_name("form")
form_label = form.find_element_by_tag_name("label")
form_div = form_label.find_element_by_tag_name("div")

input_elm = form_div.find_element_by_tag_name("input")
input_elm.click()
input_elm.send_keys("Hollywood, CA")
time.sleep(3)
form_div_div = form_div.find_element_by_tag_name("div")
# children = form_div_div.find_elements_by_css_selector("*")
ul_elm = form_div_div.find_element_by_tag_name("ul")
li_elm = ul_elm.find_element_by_tag_name("li").click()

time.sleep(3)

# Get all h2 elements, which represent the items on the menu
# h2_menu_items = driver.find_elements_by_xpath('./div')
# h2_menu_items = driver.find_elements(By.TAG_NAME, 'h2')
# time.sleep(2)
# h2_menu_items = driver.find_elements_by_xpath('//h2')
# h2_menu_item = h2_menu_items[0]
#
# p=0
# for item in h2_menu_items:
#     if p < 4:
#         go_up = item.find_element_by_xpath('../../../../..')
#
#         # print(go_up.get_attribute("class"))
#         # go_down = go_up.find_element_by_xpath("./div[2]/div/div[3]/div")
#
#         # go_down = go_up.find_element_by_class_name("css-14fj73o")
#         go_down = go_up.find_element_by_xpath(".//img").get_attribute("src")
#         print(go_down)
#         if not go_down:
#             # print("op")
#             go_down = go_up.find_elements_by_tag_name("img")
#             # for item in go_down:
#             #     print(item.get_attribute("class"))
#
#         # print(go_down)
#
#         p+=1


div_next = driver.find_element_by_id("__next")
div_menu = div_next.find_element_by_tag_name("div")
div_see_all = div_menu.find_element_by_class_name("e1u2pro73")
buttons = div_see_all.find_element_by_tag_name("button").click()

time.sleep(1)

div_link = driver.find_elements_by_class_name("e1azgudk0")
plus_button = div_link[6].find_element_by_tag_name("button").click()

time.sleep(1)

# cart_div = driver.find_element_by_class_name("e1txra6n2")
# cart_button = cart_div.find_element_by_tag_name("button")
# cart_button.click()
#
# checkout = driver.find_elements_by_class_name("eqq582b0")
# checkout_click = checkout[33].click()


# driver.quit()
