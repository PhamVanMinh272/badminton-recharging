import math
from common.enum import BillingTypes
from schema.pydantic_models.session import SessionCost

players = {
    "C Ân": {"level": 8, "weight": 0.8},
    "Giao": {"level": 6, "weight": 0.8},
}

SESSION_TEMPLATE_DATA = [
    {
        "id": 1,
        "name": "Wednesday Regular",
        "billingType": BillingTypes.EQUALLY,
        "rentalCost": 220,
        "shuttleAmount": 4,
        "shuttlePrice": 305,
        "players": ["Minh", "Đạt", "Thảo", "Tú", "Thinh", "Văn", "Tuyến"],
    },
    {
        "id": 2,
        "name": "Sunday Regular",
        "billingType": BillingTypes.EQUALLY,
        "rentalCost": 200,
        "shuttleAmount": 4,
        "shuttlePrice": 305,
        "players": ["Minh", "Đạt", "Thảo", "Tú", "Thinh", "Văn", "Tuyến"],
    },
    {
        "id": 3,
        "name": "Friday",
        "billingType": BillingTypes.WEIGHTED,
        "rentalCost": 280,
        "shuttleAmount": 6,
        "shuttlePrice": 305,
        "players": [
            "Minh",
            "Đạt",
            "Thiên",
            "Tấn",
            "Thoại",
            "Tâm",
            "Toàn",
            "Giao",
            "C Ân",
        ],
    },
]


class PracticeSessionService:
    def __init__(self, billing_type: int, session_cost_model: SessionCost):
        """
        :param active_player_names:
        """
        self._session_cost_model = session_cost_model

        # self.players = players
        if billing_type is BillingTypes.WEIGHTED:
            weighted = self._session_cost_model.weighted_data
            self._session_cost_model.clean_players()
            self._session_cost_model.check_players_unique()

            self._active_players = [
                {"name": name, "weight": weight} if weight != 1 else {"name": name} for name, weight in zip(self._session_cost_model.players, weighted)
            ]
            # retreive weight from players list
            for player in self._active_players:
                if player.get("name") in players and "weight" not in player.keys():
                    player.update(players[player.get("name")])
        self.billing_type = billing_type
        self.date = None

        self._strategies = {
            BillingTypes.WEIGHTED: self._calc_cost_weighted,
            BillingTypes.EQUALLY: self._calc_cost_equally,
        }

    def calc_cost_amount(self) -> dict:
        self._re_calc_shuttle_price()
        return self._strategies[self.billing_type]()

    @classmethod
    def get_session_templates(cls):
        return SESSION_TEMPLATE_DATA

    def _re_calc_shuttle_price(self):
        """
        Price can be 1 shuttle or 12 shuttles.
        It is 12 shuttles if price > 100
        :return:
        """
        if self._session_cost_model.shuttlePrice > 100:
            self._session_cost_model.shuttlePrice = math.ceil(
                self._session_cost_model.shuttlePrice / 12
            )
        else:
            self._session_cost_model.shuttlePrice = (
                self._session_cost_model.shuttlePrice
            )

    def _calc_cost_equally(self) -> dict:
        if not self._session_cost_model.numberOfPlayers:
            raise ValueError("number_of_players is required for EQUALLY billing type")
        base_cost_per_person = math.ceil(
            self._session_cost_model.total_cost
            / self._session_cost_model.numberOfPlayers
        )
        return {"Per Person": base_cost_per_person}

    def _calc_cost_weighted(self) -> dict:
        print(self._active_players)
        base_cost_per_person = math.ceil(
            self._session_cost_model.total_cost / len(self._active_players)
        )

        # base cost per person by weight
        discount_person = [
            player for player in self._active_players if player.get("weight", 1) < 1
        ]
        billed_players = {}
        temp_total_cost = self._session_cost_model.total_cost
        for player in discount_person:
            billed_players[player.get("name")] = math.ceil(
                base_cost_per_person * player.get("weight", 1)
            )
            temp_total_cost -= billed_players[player.get("name")]

        for player in self._active_players:
            if player.get("name") not in billed_players:
                billed_players[player.get("name")] = math.ceil(
                    temp_total_cost / (len(self._active_players) - len(discount_person))
                )

        return billed_players
