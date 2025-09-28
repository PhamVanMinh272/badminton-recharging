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

    @computed_field
    @property
    def weighted_data(self) -> list[float]:
        """
        self.players = [
        "Minh", "An-0.8", "John"
        ]
        return [1, 0.8, 1]
        Remove weighted from name
        :return:
        """
        weighted_list = []
        new_names = []
        for player in self.players:
            if "-" in player:
                name, weight_str = player.split("-")
                new_names.append(name.strip())
                try:
                    weight = float(weight_str)
                except ValueError:
                    weight = 1.0
                weighted_list.append(weight)
            else:
                weighted_list.append(1.0)
                new_names.append(player.strip())
        # TODO: update players name more cleanly
        self.players = new_names
        return weighted_list

    def check_players_unique(self):
        is_unique_items_list(self.players)

    def clean_players(self):
        """Remove weight from names"""
        new_names = []
        for player in self.players:
            name = player
            if "-" in player:
                name, weight_str = player.split("-")
            new_names.append(name.strip())
        self.players = new_names


class SessionCostEqually(SessionCost):
    numberOfPlayers: int
