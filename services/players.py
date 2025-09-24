class Players:
    def __init__(self):
        self.players = [
            "C Ân", "Giao", "Tấn", "Thảo", "Tú", "Thinh", "Văn", "Tuyến"
        ]

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players