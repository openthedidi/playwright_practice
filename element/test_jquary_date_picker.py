from playwright.sync_api import Page, expect
from datetime import datetime


def test_data_picker(page: Page):
    target_date = "2025/11/30"

    # Parse target date
    target_dt = datetime.strptime(target_date, "%Y/%m/%d")
    target_year = target_dt.year
    target_month = target_dt.month  # 1-12
    target_day = target_dt.day

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    page.goto("https://testautomationpractice.blogspot.com/")
    date_picker_input = page.locator("#datepicker")
    date_picker_input.click()

    prev_month_btn = page.locator("a[data-handler=prev]")
    next_month_btn = page.locator("a[data-handler=next]")
    present_month_on_data_picker = page.locator("span.ui-datepicker-month")
    present_year_on_data_picker = page.locator("span.ui-datepicker-year")

    # 導航到目標月份/年份
    while True:
        current_month_text = present_month_on_data_picker.text_content()
        current_year_text = present_year_on_data_picker.text_content()

        current_month = months.index(current_month_text) + 1  # 1-12
        current_year = int(current_year_text)

        if current_year == target_year and current_month == target_month:
            break
        elif (current_year, current_month) < (target_year, target_month):
            next_month_btn.click()
        else:
            prev_month_btn.click()

    # 點擊目標日期（排除其他月份的灰色日期）
    date_table_tbody = page.locator("table.ui-datepicker-calendar").locator("tbody")
    date_table_tbody.locator(
        f"td:not(.ui-datepicker-other-month) a:text-is('{target_day}')"
    ).click()

    # 驗證 input 值格式為 mm/dd/yyyy
    expected_value = target_dt.strftime("%m/%d/%Y")
    expect(date_picker_input).to_have_value(expected_value)
