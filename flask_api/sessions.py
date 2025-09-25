from flask import request, Blueprint

from api_logic.sessions import calc_cost_api_logic, get_session

session_router = Blueprint('session', __name__)

@session_router.route('', methods=['GET'])
def get_session_route():
    return get_session()

@session_router.route('/calc-cost', methods=['POST'])
def calc_cost():
    data = request.json
    return calc_cost_api_logic(**data)
