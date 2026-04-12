from playwright.sync_api import Playwright, expect


def test_cookies_in_response(playwright: Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get(
        "https://www.youtube.com/?gl=TW")
    assert response.ok, "response is not ok"
    assert response.status == 200

    cookies = request_context.storage_state()["cookies"]

    gps_cookie = None

    for cookie in cookies:
        if cookie["name"] == "GPS":
            gps_cookie = cookie
            break

    assert gps_cookie is not None
    assert gps_cookie["value"] == "1"
    assert gps_cookie["domain"] == ".youtube.com"

    request_context.dispose()
