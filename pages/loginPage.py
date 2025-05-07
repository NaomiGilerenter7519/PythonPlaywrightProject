from playwright.sync_api import Page, expect
import allure
base_url = "https://www.saucedemo.com/"


class LoginPage:
    def __init__(self,page:Page):
        self.__page=page
        self.__username_txtfield=page.locator("[data-test=\"username\"]")
        self.__password_txtfiled=page.get_by_placeholder("Password")
        self.__login_button=page.get_by_role("button",name="Login")
        self.__error_message=page.locator("[data-test=\"error\"]")
    def navegate_to(self,url:str):
        with allure.step(f"navigating to url:{url}"):
         self.__page.goto(url)

    def login_to_application(self,username:str,password:str):
        with allure.step(f"login to app sith parameters:{username}:{password}"):
            self.__username_txtfield.fill(username)
            self.__password_txtfiled.press_sequentially(password, delay=100)
            self.__login_button.click()

    def validat_error_messege(self,error_message):
        with allure.step(f"Validating that error message is: '{error_message}'"):
            expect(self.__error_message).to_contain_text(error_message)

    def validate_page_url(self,page_url:str):
        expect(self.__page).to_have_url(page_url)

