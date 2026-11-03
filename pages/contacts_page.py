from pages.base_page import BasePage
from playwright.sync_api import Page


class ContactsPage(BasePage):
    def __init__(self, page:Page) -> None:
        super().__init__(page)
        self.link_add = page.locator("a[href='/add']")

    def is_link_add_present(self) -> bool:
        return self.is_element_visible(self.link_add)
