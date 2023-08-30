from page_object.page_object import HandlingClass
import pytest


@pytest.mark.ui
def test_add_to_favorite(chrome):
    page = HandlingClass(chrome)
    page.go_to_site()
    page.add_favorite_button().click()

    assert page.added_favorite_button().text == "В избранном"
    assert page.added_favorite_button().get_attribute("data-is-favorite") == "true"



