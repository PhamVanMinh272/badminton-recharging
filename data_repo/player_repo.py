class PlayerRepo:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = conn.cursor()

    def get_all_players(self):
        self._cursor.execute("SELECT id, name, weight FROM player")
        rows = self._cursor.fetchall()
        players = [{"id": row[0], "name": row[1], "weight": row[2]} for row in rows]
        return players
