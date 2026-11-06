import time

from pages.contacts_page import ContactsPage
from pages.add_contact_page import AddContactPage
from utils.factory import random_contact
import pytest

count_contacts_before = 0

@pytest.fixture
def add_page(contacts_page: ContactsPage) -> AddContactPage:
    global count_contacts_before
    count_contacts_before = contacts_page.count_contacts()
    contacts_page.click_link_add()
    return AddContactPage(contacts_page.page)

def test_add_new_contact_positive(contacts_page: ContactsPage, add_page: AddContactPage):
    add_page.type_add_contact_form(random_contact())
    add_page.click_btn_save()
    global count_contacts_before
    exp = count_contacts_before + 1
    assert contacts_page.count_contacts() == exp

def test_add_new_contact_positive_check_last_contact(contacts_page: ContactsPage, add_page: AddContactPage):
    add_page.type_add_contact_form(random_contact())
    add_page.click_btn_save()
    time.sleep(3)

    assert ContactsPage(add_page.page).validate_text_in_last_contacts(random_contact().phone)

