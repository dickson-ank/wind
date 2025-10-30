from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_database
from app.routers import items, shelves

app = FastAPI(
    title="Store Inventory API",
    description="API for managing store inventory and shelf locations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(items.router)
app.include_router(shelves.router)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_database()

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "Store Inventory API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)