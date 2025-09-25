import json

from api_logic import sessions
from common.api_utils import exception_handler


@exception_handler
def lambda_handler(event, context):

    get_paths = {
        "/sessions": sessions.get_session,
    }
    post_paths = {
        "/sessions/calc-cost-weighted": sessions.calc_cost_api_logic,
        "/sessions/calc-cost-equally": sessions.calc_cost_equally,
    }

    path = event.get("path", "")
    method = event.get("httpMethod", "GET")
    body = json.loads(event.get("body", "{}"))
    if method == "GET":
        paths = get_paths
    elif method == "POST":
        paths = post_paths
    else:
        raise Exception("Method Not Allowed")
    if path in paths:
        function_name = paths[path]
        result = function_name(**body)
    else:
        raise Exception("Not found")
    return result

if __name__ == '__main__':
    event = {
        "body": json.dumps({
            "players": [
                "Đạt", "Thảo", "Văn", "Huy", "Vu", "Thinh"
            ],
            "rentalCost": 200, "shuttleAmount": 3, "shuttlePrice": 26}),
        "path": "/sessions/calc-cost",
        "httpMethod": "POST"
    }
    response = lambda_handler(event, None)
    print(response)