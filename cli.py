import click
from items import add_item, view_inventory, update_item, remove_item
from purchases import record_purchase
from sales import record_sale
from backup_restore import backup_data, restore_data
from search import search_items
from database import setup_database

@click.group()
def cli():
    """Barventory CLI application."""
    pass

@cli.command()
@click.option('--name', prompt='Item name', help='Name of the item')
@click.option('--category', prompt='Item category', help='Category of the item')
@click.option('--quantity', prompt='Quantity', type=int, help='Quantity of the item')
@click.option('--price', prompt='Price', type=float, help='Price of the item')
def add(name, category, quantity, price):
    """Add a new item to the inventory."""
    add_item(name, category, quantity, price)

@cli.command()
def view():
    """View the current stock levels of all items."""
    view_inventory()

@cli.command()
@click.option('--item_id', prompt='Item ID', type=int, help='ID of the item to update')
@click.option('--quantity', prompt='New quantity', type=int, help='New quantity of the item', required=False)
@click.option('--price', prompt='New price', type=float, help='New price of the item', required=False)
def update(item_id, quantity, price):
    """Update the quantity or price of an existing item."""
    update_item(item_id, quantity, price)

@cli.command()
@click.option('--item_id', prompt='Item ID', type=int, help='ID of the item to remove')
def remove(item_id):
    """Remove an item from the inventory."""
    remove_item(item_id)

@cli.command()
@click.option('--item_id', prompt='Item ID', type=int, help='ID of the item purchased')
@click.option('--quantity', prompt='Quantity purchased', type=int, help='Quantity purchased')
@click.option('--purchase_price', prompt='Purchase price', type=float, help='Purchase price')
def purchase(item_id, quantity, purchase_price):
    """Record a purchase of new stock."""
    record_purchase(item_id, quantity, purchase_price)

@cli.command()
@click.option('--item_id', prompt='Item ID', type=int, help='ID of the item sold')
@click.option('--quantity', prompt='Quantity sold', type=int, help='Quantity sold')
@click.option('--selling_price', prompt='Selling price', type=float, help='Selling price')
def sale(item_id, quantity, selling_price):
    """Record a sales transaction."""
    record_sale(item_id, quantity, selling_price)

@cli.command()
@click.option('--keyword', prompt='Search keyword', help='Keyword to search for')
def search(keyword):
    """Search for specific items in the inventory."""
    items = search_items(keyword)
    for item in items:
        click.echo(f'ID: {item[0]}, Name: {item[1]}, Category: {item[2]}, Quantity: {item[3]}, Price: {item[4]}')

@cli.command()
@click.option('--backup_path', prompt='Backup file path', help='File path to save the backup')
def backup(backup_path):
    """Backup the inventory database."""
    backup_data(backup_path)

@cli.command()
@click.option('--backup_path', prompt='Backup file path', help='File path to restore the backup from')
def restore(backup_path):
    """Restore the inventory database from a backup."""
    restore_data(backup_path)

if __name__ == '__main__':
    setup_database()  # Ensure the database and tables are created
    cli()
