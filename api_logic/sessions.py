import datetime

from schema.pydantic_models.session import SessionCreate
from services.sessions import Session

def get_session(**kwargs):
    return {"data": {
        "message": "Session endpoint is working",
        "sessionDate": datetime.date.today().strftime("%Y-%m-%d")
    }}

def calc_cost_api_logic(**kwargs):
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