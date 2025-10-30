import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from app.database import init_database

if __name__ == "__main__":
    init_database()
    print("✅ Database initialization complete!")