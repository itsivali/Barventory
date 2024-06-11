from database import connect_db
from utils import validate_item_name, validate_category, validate_quantity, validate_price, handle_error, format_currency

def add_item(name, category, quantity, price):
    try:
        # Validate inputs
        validate_item_name(name)
        validate_category(category)
        validate_quantity(quantity)
        validate_price(price)

        # Connect to the database and add the item
        conn = connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO items (name, category, quantity, price) VALUES (?, ?, ?, ?)", (name, category, quantity, price))
        conn.commit()
        conn.close()
        print(f"Item '{name}' added successfully.")
    except ValueError as e:
        handle_error(e)

def view_inventory():
    try:
        # Connect to the database and fetch all items
        conn = connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM items")
        items = c.fetchall()
        conn.close()

        # Display items
        for item in items:
            print(f"ID: {item[0]}, Name: {item[1]}, Category: {item[2]}, Quantity: {item[3]}, Price: {format_currency(item[4])}")
    except Exception as e:
        handle_error(e)

def update_item(item_id, quantity=None, price=None):
    try:
        # Connect to the database
        conn = connect_db()
        c = conn.cursor()

        # Update quantity if provided
        if quantity is not None:
            validate_quantity(quantity)
            c.execute("UPDATE items SET quantity = ? WHERE id = ?", (quantity, item_id))

        # Update price if provided
        if price is not None:
            validate_price(price)
            c.execute("UPDATE items SET price = ? WHERE id = ?", (price, item_id))

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print(f"Item '{item_id}' updated successfully.")
    except ValueError as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)

def remove_item(item_id):
    try:
        # Connect to the database and delete the item
        conn = connect_db()
        c = conn.cursor()
        c.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        conn.close()
        print(f"Item '{item_id}' removed successfully.")
    except Exception as e:
        handle_error(e)
