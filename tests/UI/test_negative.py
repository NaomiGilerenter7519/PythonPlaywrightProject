
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from tests.conftest import login_page
import utils.configs as configs
import allure
from allure_commons.types import AttachmentType

@allure.feature("Login")
@allure.story("negative scenarios")
@allure.title("Login with locked out")
def test_negative(page: Page,login_page):
    login_page.navegate_to(configs.base_url)
    login_page.login_to_application("locked_out_user","secret_sauce")
    login_page.validat_error_messege("Epic sadface: Sorry, this user has been locked out")
    login_page.validate_page_url(configs.base_url)
    allure.attach(page.screenshot())
    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(2000)
