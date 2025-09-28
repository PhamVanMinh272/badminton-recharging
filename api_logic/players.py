from settings import logger
from services.players import PlayerService


def get_players(**kwargs):
    players = PlayerService().get_players()
    logger.info(f"Fetched players: {players}")
    return {"data": players}
