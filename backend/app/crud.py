from typing import List, Optional
from app.database import get_db
from app.models import Item
from fastapi import HTTPException

class ItemCRUD:
    """CRUD operations for items"""
    
    @staticmethod
    def get_item_by_id(item_id: str) -> Optional[Item]:
        """Get item by ID"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM items WHERE item_id = ?
            """, (item_id,))
            row = cursor.fetchone()
            return Item.from_row(row) if row else None
    
    @staticmethod
    def get_item_by_name(item_name: str) -> Optional[Item]:
        """Get item by name (case-insensitive)"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM items 
                WHERE item_name = ? COLLATE NOCASE
            """, (item_name,))
            row = cursor.fetchone()
            return Item.from_row(row) if row else None
    
    @staticmethod
    def get_items_by_shelf(shelf_number: str) -> List[Item]:
        """Get all items in a specific shelf"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM items 
                WHERE shelf_number = ?
                ORDER BY item_name
            """, (shelf_number,))
            rows = cursor.fetchall()
            return [Item.from_row(row) for row in rows]
    
    @staticmethod
    def get_all_items() -> List[Item]:
        """Get all items"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM items
                ORDER BY shelf_number, item_name
            """)
            rows = cursor.fetchall()
            return [Item.from_row(row) for row in rows]
    
    @staticmethod
    def create_item(item_id: str, item_name: str, shelf_number: str, 
                   category: Optional[str] = None, quantity: Optional[int] = None) -> Item:
        """Create a new item"""
        with get_db() as conn:
            cursor = conn.cursor()
            
            # Check if item exists
            cursor.execute("SELECT item_id FROM items WHERE item_id = ?", (item_id,))
            if cursor.fetchone():
                raise HTTPException(
                    status_code=400,
                    detail=f"Item with ID '{item_id}' already exists"
                )
            
            cursor.execute("""
                INSERT INTO items (item_id, item_name, shelf_number, category, quantity)
                VALUES (?, ?, ?, ?, ?)
            """, (item_id, item_name, shelf_number, category, quantity))
            
            return ItemCRUD.get_item_by_id(item_id)
    
    @staticmethod
    def update_item(item_id: str, item_name: str, shelf_number: str,
                   category: Optional[str] = None, quantity: Optional[int] = None) -> Item:
        """Update an existing item"""
        with get_db() as conn:
            cursor = conn.cursor()
            
            # Check if item exists
            if not ItemCRUD.get_item_by_id(item_id):
                raise HTTPException(
                    status_code=404,
                    detail=f"Item with ID '{item_id}' not found"
                )
            
            cursor.execute("""
                UPDATE items 
                SET item_name = ?, shelf_number = ?, category = ?, quantity = ?
                WHERE item_id = ?
            """, (item_name, shelf_number, category, quantity, item_id))
            
            return ItemCRUD.get_item_by_id(item_id)
    
    @staticmethod
    def delete_item(item_id: str) -> bool:
        """Delete an item"""
        with get_db() as conn:
            cursor = conn.cursor()
            
            # Check if item exists
            if not ItemCRUD.get_item_by_id(item_id):
                raise HTTPException(
                    status_code=404,
                    detail=f"Item with ID '{item_id}' not found"
                )
            
            cursor.execute("DELETE FROM items WHERE item_id = ?", (item_id,))
            return True