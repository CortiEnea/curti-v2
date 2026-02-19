from __future__ import annotations

import json
import os
import sqlite3
from contextlib import contextmanager

IS_VERCEL = bool(os.getenv("VERCEL"))
DB_PATH = "/tmp/database.db" if IS_VERCEL else os.path.join(os.path.dirname(__file__), "database.db")


def _row_factory(cursor: sqlite3.Cursor, row: tuple) -> dict:
    return {col[0]: row[i] for i, col in enumerate(cursor.description)}


@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = _row_factory
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS projects (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       TEXT    NOT NULL,
                location    TEXT    NOT NULL,
                goal        TEXT    NOT NULL,
                solution    TEXT    NOT NULL,
                materials   TEXT    NOT NULL,
                image       TEXT    DEFAULT '',
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS real_estate (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                listing_type  TEXT    NOT NULL CHECK(listing_type IN ('vendita', 'affitto')),
                place         TEXT    NOT NULL,
                title         TEXT    NOT NULL,
                rooms         TEXT    NOT NULL,
                floor         TEXT    NOT NULL,
                price_chf     INTEGER NOT NULL,
                price_label   TEXT    DEFAULT '',
                description   TEXT    NOT NULL,
                bullets       TEXT    DEFAULT '[]',
                images        TEXT    DEFAULT '[]',
                created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)


# ── Projects ──────────────────────────────────────────────────────────────────

def get_projects() -> list[dict]:
    with get_db() as conn:
        return conn.execute("SELECT * FROM projects ORDER BY created_at DESC").fetchall()


def get_project(project_id: int) -> dict | None:
    with get_db() as conn:
        return conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()


def create_project(title: str, location: str, goal: str, solution: str, materials: str, image: str = "") -> int:
    with get_db() as conn:
        cur = conn.execute(
            "INSERT INTO projects (title, location, goal, solution, materials, image) VALUES (?, ?, ?, ?, ?, ?)",
            (title, location, goal, solution, materials, image),
        )
        return cur.lastrowid


def update_project(project_id: int, title: str, location: str, goal: str, solution: str, materials: str, image: str = "") -> None:
    with get_db() as conn:
        conn.execute(
            "UPDATE projects SET title=?, location=?, goal=?, solution=?, materials=?, image=? WHERE id=?",
            (title, location, goal, solution, materials, image, project_id),
        )


def delete_project(project_id: int) -> None:
    with get_db() as conn:
        conn.execute("DELETE FROM projects WHERE id = ?", (project_id,))


# ── Real Estate ───────────────────────────────────────────────────────────────

def get_listings() -> list[dict]:
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM real_estate ORDER BY listing_type, created_at DESC").fetchall()
    for row in rows:
        row["bullets"] = json.loads(row.get("bullets") or "[]")
        row["images"] = json.loads(row.get("images") or "[]")
    return rows


def get_listing(listing_id: int) -> dict | None:
    with get_db() as conn:
        row = conn.execute("SELECT * FROM real_estate WHERE id = ?", (listing_id,)).fetchone()
    if row:
        row["bullets"] = json.loads(row.get("bullets") or "[]")
        row["images"] = json.loads(row.get("images") or "[]")
    return row


def create_listing(
    listing_type: str, place: str, title: str, rooms: str, floor: str,
    price_chf: int, price_label: str, description: str,
    bullets: list[str], images: list[str],
) -> int:
    with get_db() as conn:
        cur = conn.execute(
            """INSERT INTO real_estate
               (listing_type, place, title, rooms, floor, price_chf, price_label, description, bullets, images)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (listing_type, place, title, rooms, floor, price_chf, price_label, description,
             json.dumps(bullets, ensure_ascii=False), json.dumps(images, ensure_ascii=False)),
        )
        return cur.lastrowid


def update_listing(
    listing_id: int, listing_type: str, place: str, title: str, rooms: str,
    floor: str, price_chf: int, price_label: str, description: str,
    bullets: list[str], images: list[str],
) -> None:
    with get_db() as conn:
        conn.execute(
            """UPDATE real_estate
               SET listing_type=?, place=?, title=?, rooms=?, floor=?, price_chf=?,
                   price_label=?, description=?, bullets=?, images=?
               WHERE id=?""",
            (listing_type, place, title, rooms, floor, price_chf, price_label, description,
             json.dumps(bullets, ensure_ascii=False), json.dumps(images, ensure_ascii=False), listing_id),
        )


def delete_listing(listing_id: int) -> None:
    with get_db() as conn:
        conn.execute("DELETE FROM real_estate WHERE id = ?", (listing_id,))


# ── Seed ──────────────────────────────────────────────────────────────────────

def seed_defaults():
    """Populate the database with default data from site_data.py if tables are empty."""
    from site_data import PROJECTS, REAL_ESTATE, IMAGES
    import json as _json

    with get_db() as conn:
        count = conn.execute("SELECT COUNT(*) as c FROM projects").fetchone()["c"]
        if count == 0:
            image_keys = ["cucina", "portoncino", "armadio"]
            for i, p in enumerate(PROJECTS):
                img = IMAGES["projects"].get(image_keys[i], "") if i < len(image_keys) else ""
                conn.execute(
                    "INSERT INTO projects (title, location, goal, solution, materials, image) VALUES (?, ?, ?, ?, ?, ?)",
                    (p.title, p.location, p.goal, p.solution, p.materials, img),
                )

        count = conn.execute("SELECT COUNT(*) as c FROM real_estate").fetchone()["c"]
        if count == 0:
            for listing in REAL_ESTATE:
                conn.execute(
                    """INSERT INTO real_estate
                       (listing_type, place, title, rooms, floor, price_chf, price_label, description, bullets, images)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (listing.listing_type, listing.place, listing.title, listing.rooms,
                     listing.floor, listing.price_chf, listing.price_label, listing.description,
                     _json.dumps(listing.bullets, ensure_ascii=False),
                     _json.dumps(listing.images, ensure_ascii=False)),
                )
