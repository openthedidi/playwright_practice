from playwright.sync_api import Page, expect

# dynamic web table


def test_dynamic_table(page: Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table = page.locator("table.table.table-striped")
    expect(table).to_be_visible()

    table_tbody = table.locator("tbody")
    expect(table_tbody).to_be_visible()

    tbody_rows = table_tbody.locator("tr")
    expect(tbody_rows).to_have_count(4)

    ie_cpu = ''

    for row in tbody_rows.all():
        first_name_cell = row.locator("td:nth-child(1)")
        expect(first_name_cell).to_be_visible()
        if first_name_cell.text_content() == "Chrome":
            ie_cpu = row.locator("td:has-text('%')").inner_text()
            print(ie_cpu)
            break

    expect(page.locator("#chrome-cpu")).to_contain_text(ie_cpu)
