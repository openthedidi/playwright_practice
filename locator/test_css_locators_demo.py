from playwright.sync_api import Page, expect


def test_csslocators(page: Page):
    page.goto(
        "https://ilp.nanshanlife.com.tw/main.html?sUrl=$W$ANNOUNCE$ANNOUNCELIST]DJHTM{TYPEID}ACCOUNT")
    page.wait_for_timeout(1000)

    # tag & id -> tag#id
    page.locator(
        "input#search").fill("test")
    page.wait_for_timeout(3000)

    # tag & class -> tag.class
    page.locator("a.logo").click()
    page.wait_for_timeout(3000)

    # tag & attribute -> tag[attribute]
    page.frame_locator("iframe[name=mainframe]").locator(
        "select[name=dataTbl_length]").select_option("100")
    page.wait_for_timeout(3000)

    # tag & class & attribute -> tag.class[attribute]
    page.frame_locator("iframe[name=mainframe]").locator(
        "input.form-control.input-sm[aria-controls=dataTbl]").fill("test")
    page.wait_for_timeout(3000)

    page.locator(
        "input#search").fill("test")
    page.wait_for_timeout(3000)
    page.locator(
        "button[type=submit][class='search-btn btn absolute quickSearch-submit']").click()
    page.wait_for_timeout(3000)
