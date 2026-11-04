from playwright.sync_api import Page, expect, Locator, TimeoutError as PlaywrightTimeoutError
import re

DEFAULT_TIMEOUT = 5_000

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def is_url_contains(self, text: str, timeout:int = DEFAULT_TIMEOUT) -> bool:
        try:
            expect(self.page).to_have_url(re.compile(re.escape(text)), timeout=timeout)
            return True
        except AssertionError:
            print(f"AssertionError: {text}")
            return False

    def is_element_visible(self, locator: Locator, timeout:int = DEFAULT_TIMEOUT) -> bool:
        try:
            locator.wait_for(state="visible", timeout=timeout)
            return True
        except PlaywrightTimeoutError:
            return False
