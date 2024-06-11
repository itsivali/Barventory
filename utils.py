import re

def validate_item_name(name):
    """Validate the item name to ensure it is not empty and contains only valid characters."""
    if not name or not re.match("^[a-zA-Z0-9 _-]+$", name):
        raise ValueError("Invalid item name. Name must contain only alphanumeric characters, spaces, underscores, and hyphens.")
    return True

def validate_category(category):
    """Validate the category name to ensure it is not empty and contains only valid characters."""
    if not category or not re.match("^[a-zA-Z0-9 _-]+$", category):
        raise ValueError("Invalid category name. Category must contain only alphanumeric characters, spaces, underscores, and hyphens.")
    return True

def validate_quantity(quantity):
    """Validate the quantity to ensure it is a non-negative integer."""
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Invalid quantity. Quantity must be a non-negative integer.")
    return True

def validate_price(price):
    """Validate the price to ensure it is a non-negative float."""
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Invalid price. Price must be a non-negative number.")
    return True

def format_currency(value):
    """Format a numerical value as currency."""
    return "${:,.2f}".format(value)

def handle_error(e):
    """Handle exceptions by printing an error message."""
    print(f"Error: {e}")

def confirm_action(prompt):
    """Prompt the user for confirmation before performing an action."""
    while True:
        response = input(f"{prompt} (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid response. Please enter 'y' for yes or 'n' for no.")
