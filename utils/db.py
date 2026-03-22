import sqlite3 as sql
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "notas.db"


class Database:
    def __init__(self):
        with sql.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                content TEXT,
                font TEXT NOT NULL,
                size INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """
            )

    def notes(self):
        with sql.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM notes")
            notes = cur.fetchall()
            return notes

    def save_note(self, note):
        with sql.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO notes (name, content, font, size, created_at) VALUES (?, ?, ?, ?, ?)",
                (note["nome"], note["texto"], note["fonte"], note["tamanho"], note["data"]),
            )
            conn.commit()


db = Database()
