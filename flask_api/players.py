from flask import request, Blueprint

from api_logic import sessions

players_router = Blueprint('player', __name__)

@players_router.route('', methods=['GET'])
def get_players():
    return sessions.get_session()

