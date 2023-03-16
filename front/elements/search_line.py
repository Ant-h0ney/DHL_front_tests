from front.elements import wrapper
import allure

# search_line_wrapper = wrapper.focus('inputs')


@allure.step('Fill and apply search bar with "{text}"')
def search_for(text: str):
    wrapper.focus_presented('inputs').element('#regular-search-input-desktop').type(text).press_enter()


@allure.step('Click on the magnifier (search button)')
def submit_by_click():
    wrapper.focus_presented('inputs').element('.search-box .input-group-btn').click()
