from playwright.sync_api import Page, expect

# static web table


def test_static_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("table[name=BookTable]")
    expect(table).to_be_visible()

    # 表格行
    rows = table.locator("tr")
    expect(rows).to_have_count(7)

    # 表格列
    columns = table.locator("th")
    expect(columns).to_have_count(4)

    # 取第1row的標頭
    first_row_header = rows.nth(1).locator("td")
    expect(first_row_header).to_have_count(4)
    expect(first_row_header.nth(0)).to_have_text("Learn Selenium")
    expect(first_row_header.nth(1)).to_have_text("Amit")

    # 取Subject第3column的文字
    subject_cells = table.locator("tr td:nth-child(3)")
    expect(subject_cells).to_have_text(["Selenium", "Java", "Javascript", "Selenium", "JAVA", "Javascript"])

    # 取全部的文字
    all_cells = table.locator("tr td")
    expect(all_cells).to_have_text([
        "Learn Selenium", "Amit", "Selenium", "300",
        "Learn Java", "Mukesh", "Java", "500",
        "Learn JS", "Animesh", "Javascript", "300",
        "Master In Selenium", "Mukesh", "Selenium", "3000",
        "Master In Java", "Amod", "JAVA", "2000",
        "Master In JS", "Amit", "Javascript", "1000",
    ])

    # 取Mukesh的文字
    mukesh_cells = table.locator("tr td", has_text="Mukesh")
    expect(mukesh_cells).to_have_count(2)
