import sqlite3

def initialize_database():
    conn = sqlite3.connect("BankNH.db")
    cur = conn.cursor()

    # Create Users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL
        )
    """)

    # Create Transactions table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT NOT NULL,
            receiver TEXT NOT NULL,
            ttype TEXT NOT NULL,
            amount REAL NOT NULL,
            sender_old_balance REAL NOT NULL,
            sender_new_balance REAL NOT NULL,
            receiver_old_balance REAL NOT NULL,
            receiver_new_balance REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create FraudLogs table (optional, if fraud is not part of Transactions)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS FraudLogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_id INTEGER NOT NULL,
            reason TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (transaction_id) REFERENCES Transactions (id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()
