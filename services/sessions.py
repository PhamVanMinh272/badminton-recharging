import math

players = {
    "C Ân": {"level": 8, "weight": 0.8},
    "Giao": {"level": 6, "weight": 0.8},
}

class Session:
    def __init__(self, active_player_names: list):
        # self.players = players
        self.active_players = [{"name": name} for name in active_player_names]
        # retreive weight from players list
        for player in self.active_players:
            if player.get("name") in players:
                player.update(players[player.get("name")])
        self.billed_players = {}
        self.date = None
        self.rental_cost = 0

    def cost_per_person(self, total_cost: int) -> dict:
        base_cost_per_person = math.ceil(total_cost / len(self.active_players))

        # base cost per person by weight
        discount_person = [player for player in self.active_players if player.get("weight", 1) < 1]
        for player in discount_person:
            self.billed_players[player.get("name")] = math.ceil(base_cost_per_person * player.get("weight", 1))
            total_cost -= self.billed_players[player.get("name")]

        for player in self.active_players:
            if player.get("name") not in self.billed_players:
                self.billed_players[player.get("name")] = math.ceil(total_cost / (len(self.active_players) - len(discount_person)))

        return self.billed_players

    def cost_amount(self, rental_cost: int, shuttle_amount: int, shuttle_price: int) -> int:
        shuttle_cost = shuttle_amount * shuttle_price
        total_cost = rental_cost + shuttle_cost
        return total_cost
