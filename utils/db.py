import sqlite3 as sql
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "notas.db"


class Database:
    def __init__(self):
        with sql.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                content TEXT,
                font TEXT NOT NULL,
                size INTEGER NOT NULL,
                created_at TEXT NOT NULL
            )
            """)

    def list_notes(self):
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
                (
                    note["nome"],
                    note["texto"],
                    note["fonte"],
                    note["tamanho"],
                    note["data"],
                ),
            )
            conn.commit()

    def edit_note(self, note, id):
        with sql.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE notes SET name = ?, content = ?, font = ?, size = ? WHERE id = ?",
                (
                    note["nome"],
                    note["texto"],
                    note["fonte"],
                    note["tamanho"],
                    id,
                ),
            )
            conn.commit()

    def delete_note(self, id):
        with sql.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM notes WHERE id = ?", (id,))
            conn.commit()
    
    # def search_by_name(self, name):
    #     with sql.connect(DB_PATH) as conn:
    #         cur = conn.cursor()
    #         cur.execute("SELECT FROM notes WHERE name = ?", (name,))
    #         note = cur.fetchone()
    #         return note

db = Database()
