import json

from api_logic import sessions
from common.api_utils import exception_handler
from settings import logger


@exception_handler
def lambda_handler(event, context):

    get_paths = {
        "/api/sessions/templates": sessions.get_session_templates,
        "/api/sessions/billing-types": sessions.get_billing_types,
        "/api/sessions/attributes-data": sessions.get_session_attributes_data,
        "/api/sessions": sessions.get_all_sessions,
    }
    post_paths = {
        "/api/sessions/calc-cost-weighted": sessions.calc_cost_api_logic,
        "/api/sessions/calc-cost-equally": sessions.calc_cost_equally,
        "/api/sessions": sessions.add_session,
    }

    path = event.get("path", "")
    logger.info(f"Path: {path}")
    method = event.get("httpMethod", "GET")
    body = json.loads(event.get("body", "{}") or "{}")
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


if __name__ == "__main__":
    event = {
        "body": json.dumps(
            {
                "players": ["Đạt", "Thảo", "Văn", "Huy", "Vu", "Thinh"],
                "numberOfPlayers": 6,
                "rentalCost": 200,
                "shuttleAmount": 3,
                "shuttlePrice": 26,
            }
        ),
        "path": "/api/sessions/attributes-data",
        "httpMethod": "GET",
    }
    response = lambda_handler(event, None)
    body = response["body"]
    body_json = json.loads(body)
    print(json.dumps(body_json, indent=4, ensure_ascii=False))
