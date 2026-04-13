from playwright.sync_api import Page, expect
from datetime import datetime

CHINESE_MONTHS = {
    "一月": 1, "二月": 2, "三月": 3, "四月": 4,
    "五月": 5, "六月": 6, "七月": 7, "八月": 8,
    "九月": 9, "十月": 10, "十一月": 11, "十二月": 12,
}


def get_current_month(page: Page):
    """從 .dpicker__current-month 讀取目前顯示的第一個月份，回傳 (year, month)"""
    # picker 同時顯示兩個月，取第一個
    text = page.locator(".dpicker__current-month").first.text_content().strip()
    # 格式: "2026 年 四月"
    parts = text.split()           # ["2026", "年", "四月"]
    year = int(parts[0])
    month = CHINESE_MONTHS[parts[2]]
    return year, month


def click_date(page: Page, target_year: int, target_month: int, target_day: int):
    """導航到目標月份並點擊目標日期"""
    next_btn = page.locator('button[aria-label="Next Month"]')
    prev_btn = page.locator('button[aria-label="Previous Month"]')
    target_month_label = f"month  {target_year}-{target_month:02d}"

    while True:
        month_container = page.locator(f'[aria-label="{target_month_label}"]')
        if month_container.count() > 0 and month_container.is_visible():
            break

        # 從 .dpicker__current-month 判斷目前第一個月份，先對年再對月
        current_year, current_mon = get_current_month(page)

        if current_year != target_year:
            if current_year < target_year:
                next_btn.click()
            else:
                prev_btn.click()
        else:
            if current_mon < target_month:
                next_btn.click()
            else:
                prev_btn.click()

    # 在目標月份內點擊對應日期
    # 日期用 CSS class dpicker__day--{day:03d} 定位，排除跨月灰色日期和不可選日期
    month_container = page.locator(f'[aria-label="{target_month_label}"]')
    month_container.locator(
        f'.dpicker__day--{target_day:03d}'
        f':not(.dpicker__day--outside-month)'
        f':not([aria-disabled="true"])'
    ).click()


def test_bootstrap_date_picker(page: Page):
    target_start_date = "2026-5-28"
    target_end_date = "2026-6-2"

    start_dt = datetime.strptime(target_start_date, "%Y-%m-%d")
    end_dt = datetime.strptime(target_end_date, "%Y-%m-%d")

    page.goto("https://packages.eztravel.com.tw/")

    check_in_date_input = page.locator(
        "#package-search-hotel-dates-select-start")
    check_out_date_input = page.locator(
        "#package-search-hotel-dates-select-end")

    # 開啟入住日期選擇器
    check_in_date_input.click()

    # 選擇入住日期
    click_date(page, start_dt.year, start_dt.month, start_dt.day)

    # 選擇退房日期（picker 選完入住後仍保持開啟）
    click_date(page, end_dt.year, end_dt.month, end_dt.day)

    # 驗證兩個欄位皆已填入值
    expect(check_in_date_input).not_to_have_value("")
    expect(check_out_date_input).not_to_have_value("")
