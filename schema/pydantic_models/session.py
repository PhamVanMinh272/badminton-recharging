from pydantic import BaseModel, computed_field

class SessionCost(BaseModel):
    rentalCost: int
    shuttleAmount: int
    shuttlePrice: int

    @computed_field
    @property
    def total_cost(self) -> int:
        return self.rentalCost + self.shuttleAmount * self.shuttlePrice


class SessionCreate(SessionCost):
    players: list[str]


class SessionCostEqually(SessionCost):
    numberOfPlayers: int

