from playwright.sync_api import Page, expect


def test_name_field_fill(page: Page):
    """測試姓名欄位可以正常輸入"""
    page.goto("https://www.nanshanlife.com.tw/nanshanlife/contact-us")

    name_input = page.get_by_placeholder("請輸入真實姓名")

    # 驗證欄位可見
    expect(name_input).to_be_visible()

    # 填入姓名
    name_input.fill("王小明")

    # 驗證填入的值正確
    expect(name_input).to_have_value("王小明")


def test_name_field_clear(page: Page):
    """測試姓名欄位清除後為空"""
    page.goto("https://www.nanshanlife.com.tw/nanshanlife/contact-us")

    name_input = page.get_by_placeholder("請輸入真實姓名")
    name_input.fill("王小明")
    name_input.clear()

    expect(name_input).to_have_value("")


def test_name_field_is_empty_on_load(page: Page):
    """測試頁面載入時姓名欄位預設為空"""
    page.goto("https://www.nanshanlife.com.tw/nanshanlife/contact-us")

    name_input = page.get_by_placeholder("請輸入真實姓名")

    expect(name_input).to_be_empty()
