import sqlite3


DB = "tasks.db"

def create_table():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT,
        done BOOLEAN
    )               
    """)
    conn.commit()
    conn.close()

def create_table():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        title TEXT,
        done BOOLEAN
    )               
    """)
    conn.commit()
    conn.close()

def seed_tasks():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
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

def get_tasks():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    
    return tasks

def get_tasks(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    
    task = cursor.fetchone()
    
    conn.close()
    return task