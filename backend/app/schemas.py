from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ItemBase(BaseModel):
    """Base schema for Item"""
    item_name: str = Field(..., min_length=1, max_length=255)
    shelf_number: str = Field(..., min_length=1, max_length=50)
    category: Optional[str] = Field(None, max_length=100)
    quantity: Optional[int] = Field(None, ge=0)

class ItemCreate(ItemBase):
    """Schema for creating an item"""
    item_id: str = Field(..., min_length=1, max_length=100)

class ItemUpdate(ItemBase):
    """Schema for updating an item"""
    pass

class ItemResponse(ItemBase):
    """Schema for item response"""
    item_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class ItemShelfResponse(BaseModel):
    """Schema for item shelf lookup response"""
    item_id: str
    item_name: str
    shelf_number: str

class ShelfItemsResponse(BaseModel):
    """Schema for shelf items response"""
    shelf_number: str
    items: List[ItemResponse]
    total_items: int

class MessageResponse(BaseModel):
    """Schema for generic message response"""
    message: str