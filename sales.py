from database import connect_db
from utils import validate_quantity, validate_price, handle_error

def record_sale(item_id, quantity, selling_price):
    try:
        # Validate inputs
        validate_quantity(quantity)
        validate_price(selling_price)

        # Connect to the database
        conn = connect_db()
        c = conn.cursor()

        # Ensure there is enough stock to sell
        c.execute("SELECT quantity FROM items WHERE id = ?", (item_id,))
        current_quantity = c.fetchone()[0]
        if current_quantity < quantity:
            raise ValueError("Not enough stock available to complete the sale.")

        # Record the sale
        c.execute("INSERT INTO sales (item_id, quantity, selling_price, date) VALUES (?, ?, ?, DATE('now'))", 
                  (item_id, quantity, selling_price))

        # Update the inventory
        c.execute("UPDATE items SET quantity = quantity - ? WHERE id = ?", (quantity, item_id))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print(f"Sale recorded successfully for item ID {item_id}.")
    except ValueError as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)
