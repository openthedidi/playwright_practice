from playwright.sync_api import Playwright
import pytest


base_url = "https://restful-booker.herokuapp.com"

# scope="session" 表示整個測試 session 只建立一次，所有測試共用同一個 context
booking_id = ''


@pytest.fixture(scope="session")
# 接收 Playwright 實例作為參數（由 pytest-playwright 自動注入）
def request_context(playwright: Playwright):
    context = playwright.request.new_context()  # 建立一個 API 請求的 context，可用來發送 HTTP 請求
    yield context  # 將 context 提供給測試使用；yield 之前是 setup，之後是 teardown
    context.dispose()  # 測試結束後釋放 context，清理資源


def test_create_booking(request_context):
    global booking_id
    global first_name
    global last_name
    first_name = "Jim"
    last_name = "Brown"

    requst_body = {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = request_context.post(f"{base_url}/booking", data=requst_body)
    response_body = response.json()
    print(response_body)
    booking_id = response_body["bookingid"]
    assert response.status == 200
    assert response.ok, "response is not ok"
    assert response_body["booking"]["firstname"] == "Jim"
    assert response_body["booking"]["lastname"] == "Brown"


# def test_get_booking_details_by_id(request_context):
#     response = request_context.get(f"{base_url}/booking/{booking_id}")
#     response_body = response.json()
#     print(response_body)
#     assert response.status == 200
#     assert response.ok, "response is not ok"
#     assert response_body["firstname"] == "Jim"


def test_get_booking_details_by_name(request_context):
    name_params = {
        "firstname": first_name,
        "lastname": last_name
    }

    # response = request_context.get(
    #     f"{base_url}/booking?firstname={first_name}&lastname={last_name}")

    response = request_context.get(f"{base_url}/booking", params=name_params)
    response_body = response.json()
    print(response_body)
    assert response.status == 200
    assert response.ok, "response is not ok"
    for booking in response_body:
        if booking_id == booking["bookingid"]:
            assert True
            break


def test_create_testing_token(request_context):
    global user_token
    requst_body = {
        "username": "admin",
        "password": "password123"
    }
    response = request_context.post(f"{base_url}/auth", data=requst_body)
    response_body = response.json()
    print(response_body)
    user_token = response_body["token"]


def test_update_booking(request_context):
    requst_body = {
        "firstname": "Jim",
        "lastname": "Marry",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-02-01",
            "checkout": "2019-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = request_context.put(
        f"{base_url}/booking/{booking_id}",
        data=requst_body,
        headers={"Cookie": "token=" + user_token}
    )
    assert response.status == 200
    response_body = response.json()
    print(response_body)
    assert response_body["firstname"] == "Jim"
    assert response_body["lastname"] == "Marry"
    assert response_body["bookingdates"]["checkin"] == "2018-02-01"


# def test_partial_update_booking(request_context):
#     requst_body = {
#         "bookingdates": {
#             "checkin": "2018-03-01",
#             "checkout": "2019-02-01"
#         }
#     }
#     response = request_context.put(
#         f"{base_url}/booking/{booking_id}",
#         data=requst_body,
#         headers={"Cookie": "token=" + user_token}
#     )
#     assert response.status == 200
#     response_body = response.json()
#     print(response_body)
#     assert response_body["bookingdates"]["checkin"] == "2018-03-01"


def test_delete_booking(request_context):
    response = request_context.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": "token=" + user_token}
    )
    assert response.status == 201
    check_response = request_context.get(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": "token=" + user_token}
    )
    assert check_response.status == 404
