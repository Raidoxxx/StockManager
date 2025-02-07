import sqlite3
from manager.stock import stock_class

def database():
    # Create a sqlite database
    conn = sqlite3.connect('stock.db')

    sqls = [
        '''CREATE TABLE IF NOT EXISTS stock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        create_at TEXT NOT NULL,
        update_at TEXT NOT NULL
        )''',

        '''CREATE TABLE IF NOT EXISTS supplier (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        create_at TEXT NOT NULL,
        update_at TEXT NOT NULL,
        stock_id INTEGER NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock(id)
        )''',

        '''CREATE TABLE IF NOT EXISTS item (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT NOT NULL,
        cost_price REAL NOT NULL,
        sell_price REAL NOT NULL,
        create_at TEXT NOT NULL,
        update_at TEXT NOT NULL,
        supplier_id INTEGER NOT NULL,
        FOREIGN KEY (supplier_id) REFERENCES supplier(id)
        )'''
    ]

    for sql in sqls:
        conn.cursor().execute(sql)
        conn.commit()
    
    conn.close()
    loadData()
            
def main():
    database()

def loadData():
    stock_data = sqlite3.connect('stock.db').cursor().execute('SELECT * FROM stock')
    supplier_data = sqlite3.connect('stock.db').cursor().execute('SELECT * FROM supplier')
    item_data = sqlite3.connect('stock.db').cursor().execute('SELECT * FROM item')
    
if __name__ == "__main__":
    main()