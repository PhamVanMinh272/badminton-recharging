import math
from datetime import datetime, timedelta

from common.enum import BillingTypes
from schema.pydantic_models.session import SessionCost
from data_repo.session_repo import SessionRepo

players = {
    "C Ân": {"weight": 0.8},
    "Giao": {"weight": 0.8},
}


class PracticeSessionService:
    def __init__(self, billing_type: int, session_cost_model: SessionCost):
        """
        :param active_player_names:
        """
        self._session_cost_model = session_cost_model

        # self.players = players
        if billing_type == BillingTypes.WEIGHTED.value:
            weighted = self._session_cost_model.weighted_data
            self._session_cost_model.clean_players()
            self._session_cost_model.check_players_unique()

            self._active_players = [
                {"name": name, "weight": weight} if weight != 1 else {"name": name}
                for name, weight in zip(self._session_cost_model.players, weighted)
            ]
            # retreive weight from players list
            for player in self._active_players:
                if player.get("name") in players and "weight" not in player.keys():
                    player.update(players[player.get("name")])
        self.billing_type = billing_type
        self.date = None

        self._strategies = {
            BillingTypes.WEIGHTED.value: self._calc_cost_weighted,
            BillingTypes.EQUALLY.value: self._calc_cost_equally,
        }

    def calc_cost_amount(self) -> dict:
        self._re_calc_shuttle_price()
        return self._strategies[self.billing_type]()

    @classmethod
    def get_session_templates(cls):
        # return SESSION_TEMPLATE_DATA
        return SessionRepo().get_all_templates()

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

    @classmethod
    def get_billing_types(cls) -> list[dict]:
        return SessionRepo.get_billing_types()

    @classmethod
    def get_all_sessions(cls):
        return SessionRepo().get_all_sessions()

    @staticmethod
    def get_recently_sessions_date():
        latest_wednesday = PracticeSessionService.get_latest_weekday(2)
        latest_friday = PracticeSessionService.get_latest_weekday(4)
        latest_sunday = PracticeSessionService.get_latest_weekday(6)
        return [
            {
                "name": "",
                "day": "",
                "date": latest_wednesday.strftime("%Y-%m-%d")
            },
            {
                "name": "",
                "day": "",
                "date": latest_sunday.strftime("%Y-%m-%d")
            },
            {
                "name": "",
                "day": "",
                "date": latest_friday.strftime("%Y-%m-%d")
            }
        ]

    @staticmethod
    def get_latest_weekday(target_weekday):
        today = datetime.today()
        days_ago = (today.weekday() - target_weekday) % 7
        return today - timedelta(days=days_ago)


