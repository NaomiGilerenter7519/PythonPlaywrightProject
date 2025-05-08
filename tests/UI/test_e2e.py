import re
from playwright.sync_api import Page, expect
from tests.conftest import login_page

def test_end_2_end(page: Page,login_page) -> None:
    page.goto("https://www.saucedemo.com/")

    login_page.login_to_application("standard_user","secret_sauce")

    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("3")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"title\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    page.get_by_text("Sauce Labs Bolt T-ShirtGet").click(button="right")
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("alex")
    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("komanov11")
    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("12")
    expect(page.locator("[data-test=\"lastName\"]")).to_be_visible()
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"payment-info-label\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shipping-info-label\"]")).to_contain_text("Shipping Information:")
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    expect(page.locator("[data-test=\"complete-header\"]")).to_be_visible()
    page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    page.wait_for_timeout(6000)