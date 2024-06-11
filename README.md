# Barventory - Command Line Inventory Management for Bars

Barventory is a command-line interface (CLI) application designed to manage inventory for bars that serve alcohol. It provides a user-friendly interface for tracking and managing various aspects of the bar's inventory, including stock levels, purchases, sales, and generating reports. The application utilizes an SQLite database to store and manage data efficiently.

## Features

### Inventory Management

- **Add Items**: Add new items to the inventory with details such as name, category, quantity, and price.
- **View Inventory**: View the current stock levels of all items in the inventory.
- **Update Items**: Update the quantity or price of existing items in the inventory.
- **Remove Items**: Remove items from the inventory when they are no longer available.

### Purchases

- **Record Purchases**: Record purchases of new stock items, specifying the quantity, purchase price, and date.
- **Automatically Update Inventory**: Automatically update the inventory stock levels upon purchase.

### Sales

- **Record Sales**: Record sales transactions, specifying the items sold, quantity, selling price, and date.
- **Automatically Update Inventory**: Automatically update the inventory stock levels upon sale.

### Search and Filter

- **Search Items**: Search for specific items in the inventory using keywords or categories.
- **Filter Inventory**: Filter inventory items based on criteria such as low stock levels or specific categories.

### Data Backup and Restore

- **Backup Data**: Implement functionality to backup the SQLite database to prevent data loss.
- **Restore Data**: Implement functionality to restore the SQLite database from a backup.

### Data Validation and Error Handling

- **Validate Input Data**: Validate input data to ensure accuracy and prevent inconsistencies.
- **Error Handling**: Implement error handling mechanisms to gracefully handle exceptions and errors.

### Interactive Interface

- **User-Friendly CLI**: Design a user-friendly command-line interface with intuitive commands and prompts.
- **Help and Documentation**: Provide help and documentation within the application for users to reference commands and features.

## Usage

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itsivali/Barventory.git

2. Navigate to the project directory:
    ```bash
    cd Barventory

3. Install dependancies
    ```bash
    pip install -r requirements.txt

### Getting Started

1. Setup the database
    ```bash
    python cli.py
 
2. Use the CLI commands to manage inventory, record purchases, and sales, search for items, and perform backup and restore operations.

### Example Usage

#### Add a new item
 ```bash
    python cli.py add --name="Vodka" --category="Spirits" --quantity=20 --price=30.0

#### View inventory
