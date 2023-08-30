from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from custom_waitings.custom_waitings import ElementHasCssClass, ElementHasChildren


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.avito.ru/izhevsk/oborudovanie_dlya_biznesa/elektrostantsiya_20_kvt_v_kozhuhe_2931197932'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find an element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_css_class(self, locator, css_class, time=10):
        return WebDriverWait(self.driver, time).until((ElementHasCssClass(locator, css_class)),
                                                      message=f"Can't find ccs_class: {css_class}.")

    def wait_children(self, locator, sub_locator, time=10):
        return WebDriverWait(self.driver, time).until((ElementHasChildren(locator, sub_locator)),
                                                      message=f"Can't find children with sub_locator: {sub_locator}")

    def find_title(self, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.title_is(text))

    def go_to_site(self):
        return self.driver.get(self.base_url)