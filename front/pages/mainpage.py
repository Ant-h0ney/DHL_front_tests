from selene.support.shared import browser

from front.elements import search_line


def open():  # NOQA
    browser.open('')


def search(value: str):
    search_line.search_for(value)
