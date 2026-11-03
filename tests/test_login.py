from models.user import User
from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage
from utils.soft_assert import SoftAssert


def test_login_positive(login_page: LoginPage, base_user: User):
    login_page.type_login_registration_form(base_user)
    login_page.click_btn_login()
    contacts_page = ContactsPage(login_page.page)
    soft = SoftAssert()
    soft.assert_true(contacts_page.is_link_add_present(), "validate  link add present")
    soft.assert_true(contacts_page.is_url_contains("contacts"), "validate url")
    soft.assert_all()

