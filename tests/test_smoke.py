import pytest
from playwright.sync_api import Page, expect

def test_open_home(page: Page):
    page.goto("https://telranedu.web.app/home")
    expect(page.locator("//a[text()='LOGIN']")).to_be_visible()