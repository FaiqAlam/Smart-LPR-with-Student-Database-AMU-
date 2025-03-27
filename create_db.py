import sqlite3

def create_database():
    # Connect to SQLite database (this will create the file if it doesn't exist)
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create students table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_plate TEXT UNIQUE,
        name TEXT,
        enrollment_no TEXT,
        hall TEXT,
        room_no TEXT,
        department TEXT
    )
    ''')

    conn.commit()
    conn.close()
    print("Database and table created successfully.")

# Run this script first to set up your database
if __name__ == "__main__":
    create_database()