
from playwright.sync_api import Page, expect


def test_negative(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"login-credentials\"]").dblclick()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out")
    expect(page).to_have_url("https://www.saucedemo.com/")
    page.wait_for_timeout(2000)