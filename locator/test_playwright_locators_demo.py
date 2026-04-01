from playwright.sync_api import Page, expect


def test_pwlocators(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(3000)

    # get_by_alt_text
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    # get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()
    expect(page.get_by_text("Welcome to")).to_be_visible()

    # get_by_role()
    expect(page.get_by_role("button", name="Computers")).to_be_visible()
