from playwright.sync_api import Page, expect


def test_verifyPageUrl(page: Page):
    page.goto("https://www.saucedemo.com/")
    myurl = page.url
    expect(page).to_have_url("https://www.saucedemo.com/")
    print(myurl)


def test_verifyPageTitle(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    print(page.title())
