# Store Inventory API

FastAPI backend for managing store inventory and shelf locations.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize database:
```bash
python scripts/init_db.py
```

3. (Optional) Seed with sample data:
```bash
python scripts/seed_data.py
```

4. Run the server:
```bash
python -m app.main
# or
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /items/` - Get all items
- `GET /items/shelf?item_name=Milk` - Get shelf for item
- `POST /items/` - Create new item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item
- `GET /shelves/{shelf_number}/items` - Get all items in shelf

## Documentation

Interactive API docs available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc