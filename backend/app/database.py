import sqlite3
from contextlib import contextmanager
from typing import Generator

DATABASE = "store_inventory.db"

@contextmanager
def get_db() -> Generator[sqlite3.Connection, None, None]:
    """Database connection context manager"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_database():
    """Initialize database with tables and indexes"""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Create items table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                item_id TEXT PRIMARY KEY,
                item_name TEXT NOT NULL,
                shelf_number TEXT NOT NULL,
                category TEXT,
                quantity INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create indexes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_item_name 
            ON items(item_name)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_shelf_number 
            ON items(shelf_number)
        """)
        
        # Create trigger to update updated_at timestamp
        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS update_items_timestamp 
            AFTER UPDATE ON items
            BEGIN
                UPDATE items SET updated_at = CURRENT_TIMESTAMP 
                WHERE item_id = NEW.item_id;
            END
        """)
        
        print("✅ Database initialized successfully!")