from typing import Annotated

from pydantic import BaseModel, computed_field, AfterValidator


def is_unique_items_list(value):
    # check duplicate case insensitive
    lowercased_players = [player.lower().strip() for player in value]
    if len(lowercased_players) != len(set(lowercased_players)):
        raise ValueError("Players list contains duplicate names (case insensitive).")
    return value


class SessionCost(BaseModel):
    rentalCost: int
    shuttleAmount: int
    shuttlePrice: int

    @computed_field
    @property
    def total_cost(self) -> int:
        return self.rentalCost + self.shuttleAmount * self.shuttlePrice


class SessionCostWeighted(SessionCost):
    players: Annotated[list[str], AfterValidator(is_unique_items_list)]


class SessionCostEqually(SessionCost):
    numberOfPlayers: int

