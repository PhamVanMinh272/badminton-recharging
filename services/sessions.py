import math
from common.enum import BillingTypes
from schema.pydantic_models.session import SessionCost

players = {
    "C Ân": {"level": 8, "weight": 0.8},
    "Giao": {"level": 6, "weight": 0.8},
}

class Session:
    def __init__(self, billing_type: int, session_cost_model: SessionCost):
        """
        :param active_player_names:
        """
        self._session_cost_model = session_cost_model

        # self.players = players
        self._active_players = [{"name": name} for name in self._session_cost_model.players]
        # retreive weight from players list
        for player in self._active_players:
            if player.get("name") in players:
                player.update(players[player.get("name")])
        self.billing_type = billing_type
        self.date = None

        self._strategies = {
            BillingTypes.WEIGHTED: self._calc_cost_weighted,
            BillingTypes.EQUALLY: self._calc_cost_equally,
        }

    def calc_cost_amount(self) -> dict:
        return self._strategies[self.billing_type]()

    def _calc_cost_equally(self) -> dict:
        if not self._session_cost_model.numberOfPlayers:
            raise ValueError("number_of_players is required for EQUALLY billing type")
        base_cost_per_person = math.ceil(self._session_cost_model.total_cost / self._session_cost_model.numberOfPlayers)
        return {"Per Person": base_cost_per_person}

    def _calc_cost_weighted(self) -> dict:
        base_cost_per_person = math.ceil(self._session_cost_model.total_cost / len(self._active_players))

        # base cost per person by weight
        discount_person = [player for player in self._active_players if player.get("weight", 1) < 1]
        billed_players = {}
        temp_total_cost = self._session_cost_model.total_cost
        for player in discount_person:
            billed_players[player.get("name")] = math.ceil(base_cost_per_person * player.get("weight", 1))
            temp_total_cost -= billed_players[player.get("name")]

        for player in self._active_players:
            if player.get("name") not in billed_players:
                billed_players[player.get("name")] = math.ceil(temp_total_cost / (len(self._active_players) - len(discount_person)))

        return billed_players
