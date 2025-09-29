from flask import request, Blueprint

from api_logic import sessions


session_router = Blueprint("session", __name__)


@session_router.route("", methods=["GET"])
def get_all_sessions():
    return sessions.get_all_sessions()


@session_router.route("", methods=["POST"])
def add_session():
    return sessions.add_session(**request.json)


@session_router.route("/templates", methods=["GET"])
def get_session_templates():
    return sessions.get_session_templates()


@session_router.route("/attributes-data", methods=["GET"])
def get_session_attributes_data():
    return sessions.get_session_attributes_data()


@session_router.route("/calc-cost-weighted", methods=["POST"])
def calc_cost_weighted():
    data = request.json
    return sessions.calc_cost_api_logic(**data)


@session_router.route("/calc-cost-equally", methods=["POST"])
def calc_cost_equally():
    data = request.json
    return sessions.calc_cost_equally(**data)


@session_router.route("/billing-types", methods=["GET"])
def get_billing_types():
    return sessions.get_billing_types()
