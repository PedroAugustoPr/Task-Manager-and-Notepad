import sqlite3 as sql


class Database:
    def __init__(self):
        with sql.connect("notas.db") as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                text TEXT
            )
            """
        )


db = Database()
