import datetime
import json

from fast_api.sessions import get_session
from schema.pydantic_models.session import SessionCreate
from services.sessions import Session
from common.api_utils import exception_handler


def calc_cost_func(**kwargs):
    session_data = SessionCreate(**kwargs)
    session = Session(session_data.players)
    cost = session.cost_amount(
        rental_cost=session_data.rentalCost,
        shuttle_amount=session_data.shuttleAmount,
        shuttle_price=session_data.shuttlePrice
    )

    return {"data": {
        "cost": session.cost_per_person(cost),
        "sessionDate": datetime.date.today().strftime("%Y-%m-%d")
    }}

@exception_handler
def lambda_handler(event, context):

    get_paths = {
        "/sessions": get_session,
    }
    post_paths = {
        "/sessions/calc-cost": calc_cost_func,
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