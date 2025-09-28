import datetime

from schema.pydantic_models.session import SessionCostWeighted, SessionCostEqually
from services.sessions import PracticeSessionService
from common.enum import BillingTypes


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
