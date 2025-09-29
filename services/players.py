from data_repo.player_repo import PlayerRepo


class PlayerService:
    def __init__(self, conn):
        self._conn = conn
        self.players = PlayerRepo(self._conn).get_all_players()

    def get_players(self):
        return self.players
