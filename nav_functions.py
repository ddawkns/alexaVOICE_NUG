
def get_button_elm(h2_item):
    element = h2_item.find_element_by_xpath('../..')
    # element = element.find_element_by_xpath('..')

    button_elm = element.find_element_by_xpath(".//button")

    return button_elm


def get_section_item_total(button_elm):

    # Get text from "button_elm"
    button_elm_text = button_elm.text

    # given items for a section
    section_item_total = button_elm_text[8:-2]

    return section_item_total


def get_section_url_param(button_elm):

    # Get attribute of the button element
    button_elm_atb = button_elm.get_attribute('data-e2eid')

    # url parameter
    url_param = button_elm_atb[18:]

    return url_param

# Helper function for menu prep - splits menu into head and tail
def get_menu(item_name, menu_items_len, menu, menu_num):
    #
    menu += str(menu_num) + ". " + item_name + ", "

    # Add the following pharse before the loop ends
    if menu_num == menu_items_len:  # Adds one to "p" to check if this is the last iteration

        menu += "say repeat if you were too high the first time, \
            or say more to hear the rest of the menu."

    return menu

def get_item_list(img_dict, item_name, item_url, item_price, item_list, json_list_item):
    img_dict[item_name] = (item_url, item_price)
    item_list.append(json_list_item)
    return item_list

# Helper function for menu prep - splits menu into head and tail
def split_menu(item_name, menu_items_len, menu_num, head_menu, tail_menu):
    # Creates abbreviated menu so alexa doesnt have to speak the entire menu
    if menu_num < 7:
        head_menu += str(menu_num) + ". " + item_name + ", "

    else:
        tail_menu += str(menu_num) + ". " + item_name + ", "

    # Add the following pharse before the loop ends
    if menu_num == menu_items_len:
        head_menu += "say repeat if you were too high the first time"

        if menu_num > 7:
            head_menu += ", or say more to hear the rest of the menu."

        else:
            head_menu += "."

        tail_menu += "say repeat to hear the entire menu."

    return head_menu, tail_menu


def menu_prep(h2_menu_items):

    # Initate variables used in the following loop
    h2_menu_items_len = len(h2_menu_items)
    menu = ""
    head_menu = ""
    tail_menu = ""

    item_name_dict = {}
    section_url_param_item_total_dict = {}

    menu_num = 1

    # Loop through each item in the menu_items
    for h2_item in h2_menu_items:

        # Gets h2 item name
        h2_item_name = h2_item.text

        # Gets "See All" button element from the h2 item
        button_elm = get_button_elm(h2_item)

        # Gets total number of section items, from the "button_elm"
        section_item_total = get_section_item_total(button_elm)

        # Gets url_param from the "button_elm"
        url_param = get_section_url_param(button_elm)

        # Add to dictionary; key: menu_num - value: tuple(url_param, section_item_total)
        section_url_param_item_total_dict[menu_num] = (url_param, section_item_total)

        # Add to dictionary, key: menu_num - value: h2_item_name
        item_name_dict[menu_num] = h2_item_name

        menu = get_menu(h2_item_name, h2_menu_items_len, menu, menu_num)

        if h2_menu_items_len >= 7:
            head_menu, tail_menu = split_menu(h2_item_name, h2_menu_items_len, menu_num, head_menu, tail_menu)

        menu_num += 1

    return item_name_dict, section_url_param_item_total_dict, menu, head_menu, tail_menu

# "section menu" - gets (price, url, name) from "item.text"
def get_item_props(item):
    item_price = item.find_element_by_xpath('./div/div/div[2]/div[1]')
    item_price = item_price.text
    # Get the name of the item
    item_name = item.find_element_by_xpath('./div/div/div[2]/div[2]')
    item_name = item_name.text

    # Get the item url
    item_url = item.find_element_by_xpath('./div/div/div[1]/div[1]/img')
    item_url = item_url.get_attribute("src")

    return item_price, item_name, item_url