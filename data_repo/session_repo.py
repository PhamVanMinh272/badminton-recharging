class SessionRepo:

    def __init__(self, conn):
        self._conn = conn
        self._cursor = conn.cursor()

    def get_all_sessions(self) -> list[dict]:
        self._cursor.execute(
            """
            SELECT practice_session.id, name, session_date, shift_time, location, bill.id as bill_id, rental_cost, shuttle_amount, shuttle_price
            FROM practice_session left join bill on practice_session.id = bill.practice_session_id 
            ORDER BY session_date DESC"""
        )
        rows = self._cursor.fetchall()
        sections = [
            {
                "id": row[0],
                "name": row[1],
                "sessionDate": row[2],
                "shiftTime": row[3],
                "location": [row[4]],
                "billId": row[5],
                "rentalCost": row[6] if row[6] else 0,
                "shuttleAmount": row[7] if row[7] else 0,
                "shuttlePrice": row[8] if row[8] else 0,
            }
            for row in rows
        ]
        return sections

    def get_all_templates(self) -> list[dict]:
        self._cursor.execute(
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
        rows = self._cursor.fetchall()
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

    def add_session(self, session_data: dict) -> int:
        self._cursor.execute(
            """
            INSERT INTO practice_session (name, session_date, shift_time, location) VALUES (?, ?, ?, ?)
            """,
            (
                session_data["name"],
                session_data["sessionDate"],
                session_data["shiftTime"],
                session_data["location"],
            ),
        )
        session_id = self._cursor.lastrowid
        # commit
        self._cursor.connection.commit()
        return session_id

    def get_billing_types(self) -> list[dict]:
        self._cursor.execute("SELECT id, name FROM billing_type")
        rows = self._cursor.fetchall()
        billing_types = [{"id": row[0], "name": row[1]} for row in rows]
        return billing_types
