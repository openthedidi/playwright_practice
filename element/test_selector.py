from playwright.sync_api import Page, expect

# select demo


def test_select_with_option_label(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    country_selector = page.locator("#country")
    expect(country_selector).to_be_visible()
    expect(country_selector).to_be_enabled()

    # 用web上的值來指定選項
    country_selector.select_option(label="United States")
    expect(country_selector).to_have_value("usa")

    # 用option上的value來指定
    country_selector.select_option(value="uk")
    expect(country_selector).to_have_value("uk")

    # 用index
    country_selector.select_option(index=1)
    expect(country_selector).to_have_value("canada")

    # 檢查選項數量
    coutry_options = country_selector.locator("option")
    expect(coutry_options).to_have_count(10)

    # print選項名稱
    for option in coutry_options.all():
        print(option.text_content())


def test_hidden_selection_options(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()

    page.get_by_text("PIM").click()

    employment_status_selector_btn = page.locator(
        "div.oxd-select-text--after").nth(0)
    expect(employment_status_selector_btn).to_be_visible()
    employment_status_selector_btn.click()

    option_freelance = page.get_by_role("listbox").get_by_text("Freelance")
    option_freelance.click()
    expect(page.locator("div.oxd-select-text-input").nth(0)
           ).to_have_text("Freelance")
