from database import connect_db

def backup_data(backup_path):
    conn = connect_db()
    with open(backup_path, 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    conn.close()

def restore_data(backup_path):
    conn = connect_db()
    c = conn.cursor()
    with open(backup_path, 'r') as f:
        sql = f.read()
        c.executescript(sql)
    conn.commit()
    conn.close()
