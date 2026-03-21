import sqlite3 as sql


class Database:
    def __init__(self):
        with sql.connect("notas.db") as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                name TEXT NOT NULL,
                content TEXT,
                font TEXT,
                size INTEGER
            )
            """
            )

    def save_note(self, note):
        with sql.connect("notas.db") as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO notes (name, content, font, size) VALUES (?, ?, ?, ?)",
                (note["nome"], note["texto"], note["fonte"], note['tamanho']),
            )
            conn.commit()


db = Database()
