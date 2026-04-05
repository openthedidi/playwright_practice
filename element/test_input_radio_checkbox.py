from playwright.sync_api import Page, expect


# def test_input(page: Page):
#     page.goto("https://www.eztravel.com.tw/")

#     country_input = page.locator("#search-flight-arrival-0")
#     expect(country_input).to_be_visible()
#     expect(country_input).to_be_enabled()
#     expect(country_input).to_have_attribute("placeholder", "輸入國家/城市/機場關鍵字")
#     country_input.fill("日本")
#     enter_value = country_input.input_value()
#     print("enter_value:", enter_value)


# def test_radio(page: Page):
#     page.goto("https://www.eztravel.com.tw/")
#     singel_ticket_radio = page.get_by_role("radio", name="單程")
#     expect(singel_ticket_radio).to_be_visible()
#     expect(singel_ticket_radio).to_be_enabled()
#     singel_ticket_radio.check()
#     expect(singel_ticket_radio).to_be_checked()


def test_checkbox(page: Page):
    page.goto("https://www.eztravel.com.tw/")
    # 目前常見的自訂樣式解法
    # direct_fly_checkbox = page.locator("label[for='check-isDirectfly']")
    # direct_fly_checkbox.click()
    # expect(direct_fly_checkbox).to_be_checked()

    # 多選項目檢查
    checkboxs_texts = page.locator(
        "div[class='Engine_OtherOptionBox__6Rg1a']>label>span")
    expect(checkboxs_texts).to_have_count(2)
    expect(checkboxs_texts).to_contain_text(["直飛", "比較7天最低價"])

    # 一次全選
    checkboxs = page.locator(
        "div[class='Engine_OtherOptionBox__6Rg1a']>label")
    expect(checkboxs).to_have_count(2)

    # .all可以把複數locators轉為list
    for checkbox in checkboxs.all():
        checkbox.click()
        expect(checkbox).to_be_checked()

    for checkbox in checkboxs.all():
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
