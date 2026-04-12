from playwright.sync_api import Playwright, expect
import base64

# test basic auths


def test_basic_auth(playwright: Playwright):
    credential = base64.b64encode(b"admin:admin").decode("utf-8")

    # 這個 context 發出的所有 request 都會帶上這個 heade
    request_context = playwright.request.new_context(
        extra_http_headers={"Authorization": "Basic " + credential})

    response = request_context.get(
        "https://the-internet.herokuapp.com/basic_auth")

    # 只有這次 request 會帶上此 header（單次指定）
    # response = request_context.get(
    #     "https://the-internet.herokuapp.com/basic_auth", headers={"Authorization": f"Basic {credential}"})

    assert response.status == 200
    request_context.dispose()
