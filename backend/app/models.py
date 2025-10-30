from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Item:
    """Database model for Item"""
    item_id: str
    item_name: str
    shelf_number: str
    category: Optional[str] = None
    quantity: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    @classmethod
    def from_row(cls, row) -> "Item":
        """Create Item from database row"""
        row = dict(row)
        return cls(
            item_id=row["item_id"],
            item_name=row["item_name"],
            shelf_number=row["shelf_number"],
            category=row["category"],
            quantity=row["quantity"],
            created_at=row.get("created_at"),
            updated_at=row.get("updated_at")
        )