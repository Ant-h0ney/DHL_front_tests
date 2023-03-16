import allure
from selene.support.shared import browser

from front.elements import search_line


@allure.step('Open the mainpage')
def open():  # NOQA
    browser.open('')


@allure.step('Search {value}')
def search(value: str):
    search_line.search_for(value)
