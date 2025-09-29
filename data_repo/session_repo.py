from common.db_connection import connect_db


class SessionRepo:

    @classmethod
    def get_all_sessions(cls) -> list[dict]:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM practice_session")
        rows = cursor.fetchall()
        conn.close()
        sections = [{"id": row[0], "name": row[1]} for row in rows]
        return sections

    @classmethod
    def get_all_templates(cls) -> list[dict]:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            """
        SELECT 
        template.id,
        template.name,
        billing_type_id,
        rental_cost,
        shuttle_amount,
        shuttle_price,
        GROUP_CONCAT(player.name, ',') as player_name FROM template
        join template_player on template.id = template_player.template_id
        join player on template_player.player_id = player.id
        GROUP BY template.id,
        template.name,
        billing_type_id,
        rental_cost,
        shuttle_amount,
        shuttle_price
        """
        )
        rows = cursor.fetchall()
        conn.close()
        players = [
            {
                "id": row[0],
                "name": row[1],
                "billingType": row[2],
                "rentalCost": row[3],
                "shuttleAmount": row[4],
                "shuttlePrice": row[5],
                "players": [i for i in row[6].split(",") if i],
            }
            for row in rows
        ]
        return players

    @classmethod
    def add_session(cls, session_data: dict) -> int:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO practice_session (name, session_date, shift_time) VALUES (?, ?, ?)
            """,
            (
                session_data["name"],
                session_data["sessionDate"],
                session_data["shiftTime"],
            ),
        )
        session_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return session_id

    @classmethod
    def get_billing_types(cls) -> list[dict]:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM billing_type")
        rows = cursor.fetchall()
        conn.close()
        billing_types = [{"id": row[0], "name": row[1]} for row in rows]
        return billing_types
