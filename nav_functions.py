def getAll_Buttons(item):
    element = item.find_element_by_xpath('..')
    element = element.find_element_by_xpath('..')

    button_elm = element.find_element_by_xpath(".//button")

    button_elm_text = button_elm.text
    buttont_elm_atb = button_elm.get_attribute('data-e2eid')

    # given items for a category
    num_of_items = button_elm_text[8:-2]
    button = buttont_elm_atb[18:]

    return button, num_of_items


def getButton(h2):
    buttons = h2.find_element_by_xpath('..')
    buttons = buttons.find_element_by_xpath('..')
    buttons = buttons.find_element_by_xpath(".//button").get_attribute('data-e2eid')

    buttons = buttons[18:]

    return buttons