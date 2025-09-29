import datetime

from schema.pydantic_models.session import (
    SessionCostWeighted,
    SessionCostEqually,
    NewSession,
)
from services.sessions import PracticeSessionService
from common.enum import BillingTypes


def get_all_sessions(**kwargs):
    sessions = PracticeSessionService.get_all_sessions()
    return {"data": sessions}


def get_session_templates(**kwargs):
    session_templates = PracticeSessionService.get_session_templates()
    return {"data": session_templates}


def get_session_attributes_data(**kwargs):
    """
    Get all attributes data for session
    """
    return {
        "data": {
            "billingTypes": PracticeSessionService.get_billing_types(),
            "sessionTemplates": PracticeSessionService.get_session_templates(),
        }
    }


def add_session(**kwargs):
    new_session = NewSession(**kwargs)
    session_id = PracticeSessionService.add_session(new_session.model_dump())
    return {"data": {"sessionId": session_id}}


def calc_cost_api_logic(**kwargs):
    session_data = SessionCostWeighted(**kwargs)
    bill_result = PracticeSessionService(
        BillingTypes.WEIGHTED.value, session_data
    ).calc_cost_amount()
    return {
        "data": {
            "cost": bill_result,
            "sessionDate": datetime.date.today().strftime("%Y-%m-%d"),
        }
    }


def calc_cost_equally(**kwargs):
    session_data = SessionCostEqually(**kwargs)
    bill_result = PracticeSessionService(
        BillingTypes.EQUALLY.value, session_data
    ).calc_cost_amount()

    return {
        "data": {
            "cost": bill_result,
            "sessionDate": datetime.date.today().strftime("%Y-%m-%d"),
        }
    }


def get_billing_types(**kwargs):
    billing_types = PracticeSessionService.get_billing_types()

    return {"data": billing_types}
