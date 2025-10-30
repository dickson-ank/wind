from fastapi import APIRouter
from app.schemas import ShelfItemsResponse, ItemResponse
from app.crud import ItemCRUD

router = APIRouter(prefix="/shelves", tags=["Shelves"])

@router.get("/{shelf_number}/items", response_model=ShelfItemsResponse)
async def get_shelf_items(shelf_number: str):
    """Get all items in a specific shelf"""
    items = ItemCRUD.get_items_by_shelf(shelf_number)
    
    item_responses = [
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
    
    return ShelfItemsResponse(
        shelf_number=shelf_number,
        items=item_responses,
        total_items=len(item_responses)
    )