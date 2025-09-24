from pydantic import BaseModel

class SessionCreate(BaseModel):
    players: list[str]
    rentalCost: int
    shuttleAmount: int
    shuttlePrice: int
