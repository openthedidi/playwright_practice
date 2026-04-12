from playwright.sync_api import Playwright, expect


def test_bearer_token_auth(playwright: Playwright):
    token = ""

    request_context = playwright.request.new_context()
    response = request_context.get(
        "https://esg.com/GetPersonalConfig", headers={"Authorization": f"Bearer {token}"})

    assert response.status == 200
    request_context.dispose()
