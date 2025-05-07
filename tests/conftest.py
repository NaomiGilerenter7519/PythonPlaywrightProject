import pytest
from playwright.sync_api import Page

from pages.loginPage import LoginPage
from  pages.productsPage import ProductsPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def proudocts_page(page:Page):
    return ProductsPage(page)