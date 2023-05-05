from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def check_exists_by_xpath(web_driver, xpath):
    try:
        web_driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True
