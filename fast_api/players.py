# routers/items.py
from fastapi import APIRouter

from services.players import Players

players_router = APIRouter(prefix="/players", tags=["items"])


@players_router.get("/")
async def read_items():
    return {"data": Players().get_players()}


@players_router.post("/")
async def create_item():
    return {"message": "Creating an item"}

