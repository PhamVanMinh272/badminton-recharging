import datetime

from schema.pydantic_models.session import SessionCreate, SessionCostEqually
from services.sessions import Session
from common.enum import BillingTypes

def get_session(**kwargs):
    return {"data": {
        "message": "Session endpoint is working",
        "sessionDate": datetime.date.today().strftime("%Y-%m-%d")
    }}

def calc_cost_api_logic(**kwargs):
    session_data = SessionCreate(**kwargs)
    bill_result = Session(BillingTypes.WEIGHTED, session_data).calc_cost_amount()
    return {"data": {
        "cost": bill_result,
        "sessionDate": datetime.date.today().strftime("%Y-%m-%d")
    }}


def calc_cost_equally(**kwargs):
    session_data = SessionCostEqually(**kwargs)
    bill_result = Session(BillingTypes.EQUALLY, session_data).calc_cost_amount()

    return {"data": {
        "cost": bill_result,
        "sessionDate": datetime.date.today().strftime("%Y-%m-%d")
    }}