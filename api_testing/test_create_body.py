from playwright.sync_api import Playwright, expect
import json
from faker import Faker
from datetime import datetime
from datetime import timedelta


def test_create_booking(playwright: Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()

    # 第一種資料來源 from doc
    # request_body = {
    #     "firstname": "Jim",
    #     "lastname": "Brown",
    #     "totalprice": 111,
    #     "depositpaid": True,
    #     "bookingdates": {
    #         "checkin": "2018-01-01",
    #         "checkout": "2019-01-01"
    #     },
    #     "additionalneeds": "Breakfast"
    # }

    # 第二種資料來源 from file
    # request_body_text = open(file="./api_testing/request_body.txt").read()
    # request_body = json.loads(request_body_text)

    # 第三種資料來源 from faker

    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    total_price = faker.random_int(min=10, max=1000)
    deposit_paid = faker.boolean()
    check_in = datetime.now().strftime("%Y-%m-%d")
    check_out = (datetime.now() + timedelta(days=10)
                 ).strftime("%Y-%m-%d")
    additional_needs = faker.word()

    request_body = {
        "firstname": first_name, "lastname": last_name, "totalprice": total_price, "depositpaid": deposit_paid, "bookingdates": {
            "checkin": check_in, "checkout": check_out
        }, "additionalneeds": additional_needs
    }

    print(request_body)

    response = request_context.post(f"{base_url}/booking", data=request_body)
    response_body = response.json()
    print(response_body)

    # valitation
    # expect() 是 Playwright 的斷言函式，它只接受這三種型別：
    # Page
    # Locator
    # APIResponse
    expect(response).to_be_ok()

    assert response.status == 200
    assert response_body["booking"]["firstname"] == first_name
    assert response_body["booking"]["lastname"] == last_name
    assert response_body["booking"]["additionalneeds"] == additional_needs
    assert response_body["booking"]["bookingdates"]["checkin"] == check_in
    # close context
    request_context.dispose()
