import sqlite3
import shutil
from utils import handle_error

def backup_data(backup_path):
    try:
        # Copy the database file to the backup path
        shutil.copy('barventory.db', backup_path)
        print(f"Database backup successfully created at {backup_path}.")
    except Exception as e:
        handle_error(e)

def restore_data(backup_path):
    try:
        # Copy the backup file to the database path
        shutil.copy(backup_path, 'barventory.db')
        print(f"Database successfully restored from {backup_path}.")
    except Exception as e:
        handle_error(e)
