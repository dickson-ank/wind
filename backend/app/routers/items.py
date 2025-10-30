from fastapi import APIRouter, Query
from typing import List
from app.schemas import (
    ItemCreate, ItemUpdate, ItemResponse, 
    ItemShelfResponse, MessageResponse
)
from app.crud import ItemCRUD

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=List[ItemResponse])
async def get_all_items():
    """Get all items in inventory"""
    items = ItemCRUD.get_all_items()
    return [
        ItemResponse(
            item_id=item.item_id,
            item_name=item.item_name,
            shelf_number=item.shelf_number,
            category=item.category,
            quantity=item.quantity,
            created_at=item.created_at,
            updated_at=item.updated_at
        )
        for item in items
    ]

@router.get("/shelf", response_model=ItemShelfResponse)
async def get_item_shelf(
    item_name: str = Query(..., description="Name of the item to search for")
):
    """Get the shelf number for a specific item"""
    item = ItemCRUD.get_item_by_name(item_name)
    
    if not item:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=404,
            detail=f"Item '{item_name}' not found"
        )
    
    return ItemShelfResponse(
        item_id=item.item_id,
        item_name=item.item_name,
        shelf_number=item.shelf_number
    )

@router.post("/", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate):
    """Add a new item to inventory"""
    created_item = ItemCRUD.create_item(
        item_id=item.item_id,
        item_name=item.item_name,
        shelf_number=item.shelf_number,
        category=item.category,
        quantity=item.quantity
    )
    
    return ItemResponse(
        item_id=created_item.item_id,
        item_name=created_item.item_name,
        shelf_number=created_item.shelf_number,
        category=created_item.category,
        quantity=created_item.quantity,
        created_at=created_item.created_at,
        updated_at=created_item.updated_at
    )

@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item: ItemUpdate):
    """Update an existing item"""
    updated_item = ItemCRUD.update_item(
        item_id=item_id,
        item_name=item.item_name,
        shelf_number=item.shelf_number,
        category=item.category,
        quantity=item.quantity
    )
    
    return ItemResponse(
        item_id=updated_item.item_id,
        item_name=updated_item.item_name,
        shelf_number=updated_item.shelf_number,
        category=updated_item.category,
        quantity=updated_item.quantity,
        created_at=updated_item.created_at,
        updated_at=updated_item.updated_at
    )

@router.delete("/{item_id}", response_model=MessageResponse)
async def delete_item(item_id: str):
    """Delete an item from inventory"""
    ItemCRUD.delete_item(item_id)
    return MessageResponse(message=f"Item {item_id} deleted successfully")