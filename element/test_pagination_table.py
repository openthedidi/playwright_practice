from playwright.sync_api import Page, expect


def test_dynamic_table(page: Page):
    page.goto("https://datatables.net/examples/basic_init/zero_configuration.html")

    table = page.locator("table#example")

    has_next = True

    while has_next:
        tbody = table.locator("tbody")
        expect(tbody).to_be_visible()
        rows = tbody.locator("tr")
        row_datas = rows.all()
        table_next_page_btn = page.locator("button[aria-label=Next]")
        class_attribute_str = table_next_page_btn.get_attribute("class")
        for row in row_datas:
            first_name_cell = row.locator("td:nth-child(1)")
            expect(first_name_cell).to_be_visible()
            print(first_name_cell.text_content())

        if 'disabled' not in class_attribute_str:
            table_next_page_btn.click()
        else:
            has_next = False
