import sqlite3

def connect_db():
    return sqlite3.connect('barventory.db')

def setup_database():
    conn = connect_db()
    c = conn.cursor()
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS purchases (
        id INTEGER PRIMARY KEY,
        item_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        purchase_price REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        item_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        selling_price REAL NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
    ''')

    conn.commit()
    conn.close()
