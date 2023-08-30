from base_page.base_page import BasePage
from base_page.base_page import ElementHasCssClass
from selenium.webdriver.common.by import By


class PageLocators:
    """Здесь представлен список локаторов элементов страницы.
    NAME = (By.type_of_locator, 'locator')."""
    ADD_FAVORITE_BUTTON = (By.CSS_SELECTOR, ".desktop-usq1f1[title='Добавить в избранное']")

    FAVORITE_BUTTON = (By.CSS_SELECTOR, ".desktop-1rdftp2")
    FAVORITE_LIST = (By.CSS_SELECTOR, ".item-snippet-column-2-md2mY")


class ExpectedAttributes:
    """Здесь представлен список ожидаемых атрибутов элементов страницы.
    ATTRIBUTE_NAME = 'attribute_value'."""
    ADD_FAVORITE_BUTTON = (By.CSS_SELECTOR, ".desktop-usq1f1[title='В избранном']")


class HandlingClass(BasePage):
    """Здесь представлен список методов для взаимодействия с элементами страницы."""
    def add_favorite_button(self):
        add_favorite_button = self.find_element(PageLocators.ADD_FAVORITE_BUTTON, time=10)
        return add_favorite_button

    def favorite_button(self):
        favorite_button = self.find_element(PageLocators.FAVORITE_BUTTON, time=10)
        return favorite_button

    def favorite_list(self):
        favorite_list = self.find_element(PageLocators.FAVORITE_LIST, time=10)
        return favorite_list

    def added_favorite_button(self):
        added_favorite_button = self.find_element(ExpectedAttributes.ADD_FAVORITE_BUTTON, time=10)
        return added_favorite_button



