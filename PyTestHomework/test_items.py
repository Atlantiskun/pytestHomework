import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def test_add_to_cart_button_is_exist(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    is_button_exist = False

    try:
        browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

        # Added for facilities
        time.sleep(30)

        is_button_exist = True
    except NoSuchElementException:
        pass

    assert is_button_exist, "Add to cart button doesn't exist"
