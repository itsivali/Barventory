from database import connect_db
from utils import validate_quantity, validate_price, handle_error

def record_purchase(item_id, quantity, purchase_price):
    try:
        # Validate inputs
        validate_quantity(quantity)
        validate_price(purchase_price)

        # Connect to the database
        conn = connect_db()
        c = conn.cursor()

        # Record the purchase
        c.execute("INSERT INTO purchases (item_id, quantity, purchase_price, date) VALUES (?, ?, ?, DATE('now'))", 
                  (item_id, quantity, purchase_price))

        # Update the inventory
        c.execute("UPDATE items SET quantity = quantity + ? WHERE id = ?", (quantity, item_id))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print(f"Purchase recorded successfully for item ID {item_id}.")
    except ValueError as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)
