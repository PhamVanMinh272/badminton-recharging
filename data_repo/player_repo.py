from common.db_connection import connect_db


class PlayerRepo:
    @classmethod
    def get_all_players(cls):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, weight FROM player")
        rows = cursor.fetchall()
        conn.close()
        players = [{"id": row[0], "name": row[1], "weight": row[2]} for row in rows]
        return players
