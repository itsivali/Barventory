from database import connect_db
from utils import handle_error

def search_items(keyword):
    try:
        # Connect to the database
        conn = connect_db()
        c = conn.cursor()

        # Search for items by name or category
        query = "%" + keyword + "%"
        c.execute("SELECT * FROM items WHERE name LIKE ? OR category LIKE ?", (query, query))
        items = c.fetchall()
        conn.close()

        # Return search results
        return items
    except Exception as e:
        handle_error(e)
