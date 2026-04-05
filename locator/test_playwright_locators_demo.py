from playwright.sync_api import Page, expect


def test_pwlocators(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(3000)

    # get_by_alt_text
    # logo = page.get_by_alt_text("nopCommerce demo store")
    # expect(logo).to_be_visible()

    # # get_by_text()
    # expect(page.get_by_text("Welcome to our store")).to_be_visible()
    # expect(page.get_by_text("Welcome to")).to_be_visible()

    # # get_by_role() : role對應要看官方對應表
    # expect(page.get_by_role("button", name="Computers")).to_be_visible()

    # get_by_label #label顯示給user的名稱
    page.get_by_label("Excellent").set_checked(True)
    page.wait_for_timeout(3000)

    # get_by_placeholder()
    page.get_by_placeholder("Search store").fill("Apple MacBook Pro 13-inch")
    page.wait_for_timeout(3000)

    # get_by_title()
    expect(page.get_by_title("Show products in category Electronics")
           ).to_have_text("Electronics")
    page.wait_for_timeout(3000)
