from playwright.sync_api import Playwright, expect
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# 要先裝jsonschema


def validate_json_schema(response_json, resp_schema):
    try:
        validate(instance=response_json, schema=resp_schema)
        print("validate success")
        return True
    except ValidationError as e:
        print(e)
        return False


def test_header_in_response(playwright: Playwright):
    response_json_schema = {
        "type": "object",
        "properties": {
            "header": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string"
                    },
                    "message": {
                        "type": "string"
                    }
                },
                "required": [
                    "code",
                    "message"
                ]
            },
            "datas": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string"
                        },
                        "url": {
                            "type": "object",
                            "properties": {
                                "url": {
                                    "type": "string"
                                },
                                "url_blank": {
                                    "type": "boolean"
                                },
                                "url_type": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "url",
                                "url_blank",
                                "url_type"
                            ]
                        },
                        "sub_title": {
                            "type": "string"
                        },
                        "picture": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "title",
                        "url",
                        "sub_title",
                        "picture"
                    ]
                }
            },
            "page_info": {
                "type": "object",
                "properties": {
                    "total_page_size": {
                        "type": "number"
                    },
                    "total_rec_size": {
                        "type": "number"
                    },
                    "page": {
                        "type": "number"
                    },
                    "page_size": {
                        "type": "number"
                    }
                },
                "required": [
                    "total_page_size",
                    "total_rec_size",
                    "page",
                    "page_size"
                ]
            }
        },
        "required": [
            "header",
            "datas",
            "page_info"
        ]
    }

    request_context = playwright.request.new_context(
        extra_http_headers={"content-type": "application/json"})
    response = request_context.get(
        "https://www.nanshanlife.com.tw/nanshanlife/portal-api/DataSource/link/sales")
    response_json = response.json()
    print(response_json)
    assert response.status == 200

    assert validate_json_schema(response_json, response_json_schema)

    request_context.dispose()
