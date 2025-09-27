from data_repo.player_repo import PlayerRepo


class PlayerService:
    def __init__(self):
        self.players = PlayerRepo.get_all_players()

    def get_players(self):
        return self.players
