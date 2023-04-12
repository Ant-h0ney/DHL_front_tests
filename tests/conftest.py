from dataclasses import dataclass

import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_preparation():
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://www.dollartree.com/'
    yield


@dataclass
class Resolution:
    width: int
    height: int

    def __repr__(self):
        return f'Resolution is [{self.width}*{self.height}]'


desktop_size = Resolution(width=1200, height=1000)
mobile_size = Resolution(width=375, height=667)


@pytest.fixture(scope='function', autouse=True, params=[desktop_size], ids='default')
def resolution(request):
    browser.config.window_width = request.param.width
    browser.config.window_height = request.param.height


web = pytest.mark.parametrize('resolution', [desktop_size], indirect=True, ids=repr)
adaptive = pytest.mark.parametrize('resolution', [mobile_size], indirect=True, ids=repr)
web_and_adaptive = pytest.mark.parametrize('resolution', [desktop_size, mobile_size], indirect=True, ids=repr)

