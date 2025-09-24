# routers/items.py
import datetime

from fastapi import APIRouter
from services.sessions import Session
from schema.pydantic_models.session import SessionCreate

session_router = APIRouter(prefix="/sessions", tags=["Session"])

#
@session_router.get("/")
async def get_session():
    return {"message": "Reading items"}


@session_router.post("/calc-cost")
async def calc_cost(session_data: SessionCreate):

    session = Session(session_data.players)
    cost = session.cost_amount(
        rental_cost=session_data.rentalCost,
        shuttle_amount=session_data.shuttleAmount,
        shuttle_price=session_data.shuttlePrice
    )

    return {"data": {
        "cost": session.cost_per_person(cost),
        "sessionDate": datetime.date.today().strftime("%Y-%m-%d")
    }}