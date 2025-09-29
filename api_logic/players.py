from settings import logger
from services.players import PlayerService
from common.db_connection import db_context_manager


@db_context_manager
def get_players(conn, **kwargs):
    players = PlayerService(conn).get_players()
    logger.info(f"Fetched players: {players}")
    return {"data": players}
