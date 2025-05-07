import re
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
import utils.configs as configs
import allure

@allure.feature("Login")
@allure.story("happy scenarios")
def test_sanity_login(page: Page,login_page,proudocts_page) -> None:
    login_page.navegate_to(configs.base_url)
    login_page.login_to_application("standard_user", "secret_sauce")
    page.wait_for_timeout(2000)
    # proudocts_page.validate_primary_header_aria_snapshot()
    # proudocts_page.validate_secondary_header_aria_snapshot()
    proudocts_page.validate_shopping_cart_is_visibale()
    proudocts_page.validate_page_url(configs.proudcts_url)

    page.wait_for_timeout(2000)

