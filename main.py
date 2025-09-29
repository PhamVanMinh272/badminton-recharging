from flask import Flask
from flask_cors import CORS

from flask_api.sessions import session_router
from flask_api.players import players_router
from swagger.flask_main import swagger_bp


app = Flask(__name__)
CORS(app)

app.register_blueprint(swagger_bp, url_prefix="/api/swagger")
app.register_blueprint(session_router, url_prefix="/api/sessions")
app.register_blueprint(players_router, url_prefix="/api/players")


# app exit handler
@app.teardown_appcontext
def shutdown_session(exception=None):
    # should close db session here
    pass


if __name__ == "__main__":
    app.run(debug=True)
