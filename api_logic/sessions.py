import datetime

from schema.pydantic_models.session import (
    SessionCostWeighted,
    SessionCostEqually,
    NewSession,
)
from services.sessions import PracticeSessionService
from common.enum import BillingTypes
from common.db_connection import db_context_manager


@db_context_manager
def get_all_sessions(conn, **kwargs):
    sessions = PracticeSessionService(conn).get_all_sessions()
    return {"data": sessions}


@db_context_manager
def get_session_templates(conn, **kwargs):
    session_templates = PracticeSessionService(conn).get_session_templates()
    return {"data": session_templates}


@db_context_manager
def get_session_attributes_data(conn, **kwargs):
    """
    Get all attributes data for session
    """
    return {
        "data": {
            "billingTypes": PracticeSessionService(conn).get_billing_types(),
            "sessionTemplates": PracticeSessionService(conn).get_session_templates(),
        }
    }


@db_context_manager
def add_session(conn, **kwargs):
    new_session = NewSession(**kwargs)
    session_id = PracticeSessionService(conn).add_session(new_session.model_dump())
    return {"data": {"sessionId": session_id}}


@db_context_manager
def calc_cost_api_logic(conn, **kwargs):
    session_data = SessionCostWeighted(**kwargs)
    bill_result = PracticeSessionService(
        conn, BillingTypes.WEIGHTED.value, session_data
    ).calc_cost_amount()
    return {
        "data": {
            "cost": bill_result,
            "sessionDate": datetime.date.today().strftime("%Y-%m-%d"),
        }
    }


@db_context_manager
def calc_cost_equally(conn, **kwargs):
    session_data = SessionCostEqually(**kwargs)
    bill_result = PracticeSessionService(
        conn, BillingTypes.EQUALLY.value, session_data
    ).calc_cost_amount()

    return {
        "data": {
            "cost": bill_result,
            "sessionDate": datetime.date.today().strftime("%Y-%m-%d"),
        }
    }


@db_context_manager
def get_billing_types(conn, **kwargs):
    billing_types = PracticeSessionService(conn).get_billing_types()

    return {"data": billing_types}
