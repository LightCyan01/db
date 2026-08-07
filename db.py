import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT,
        done BOOLEAN
    )               
""")

cursor.execute("SELECT COUNT(*) FROM tasks")
count = cursor.fetchone()[0]

if count == 0:
    example = [
        ("Test 1", False),
        ("Test 2", True),
        ("Test 3", False)
    ]
    
    cursor.executemany("""
        INSERT INTO tasks (title, done)
        VALUES (?, ?)                   
    """, example)

conn.commit()
conn.close()
