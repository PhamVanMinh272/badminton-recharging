# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fast_api.sessions import session_router
from fast_api.players import players_router

app = FastAPI()

app.include_router(session_router)

app.include_router(players_router)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# You can also include routers within other routers
# from routers import users
# app.include_router(users.router)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
