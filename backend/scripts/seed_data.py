import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from app.crud import ItemCRUD

def seed_database():
    """Seed database with sample data"""
    sample_items = [
        # Dairy - Shelf A1
        ("ITEM001", "Whole Milk", "A1", "Dairy", 50),
        ("ITEM002", "Skim Milk", "A1", "Dairy", 45),
        ("ITEM003", "Almond Milk", "A1", "Dairy", 30),
        ("ITEM004", "Oat Milk", "A1", "Dairy", 25),
        ("ITEM005", "Cheddar Cheese", "A1", "Dairy", 40),
        ("ITEM006", "Mozzarella Cheese", "A1", "Dairy", 35),
        ("ITEM007", "Greek Yogurt", "A1", "Dairy", 60),
        ("ITEM008", "Butter", "A1", "Dairy", 55),
        ("ITEM009", "Cream Cheese", "A1", "Dairy", 45),
        ("ITEM010", "Sour Cream", "A1", "Dairy", 40),
        
        # Bakery - Shelf A2
        ("ITEM011", "White Bread", "A2", "Bakery", 30),
        ("ITEM012", "Wheat Bread", "A2", "Bakery", 35),
        ("ITEM013", "Sourdough Bread", "A2", "Bakery", 20),
        ("ITEM014", "Bagels", "A2", "Bakery", 50),
        ("ITEM015", "Croissants", "A2", "Bakery", 25),
        ("ITEM016", "Muffins", "A2", "Bakery", 40),
        ("ITEM017", "Donuts", "A2", "Bakery", 35),
        ("ITEM018", "Baguette", "A2", "Bakery", 28),
        ("ITEM019", "Dinner Rolls", "A2", "Bakery", 45),
        ("ITEM020", "English Muffins", "A2", "Bakery", 38),
        
        # Fruits - Shelf B1
        ("ITEM021", "Red Apples", "B1", "Fruits", 80),
        ("ITEM022", "Green Apples", "B1", "Fruits", 75),
        ("ITEM023", "Bananas", "B1", "Fruits", 100),
        ("ITEM024", "Oranges", "B1", "Fruits", 90),
        ("ITEM025", "Grapes", "B1", "Fruits", 65),
        ("ITEM026", "Strawberries", "B1", "Fruits", 55),
        ("ITEM027", "Blueberries", "B1", "Fruits", 45),
        ("ITEM028", "Watermelon", "B1", "Fruits", 30),
        ("ITEM029", "Pineapple", "B1", "Fruits", 35),
        ("ITEM030", "Mango", "B1", "Fruits", 40),
        
        # Vegetables - Shelf B2
        ("ITEM031", "Carrots", "B2", "Vegetables", 70),
        ("ITEM032", "Broccoli", "B2", "Vegetables", 50),
        ("ITEM033", "Spinach", "B2", "Vegetables", 45),
        ("ITEM034", "Lettuce", "B2", "Vegetables", 60),
        ("ITEM035", "Tomatoes", "B2", "Vegetables", 85),
        ("ITEM036", "Cucumbers", "B2", "Vegetables", 55),
        ("ITEM037", "Bell Peppers", "B2", "Vegetables", 48),
        ("ITEM038", "Onions", "B2", "Vegetables", 90),
        ("ITEM039", "Potatoes", "B2", "Vegetables", 100),
        ("ITEM040", "Garlic", "B2", "Vegetables", 65),
        
        # Breakfast - Shelf C1
        ("ITEM041", "Corn Flakes", "C1", "Breakfast", 40),
        ("ITEM042", "Oatmeal", "C1", "Breakfast", 45),
        ("ITEM043", "Granola", "C1", "Breakfast", 35),
        ("ITEM044", "Cheerios", "C1", "Breakfast", 50),
        ("ITEM045", "Frosted Flakes", "C1", "Breakfast", 42),
        ("ITEM046", "Pancake Mix", "C1", "Breakfast", 30),
        ("ITEM047", "Waffle Mix", "C1", "Breakfast", 28),
        ("ITEM048", "Maple Syrup", "C1", "Breakfast", 38),
        ("ITEM049", "Honey", "C1", "Breakfast", 40),
        ("ITEM050", "Jam", "C1", "Breakfast", 45),
        
        # Beverages - Shelf C2
        ("ITEM051", "Coffee Beans", "C2", "Beverages", 35),
        ("ITEM052", "Ground Coffee", "C2", "Beverages", 40),
        ("ITEM053", "Green Tea", "C2", "Beverages", 45),
        ("ITEM054", "Black Tea", "C2", "Beverages", 50),
        ("ITEM055", "Herbal Tea", "C2", "Beverages", 38),
        ("ITEM056", "Orange Juice", "C2", "Beverages", 60),
        ("ITEM057", "Apple Juice", "C2", "Beverages", 55),
        ("ITEM058", "Cranberry Juice", "C2", "Beverages", 42),
        ("ITEM059", "Soda Cola", "C2", "Beverages", 80),
        ("ITEM060", "Sparkling Water", "C2", "Beverages", 70),
        
        # Grains & Pasta - Shelf D1
        ("ITEM061", "White Rice", "D1", "Grains", 70),
        ("ITEM062", "Brown Rice", "D1", "Grains", 65),
        ("ITEM063", "Quinoa", "D1", "Grains", 40),
        ("ITEM064", "Spaghetti", "D1", "Grains", 55),
        ("ITEM065", "Penne Pasta", "D1", "Grains", 50),
        ("ITEM066", "Macaroni", "D1", "Grains", 48),
        ("ITEM067", "Lasagna Sheets", "D1", "Grains", 35),
        ("ITEM068", "Couscous", "D1", "Grains", 42),
        ("ITEM069", "Barley", "D1", "Grains", 38),
        ("ITEM070", "Bulgur", "D1", "Grains", 32),
        
        # Canned Goods - Shelf D2
        ("ITEM071", "Tomato Sauce", "D2", "Canned Goods", 60),
        ("ITEM072", "Canned Beans", "D2", "Canned Goods", 75),
        ("ITEM073", "Canned Corn", "D2", "Canned Goods", 65),
        ("ITEM074", "Canned Peas", "D2", "Canned Goods", 58),
        ("ITEM075", "Canned Tuna", "D2", "Canned Goods", 70),
        ("ITEM076", "Canned Salmon", "D2", "Canned Goods", 45),
        ("ITEM077", "Chicken Broth", "D2", "Canned Goods", 55),
        ("ITEM078", "Beef Broth", "D2", "Canned Goods", 52),
        ("ITEM079", "Coconut Milk", "D2", "Canned Goods", 48),
        ("ITEM080", "Tomato Paste", "D2", "Canned Goods", 62),
        
        # Snacks - Shelf E1
        ("ITEM081", "Potato Chips", "E1", "Snacks", 90),
        ("ITEM082", "Tortilla Chips", "E1", "Snacks", 85),
        ("ITEM083", "Pretzels", "E1", "Snacks", 70),
        ("ITEM084", "Popcorn", "E1", "Snacks", 75),
        ("ITEM085", "Crackers", "E1", "Snacks", 68),
        ("ITEM086", "Granola Bars", "E1", "Snacks", 80),
        ("ITEM087", "Protein Bars", "E1", "Snacks", 65),
        ("ITEM088", "Trail Mix", "E1", "Snacks", 55),
        ("ITEM089", "Cookies", "E1", "Snacks", 72),
        ("ITEM090", "Chocolate Bars", "E1", "Snacks", 95),
        
        # Condiments - Shelf E2
        ("ITEM091", "Ketchup", "E2", "Condiments", 60),
        ("ITEM092", "Mustard", "E2", "Condiments", 55),
        ("ITEM093", "Mayonnaise", "E2", "Condiments", 50),
        ("ITEM094", "BBQ Sauce", "E2", "Condiments", 45),
        ("ITEM095", "Soy Sauce", "E2", "Condiments", 58),
        ("ITEM096", "Hot Sauce", "E2", "Condiments", 42),
        ("ITEM097", "Salsa", "E2", "Condiments", 48),
        ("ITEM098", "Olive Oil", "E2", "Condiments", 52),
        ("ITEM099", "Vinegar", "E2", "Condiments", 46),
        ("ITEM100", "Ranch Dressing", "E2", "Condiments", 54),
        
        # Frozen Foods - Shelf F1
        ("ITEM101", "Frozen Pizza", "F1", "Frozen Foods", 65),
        ("ITEM102", "Ice Cream Vanilla", "F1", "Frozen Foods", 50),
        ("ITEM103", "Ice Cream Chocolate", "F1", "Frozen Foods", 48),
        ("ITEM104", "Frozen Vegetables Mix", "F1", "Frozen Foods", 70),
        ("ITEM105", "Frozen Berries", "F1", "Frozen Foods", 55),
        ("ITEM106", "Fish Sticks", "F1", "Frozen Foods", 45),
        ("ITEM107", "Chicken Nuggets", "F1", "Frozen Foods", 60),
        ("ITEM108", "French Fries", "F1", "Frozen Foods", 80),
        ("ITEM109", "Frozen Waffles", "F1", "Frozen Foods", 42),
        ("ITEM110", "Frozen Burritos", "F1", "Frozen Foods", 52),
        
        # Meat & Poultry - Shelf F2
        ("ITEM111", "Chicken Breast", "F2", "Meat & Poultry", 40),
        ("ITEM112", "Ground Beef", "F2", "Meat & Poultry", 55),
        ("ITEM113", "Pork Chops", "F2", "Meat & Poultry", 35),
        ("ITEM114", "Bacon", "F2", "Meat & Poultry", 60),
        ("ITEM115", "Sausages", "F2", "Meat & Poultry", 50),
        ("ITEM116", "Turkey Breast", "F2", "Meat & Poultry", 38),
        ("ITEM117", "Ham Slices", "F2", "Meat & Poultry", 45),
        ("ITEM118", "Beef Steak", "F2", "Meat & Poultry", 30),
        ("ITEM119", "Lamb Chops", "F2", "Meat & Poultry", 25),
        ("ITEM120", "Chicken Wings", "F2", "Meat & Poultry", 48),
        
        # Seafood - Shelf G1
        ("ITEM121", "Salmon Fillet", "G1", "Seafood", 35),
        ("ITEM122", "Shrimp", "G1", "Seafood", 45),
        ("ITEM123", "Cod Fillet", "G1", "Seafood", 32),
        ("ITEM124", "Tilapia", "G1", "Seafood", 38),
        ("ITEM125", "Tuna Steak", "G1", "Seafood", 28),
        ("ITEM126", "Lobster Tail", "G1", "Seafood", 20),
        ("ITEM127", "Crab Legs", "G1", "Seafood", 22),
        ("ITEM128", "Scallops", "G1", "Seafood", 25),
        ("ITEM129", "Mussels", "G1", "Seafood", 30),
        ("ITEM130", "Clams", "G1", "Seafood", 28),
        
        # Deli - Shelf G2
        ("ITEM131", "Sliced Turkey", "G2", "Deli", 55),
        ("ITEM132", "Sliced Ham", "G2", "Deli", 50),
        ("ITEM133", "Salami", "G2", "Deli", 42),
        ("ITEM134", "Roast Beef", "G2", "Deli", 45),
        ("ITEM135", "Swiss Cheese Slices", "G2", "Deli", 48),
        ("ITEM136", "Provolone Cheese", "G2", "Deli", 40),
        ("ITEM137", "Pepperoni", "G2", "Deli", 52),
        ("ITEM138", "Bologna", "G2", "Deli", 38),
        ("ITEM139", "Pastrami", "G2", "Deli", 35),
        ("ITEM140", "Prosciutto", "G2", "Deli", 30),
        
        # Spices & Seasonings - Shelf H1
        ("ITEM141", "Black Pepper", "H1", "Spices", 65),
        ("ITEM142", "Sea Salt", "H1", "Spices", 70),
        ("ITEM143", "Garlic Powder", "H1", "Spices", 58),
        ("ITEM144", "Onion Powder", "H1", "Spices", 55),
        ("ITEM145", "Paprika", "H1", "Spices", 48),
        ("ITEM146", "Cumin", "H1", "Spices", 45),
        ("ITEM147", "Oregano", "H1", "Spices", 52),
        ("ITEM148", "Basil", "H1", "Spices", 50),
        ("ITEM149", "Thyme", "H1", "Spices", 46),
        ("ITEM150", "Rosemary", "H1", "Spices", 44),
        
        # Baking Supplies - Shelf H2
        ("ITEM151", "All-Purpose Flour", "H2", "Baking", 80),
        ("ITEM152", "Cake Flour", "H2", "Baking", 45),
        ("ITEM153", "Baking Powder", "H2", "Baking", 60),
        ("ITEM154", "Baking Soda", "H2", "Baking", 58),
        ("ITEM155", "Granulated Sugar", "H2", "Baking", 75),
        ("ITEM156", "Brown Sugar", "H2", "Baking", 65),
        ("ITEM157", "Powdered Sugar", "H2", "Baking", 55),
        ("ITEM158", "Vanilla Extract", "H2", "Baking", 50),
        ("ITEM159", "Chocolate Chips", "H2", "Baking", 70),
        ("ITEM160", "Cocoa Powder", "H2", "Baking", 48),
        
        # Nuts & Seeds - Shelf I1
        ("ITEM161", "Almonds", "I1", "Nuts & Seeds", 55),
        ("ITEM162", "Cashews", "I1", "Nuts & Seeds", 50),
        ("ITEM163", "Peanuts", "I1", "Nuts & Seeds", 60),
        ("ITEM164", "Walnuts", "I1", "Nuts & Seeds", 45),
        ("ITEM165", "Pecans", "I1", "Nuts & Seeds", 40),
        ("ITEM166", "Pistachios", "I1", "Nuts & Seeds", 42),
        ("ITEM167", "Sunflower Seeds", "I1", "Nuts & Seeds", 52),
        ("ITEM168", "Pumpkin Seeds", "I1", "Nuts & Seeds", 48),
        ("ITEM169", "Chia Seeds", "I1", "Nuts & Seeds", 38),
        ("ITEM170", "Flax Seeds", "I1", "Nuts & Seeds", 35),
        
        # Health & Wellness - Shelf I2
        ("ITEM171", "Protein Powder Vanilla", "I2", "Health", 45),
        ("ITEM172", "Protein Powder Chocolate", "I2", "Health", 42),
        ("ITEM173", "Multivitamins", "I2", "Health", 60),
        ("ITEM174", "Vitamin C", "I2", "Health", 55),
        ("ITEM175", "Vitamin D", "I2", "Health", 52),
        ("ITEM176", "Fish Oil", "I2", "Health", 48),
        ("ITEM177", "Probiotics", "I2", "Health", 40),
        ("ITEM178", "Collagen Powder", "I2", "Health", 38),
        ("ITEM179", "Energy Bars", "I2", "Health", 65),
        ("ITEM180", "Electrolyte Drinks", "I2", "Health", 58),
        
        # Baby Products - Shelf J1
        ("ITEM181", "Baby Formula", "J1", "Baby Products", 50),
        ("ITEM182", "Baby Food Apple", "J1", "Baby Products", 45),
        ("ITEM183", "Baby Food Banana", "J1", "Baby Products", 42),
        ("ITEM184", "Baby Cereal", "J1", "Baby Products", 48),
        ("ITEM185", "Diapers Size 1", "J1", "Baby Products", 60),
        ("ITEM186", "Diapers Size 2", "J1", "Baby Products", 58),
        ("ITEM187", "Baby Wipes", "J1", "Baby Products", 70),
        ("ITEM188", "Baby Lotion", "J1", "Baby Products", 40),
        ("ITEM189", "Baby Shampoo", "J1", "Baby Products", 38),
        ("ITEM190", "Baby Powder", "J1", "Baby Products", 35),
        
        # Pet Supplies - Shelf J2
        ("ITEM191", "Dog Food Dry", "J2", "Pet Supplies", 65),
        ("ITEM192", "Dog Food Wet", "J2", "Pet Supplies", 55),
        ("ITEM193", "Cat Food Dry", "J2", "Pet Supplies", 60),
        ("ITEM194", "Cat Food Wet", "J2", "Pet Supplies", 52),
        ("ITEM195", "Dog Treats", "J2", "Pet Supplies", 48),
        ("ITEM196", "Cat Treats", "J2", "Pet Supplies", 45),
        ("ITEM197", "Cat Litter", "J2", "Pet Supplies", 70),
        ("ITEM198", "Dog Toys", "J2", "Pet Supplies", 40),
        ("ITEM199", "Cat Toys", "J2", "Pet Supplies", 38),
        ("ITEM200", "Pet Shampoo", "J2", "Pet Supplies", 42),
    ]
    
    added_count = 0
    skipped_count = 0
    
    for item_id, name, shelf, category, quantity in sample_items:
        try:
            ItemCRUD.create_item(item_id, name, shelf, category, quantity)
            added_count += 1
            print(f"✅ Added: {name} (Shelf: {shelf})")
        except Exception as e:
            skipped_count += 1
            print(f"⚠️  Skipped {name}: {e}")
    
    print(f"\n{'='*50}")
    print(f"✅ Database seeding complete!")
    print(f"   Total items: {added_count + skipped_count}")
    print(f"   Successfully added: {added_count} items")
    print(f"   Skipped: {skipped_count} items")
    print(f"{'='*50}")
    
    # Print summary by shelf
    print(f"\n📦 Items per shelf:")
    shelves = {}
    for _, _, shelf, _, _ in sample_items:
        shelves[shelf] = shelves.get(shelf, 0) + 1
    
    for shelf in sorted(shelves.keys()):
        print(f"   {shelf}: {shelves[shelf]} items")

if __name__ == "__main__":
    seed_database()