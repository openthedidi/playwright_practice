from playwright.sync_api import Playwright, expect


def test_api_key(playwright: Playwright):
    request_context = playwright.request.new_context()

    query_params = {
        "apikey": "fe9c5cddb7e01d747b4611c3fc9eaf2c",
        "q": "london"
    }

    response = request_context.get(
        "https://api.openweathermap.org/data/2.5/weather", params=query_params)

    assert response.status == 200
    request_context.dispose()
