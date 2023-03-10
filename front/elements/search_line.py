from front.elements import wrapper


# search_line_wrapper = wrapper.focus('inputs')

def search_for(text: str):
    wrapper.focus_presented('inputs').element('#regular-search-input-desktop').type(text).press_enter()


def submit_by_click():
    wrapper.focus_presented('inputs').element('.search-box .input-group-btn').click()
