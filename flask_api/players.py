from flask import Blueprint

from api_logic import players

players_router = Blueprint("player", __name__)


@players_router.route("", methods=["GET"])
def get_players():
    return players.get_players()
