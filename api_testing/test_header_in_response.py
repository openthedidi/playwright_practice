from playwright.sync_api import Playwright, expect


def test_headers_in_response(playwright: Playwright):
    request_context = playwright.request.new_context()
    response = request_context.get(
        "https://www.nanshanlife.com.tw/nanshanlife/index.html")
    assert response.ok, "response is not ok"
    assert response.status == 200

    headers = response.headers

    content_type = headers.get("content-type")
    assert content_type == "text/html; charset=UTF-8"
    assert "cache-control" in headers

    request_context.dispose()
